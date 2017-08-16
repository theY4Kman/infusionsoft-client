import os
import re
from collections import defaultdict, OrderedDict

try:
    import requests
    import docformatter
    from bs4 import BeautifulSoup
    from stringcase import camelcase
    from yapf.yapflib import yapf_api
except ImportError:
    raise RuntimeError('Please `pip install -r stub-requirements.txt` before '
                       'generating stubs')


__all__ = ['generate_stubs']


INFUSIONSOFT_DOCS_URL = 'https://developer.infusionsoft.com/docs/xml-rpc/'

SCRIPT_PATH = os.path.dirname(__file__)
CACHED_DOCS_PATH = os.path.join(SCRIPT_PATH, '_cached_api_docs.html')

TYPE_MAP = {
    'i4': 'int',
    'integer': 'int',
    'double': 'float',
    'dateTime': 'datetime',
    'dateTime.iso8601': 'datetime',
    'array': 'List',
    'string': 'str',
    'struct': 'Dict[str, Any]',
    'boolean': 'bool',
}


def soupify(html, features='html.parser'):
    return BeautifulSoup(html, features=features)


def download_api_docs_html():
    response = requests.get(INFUSIONSOFT_DOCS_URL)
    assert response.status_code == 200
    return response.content


def has_cached_api_docs_html():
    return os.path.exists(CACHED_DOCS_PATH)


def set_cached_api_docs_html(xml):
    with open(CACHED_DOCS_PATH, 'wb') as fp:
        fp.write(xml)


def get_cached_api_docs_html():
    with open(CACHED_DOCS_PATH, 'rb') as fp:
        return fp.read()


def get_api_docs_html():
    if has_cached_api_docs_html():
        return get_cached_api_docs_html()
    else:
        html = download_api_docs_html()
        set_cached_api_docs_html(html)
        return html


def _parse_params(el_call):
    params = []
    for el_arg in el_call.find_all(class_='argument'):
        el_argname = el_arg.find(class_='col-sm-4')
        if not el_argname:
            # The API docs include an interactive API call explorer, which
            # also use the class name "argument". Thankfully, ".col-sm-4"
            # is not found inside these .arguments :)
            continue

        argname = el_argname.find('b').text.rstrip(':')
        # Sometimes these are human descriptions, not keywords... for shame
        argname = camelcase(argname.replace(' ', ''))

        el_arg_desc = el_arg.find(class_='col-sm-8')
        full_desc = el_arg_desc.text.strip()
        argdesc = full_desc.split('\n', 1)[0]
        type = re.split(r'\s+', argdesc, 1)[0]

        el_req = el_arg_desc.find('b')
        is_required = '(required)' in el_req.text if el_req else False

        # Infusionsoft mislabels all params named "data" as "array",
        # because it dubs them "associative arrays". Arrays in XML-RPC are
        # lists of data. Associative arrays are structs. Infusionsoft even
        # uses "struct" correctly elsewhere. Blech. </rant>
        if argname == 'data':
            type = 'struct'

        params.append((argname, type, is_required))

    # Optional args must be at the end of the signature. If an optional arg is
    # found before a required arg, we presume it's a mistake, and mark it
    # required, too.
    last_required_arg = float('-Inf')
    for i, (arg, type, is_required) in reversed(list(enumerate(params))):
        if is_required:
            last_required_arg = i
            break

    return [
        (arg, type, True if i < last_required_arg else is_required)
        for i, (arg, type, is_required) in enumerate(params)
    ]


def _parse_rtype(el_call, default='None'):
    rtype = default

    # Parse return value from example response value
    el_resp_xml = el_call.find(class_='method-response lang-xml')
    if el_resp_xml:
        resp_xml = el_resp_xml.text
        el_resp = soupify(resp_xml)
        el_value = el_resp.find('value')
        if el_value:
            el_val_children = el_value.findChildren()
            if el_val_children:
                # An explicit <array>, <int>, <string>, etc under <value>
                el_rtype =el_val_children [0]
                rtype = el_rtype.name
            else:
                # Just text under <value> implies <string>
                rtype = 'string'

    return rtype


def _parse_title(el_call):
    el_title = el_call.find('h3')
    title = el_title.find(text=True).strip()
    return title


def _parse_meth_desc(el_call):
    el_meth_desc = el_call.find(class_='method-description')
    el_desc_paras = el_meth_desc.findAll('p', recursive=False)
    desc = '\n\n'.join(el_p.text.strip() for el_p in el_desc_paras)
    return desc


def _parse_meth_name(el_call):
    el_definition = el_call.find(class_='method-declaration lang-xml')
    if el_definition:
        # Most calls have a "Definition" section listing only the name
        name = el_definition.text.strip()
    else:
        # But some do not, and we must parse the example request XML
        req_xml = el_call.find(class_='method-request lang-xml').text
        el_req = soupify(req_xml)
        name = el_req.find('methodname').text
    return name


def extract_services(html):
    doc = soupify(html)

    el_calls = doc.find_all(class_='method',
                            id=re.compile('^(?!introduction|authentication)'))
    services = defaultdict(OrderedDict)
    for el_call in el_calls:
        if not el_call.find(class_='lang-xml'):
            # These are introduction sections
            continue

        params = _parse_params(el_call)
        rtype = _parse_rtype(el_call)
        title = _parse_title(el_call)
        desc = _parse_meth_desc(el_call)
        name = _parse_meth_name(el_call)

        service, method = name.split('.', 1)
        services[service][method] = (params, rtype, title, desc)

    return services


def render_stubs(services):

    lines = [
        'from typing import Any, Dict, List',
        'from datetime import date, datetime',
        '',
        '__all__ = [',
    ]

    lines += ["    '{name}',".format(name=name) for name in sorted(services)]
    lines += [
        ']',
        '',
        ''
    ]

    for service, methods in sorted(services.items()):
        lines.append('class {service}:'.format(service=service))
        methods = sorted(methods.items())
        for name, (params, rtype, title, desc) in methods:
            # apiKey is always first param, which is handled automatically by
            # DefaultArgServerProxy, so we ignore it here.
            params = params[1:]

            proto_parts = []
            for arg, type, is_required in params:
                part = '{arg}: {type}'.format(arg=arg,
                                              type=TYPE_MAP.get(type, type))
                if not is_required:
                    part += '=None'
                proto_parts.append(part)
            proto = ', '.join(proto_parts)

            rtype = TYPE_MAP.get(rtype, rtype)

            indent = ' ' * 8
            docstring_parts = [title + '\n' if title else None]
            docstring_parts += [(indent + line).rstrip()
                                for line in desc.split('\n')]
            docstring_contents = '\n'.join(docstring_parts).strip()

            fmt_params = {
                'name': name,
                'proto': proto,
                'rtype': rtype,
                'docstring': docstring_contents,
            }

            indent = ' ' * 4
            meth_lines = [
                '@staticmethod',
                'def {name}({proto}) -> {rtype}:'.format(**fmt_params),
                '    """{docstring}'.format(**fmt_params),
                '    """',
                '    pass',
                '',
            ]
            lines += [indent + line for line in meth_lines]
        lines.append('')

    # Format according to PEP-8
    source = '\n'.join(lines)
    source, _ = yapf_api.FormatCode(source, 'stubs.py')
    source = docformatter.format_code(source, **{
        'description_wrap_length': 79,
        'post_description_blank': False,
    })

    return source


def generate_stubs():
    html = get_api_docs_html()
    services = extract_services(html)
    source = render_stubs(services)
    return source


if __name__ == '__main__':
    print(generate_stubs())
