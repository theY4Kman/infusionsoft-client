import os

from setuptools import setup


def build_install_requires(path):
    """Support pip-type requirements files"""
    basedir = os.path.dirname(path)
    with open(path) as f:
        reqs = []
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == '#':
                continue
            elif line.startswith('-r '):
                nested_req = line[3:].strip()
                nested_path = os.path.join(basedir, nested_req)
                reqs += build_install_requires(nested_path)
            elif line[0] == '-':
                continue
            else:
                reqs.append(line)
        return reqs


pkg = 'infusionsoft'
root = os.path.dirname(__file__)
from_root = lambda *p: os.path.join(root, *p)
pkg_root = lambda *p: from_root(pkg, *p)

with open(from_root('README.rst')) as fp:
    long_description = fp.read()


with open(pkg_root('version.py')) as fp:
    context = {}
    exec(fp.read(), None, context)
    version = context['__version__']


setup(
    name='infusionsoft-client',
    version=version,
    author='Zach "theY4Kman" Kanzler',
    author_email='they4kman@gmail.com',
    description='Sexy Infusionsoft XML-RPC API client',
    long_description=long_description,
    packages=[pkg],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries',
    ],
    install_requires=build_install_requires(from_root('requirements.txt')),
    include_package_data=True,
)
