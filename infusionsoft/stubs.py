########################
# STUBS FOR CODE SENSE #
########################

from typing import List, Dict
from datetime import datetime, date


class APIAffiliateService:
    @staticmethod
    def affClawbacks(affiliateId: int, filterStartDate: datetime,
                     filterEndDate: datetime) -> List:
        """Retrieve Clawbacks

        Retrieves all clawed back commissions for a particular affiliate. Claw
        backs typically occur when an order has been refunded to the customer.
        """
        pass

    @staticmethod
    def affCommissions(affiliateId: int, filterStartDate: datetime,
                       filterEndDate: datetime) -> List:
        """Retrieve Commissions

        Retrieves all commissions for a specific affiliate within a date range.
        """
        pass

    @staticmethod
    def affPayouts(affiliateId: int, filterStartDate: datetime,
                   filterEndDate: datetime) -> List:
        """Retrieve Payments

        Retrieves all payments for a specific affiliate within a date range
        """
        pass

    @staticmethod
    def affRunningTotals(affiliateIds: List) -> List:
        """Retrieve Running Totals

        Retrieves the current balances for Amount Earned, Clawbacks, and
        Running Balance.
        """
        pass

    @staticmethod
    def affSummary(affiliateId: int, filterStartDate: datetime,
                   filterEndDate: datetime) -> List:
        """Retrieve a Summary of Affiliate Statistics

        Retrieves a summary of statistics for a list of affiliates.
        """
        pass


class APIEmailService:
    @staticmethod
    def addEmailTemplate(templateName: str, categories: str, fromAddress: str,
                         toAddress: str, ccAddress: str, bccAddress: str,
                         subject: str, textBody: str, htmlBody: str,
                         contentType: str, mergeContext: str) -> int:
        """Create an Email Template

        Creates a new email template that can be used when sending emails.
        """
        pass

    @staticmethod
    def attachEmail(contactId: int, fromName: str, fromAddress: str,
                    toAddress: str, ccAddresses: str, bccAddresses: str,
                    contentType: str, subject: str, htmlBody: str,
                    textBody: str, header: str, receivedDate: str,
                    sentDate: str, emailSentType: int) -> bool:
        """Manually Log a Sent Email

        This will create an item in the email history for a contact. This does
        not actually send the email, it only places an item into the email
        history. Using the API to instruct Infusionsoft to send an email will
        handle this automatically.
        """
        pass

    @staticmethod
    def getEmailTemplate(templateId: str) -> Dict[str, any]:
        """Retrieve an Email Template
        """
        pass

    @staticmethod
    def getOptStatus(email: str) -> int:
        """Retrieve an Email's Opt-in Status
        """
        pass

    @staticmethod
    def optIn(email: str, optInReason: str) -> bool:
        """Opt-in an Email Address

        Opts-in an email address. This method only works the first time an
        email address opts-in.
        """
        pass

    @staticmethod
    def optOut(email: str, optOutReason: str) -> bool:
        """Opt-out an Email Address

        Opts-out an email address. Once an address is opt-out, the API cannot
        opt it back in.
        """
        pass

    @staticmethod
    def sendEmail(contactList: List, fromAddress: str, toAddress: str,
                  ccAddresses: str, bccAddresses: str, contentType: str,
                  subject: str, htmlBody: str, textBody: str,
                  templateID: str) -> bool:
        """Send an Email

        Send an email to a list of contacts, as well as records the email in
        each contacts' email history.
        """
        pass

    @staticmethod
    def updateEmailTemplate(templateId: str, templateName: str,
                            categories: str, fromAddress: str, toAddress: str,
                            ccAddress: str, bccAddress: str, subject: str,
                            textBody: str, htmlBody: str, contentType: str,
                            mergeContext: str) -> int:
        """Update an Email Template

        Updates an email template that can be used when sending emails.
        """
        pass


class AffiliateProgramService:
    @staticmethod
    def getAffiliatePrograms() -> Dict[str, any]:
        """Retrieve All Programs

        Retrieves a list of all of the Affiliate Programs that are in the
        application.
        """
        pass

    @staticmethod
    def getAffiliatesByProgram(programId: int) -> None:
        """Retrieve a Program's Affiliates

        Retrieves a list of all of the affiliates with their contact data for
        the specified program. This includes all of the custom fields defined
        for the contact and affiliate records that are retrieved.
        """
        pass

    @staticmethod
    def getProgramsForAffiliate(affiliateId: int) -> Dict[str, any]:
        """Retrieve an Affiliate's Programs

        Retrieves a list of all of the Affiliate Programs for the Affiliate
        specified.
        """
        pass

    @staticmethod
    def getResourcesForAffiliateProgram(programId: int) -> None:
        """Retrieve Program Resources

        Retrieves a list of all of the resources that are associated to the
        Affiliate Program specified.
        """
        pass


class AffiliateService:
    @staticmethod
    def getRedirectLinksForAffiliate(affiliateId: int) -> List:
        """Retrieve Redirect Links

        Retrieves a list of the redirect links for the specified Affiliate.
        """
        pass


class ContactService:
    @staticmethod
    def add(data: Dict[str, any]) -> int:
        """Create a Contact

        Creates a new contact record from the data passed in the associative
        array.
        """
        pass

    @staticmethod
    def addToCampaign(contactId: int, campaignId: int) -> bool:
        """Add a Contact to a Follow-up Sequence

        Adds a contact to a follow-up sequence (campaigns were the original
        name of follow-up sequences).
        """
        pass

    @staticmethod
    def addToGroup(contactId: int, tagId: int) -> bool:
        """Add a Tag to a Contact

        Adds a tag to a contact record (tags were originally called "groups").
        """
        pass

    @staticmethod
    def addWithDupCheck(data: Dict[str, any], dupCheckType: str) -> int:
        """Create a Contact and Check for Duplicates

        Adds or updates a contact record based on matching data
        """
        pass

    @staticmethod
    def findByEmail(email: str, selectedFields: List) -> List:
        """Search for a Contact by an Email Address

        Retrieves all contacts with the given email address. This searches the
        Email, Email 2, and Email 3 fields
        """
        pass

    @staticmethod
    def getNextCampaignStep(contactId: int, followUpSequenceId: int) -> None:
        """Retrieve a Contact's Next Follow-up Sequence Step

        Returns the Id number of the next follow-up sequence step for the given
        contact
        """
        pass

    @staticmethod
    def linkContacts(contactId1: int, contactId2: int,
                     linkTypeId: int) -> bool:
        """Link Contacts

        This will link 2 contacts together using the specified link type.
        """
        pass

    @staticmethod
    def listLinkedContacts(contactId: int) -> List:
        """List Linked Contacts

        This will list all linked contacts to the given contact id.
        """
        pass

    @staticmethod
    def load(contactId: int, selectedFields: List) -> Dict[str, any]:
        """Retrieve a Contact
        """
        pass

    @staticmethod
    def merge(contactId: int, duplicateContactId: int) -> bool:
        """Merge Two Contacts

        Merges two contacts into a single record.
        """
        pass

    @staticmethod
    def pauseCampaign(contactId: int, sequenceId: int) -> bool:
        """Pause a Follow-up Sequence for a Contact

        Pauses a follow-up sequence for the given contact record
        """
        pass

    @staticmethod
    def removeFromCampaign(contactId: int, followUpSequenceId: int) -> bool:
        """Remove a Contact from a Follow-up Sequence

        Removes a follow-up sequence from a contact record
        """
        pass

    @staticmethod
    def removeFromGroup(contactId: int, tagId: int) -> bool:
        """Remove a Tag from a Contact

        Removes a tag from a contact (tags were originally called groups).
        """
        pass

    @staticmethod
    def rescheduleCampaignStep(contactIds: List, sequenceStepId: int) -> int:
        """Immediately Execute a Follow-up Sequence Step for Multiple Contacts

        Immediately performs the given follow-up sequence step for the given
        contacts.
        """
        pass

    @staticmethod
    def resumeCampaignForContact(contactId: int, seqId: int) -> bool:
        """Resume a Follow-up Sequence for a Contact

        Resumes a follow-up sequence that has been stopped/paused for a given
        contact.
        """
        pass

    @staticmethod
    def runActionSequence(contactId: int, actionSetId: int) -> List:
        """Run an Action Set for a Contact

        Runs an action sequence on a given contact record
        """
        pass

    @staticmethod
    def unlinkContacts(contactId1: int, contactId2: int,
                       linkTypeId: int) -> bool:
        """Unlink Contacts

        Unlink contacts with a specific link type
        """
        pass

    @staticmethod
    def update(contactId: int, data: Dict[str, any]) -> int:
        """Update a Contact

        Updates a contact's information
        """
        pass


class DataService:
    @staticmethod
    def add(table: str, values: Dict[str, any]) -> int:
        """Create a Record

        Creates a new record in the specified Infusionsoft data table.
        """
        pass

    @staticmethod
    def addCustomField(customFieldType: str, displayName: str, dataType: str,
                       headerID: int) -> int:
        """Create a Custom Field

        Creates a new custom field
        """
        pass

    @staticmethod
    def authenticateUser(username: str, passwordHash: str) -> Dict[str, any]:
        """Validate a User's Credentials

        Validates an Infusionsoft username and password (as an MD5 hash).
        """
        pass

    @staticmethod
    def count(table: str, queryData: Dict[str, any]) -> int:
        """Count a Data Table's Records

        Performs a query across the given table based on the query data and
        returns the count of records.
        """
        pass

    @staticmethod
    def delete(table: str, iD: int) -> bool:
        """Delete a Record

        Deletes the specified record in the given table from the database
        """
        pass

    @staticmethod
    def findByField(table: str, limit: int, page: int, fieldName: str,
                    fieldValue: str, returnFields: List) -> List:
        """Find a Record by Matching a Specific Field

        Retrieves all records in a table that match the given term on a
        specific field.
        """
        pass

    @staticmethod
    def getAppSetting(module: str, setting: str) -> str:
        """Retrieve Application Setting

        Retrieves the value of a given setting in the current application. In
        order to find the module and option names, view the HTML field name
        within the Infusionsoft settings. You will see something such as
        name="Contact_WebModule0optiontypes". The portion before the underscore
        is the module name. "Contact" in this example. The portion after the 0
        is the setting name, "optiontypes" in this example.
        """
        pass

    @staticmethod
    def getAppointmentICal(appointmentId: int) -> str:
        """Retrieve an Appointment's iCalendar File

        Retrieves the iCalendar file for the specified appointment
        """
        pass

    @staticmethod
    def load(table: str, recordID: int, fields: List) -> Dict[str, any]:
        """Retrieve a Record

        Loads the requested fields from a specified record.
        """
        pass

    @staticmethod
    def query(table: str, limit: int, page: int, queryData: Dict[str, any],
              selectedFields: List, orderBy: str, ascending: bool) -> List:
        """Query a Data Table

        Performs a query across the given table based on the query data.
        """
        pass

    @staticmethod
    def update(table: str, recordID: int, values: Dict[str, any]) -> int:
        """Update a Record

        Updates a specific record in the specified Infusionsoft data table.
        """
        pass

    @staticmethod
    def updateCustomField(customFieldId: int, values: Dict[str, any]) -> Dict[
        str, any]:
        """Update a Custom Field

        Updates the value of a custom field. Every field can have it's display
        name and group id changed, but only certain data types will allow you
        to actually change values (dropdown, listbox, radio, etc).
        """
        pass


class DiscountService:
    @staticmethod
    def addCategoryAssignmentToCategoryDiscount(iD: int,
                                                productID: int) -> int:
        """Assign a Product to a Category Discount
        """
        pass

    @staticmethod
    def addCategoryDiscount(name: str, description: str,
                            applyDiscountToCommission: int, amt: int) -> int:
        """Create a Category Discount
        """
        pass

    @staticmethod
    def addFreeTrial(name: str, description: str, freeTrialDays: int,
                     hidePrice: int, subscriptionPlanID: int) -> int:
        """Create a Free Trial on a Subscription
        """
        pass

    @staticmethod
    def addOrderTotalDiscount(name: str, applyDiscountToCommission: int,
                              percentOrAmt: int, payType: str) -> int:
        """Create an Order Discount
        """
        pass

    @staticmethod
    def addProductTotalDiscount(name: str, description: str,
                                applyDiscountToCommission: int, productID: int,
                                percentOrAmt: int, amt: float) -> int:
        """Create a Product Discount
        """
        pass

    @staticmethod
    def addShippingTotalDiscount(name: str, description: str,
                                 applyDiscountToCommission: int,
                                 percentOrAmt: int, amt: float) -> int:
        """Create a Shipping Discount
        """
        pass

    @staticmethod
    def getCategoryAssignmentsForCategoryDiscount(iD: int) -> List:
        """Retrieve a Category Discount's Category Assignments

        Retrieves the options and values of the category assignment for
        category discount passed.
        """
        pass

    @staticmethod
    def getCategoryDiscount(iD: int) -> Dict[str, any]:
        """Retrieve a Category Discount

        Returns the options and values of the specified category discount ID.
        """
        pass

    @staticmethod
    def getFreeTrial(trialId: int) -> Dict[str, any]:
        """Retrieve a Subscription's Free Trial
        """
        pass

    @staticmethod
    def getOrderTotalDiscount(iD: int) -> Dict[str, any]:
        """Retrieve an Order's Total Discount
        """
        pass

    @staticmethod
    def getProductTotalDiscount(productDiscountID: str) -> Dict[str, any]:
        """Retrieve a Product Total Discount
        """
        pass

    @staticmethod
    def getShippingTotalDiscount(shippingDiscountID: int) -> Dict[str, any]:
        """Retrieve a Shipping Discount
        """
        pass


class FileService:
    @staticmethod
    def getDownloadUrl(fileID: str) -> str:
        """Retrieve a File Download URL
        """
        pass

    @staticmethod
    def getFile(fileID: int) -> str:
        """Retrieve a File

        Retrieves the file data for the specified file ID.
        """
        pass

    @staticmethod
    def renameFile(fileID: str, fileName: str) -> bool:
        """Rename a File
        """
        pass

    @staticmethod
    def replaceFile(fileName: str, base64EncodedData: str) -> int:
        """Replace a File

        Replaces a file's data.
        """
        pass

    @staticmethod
    def uploadFile(contactID: int, fileName: str,
                   base64EncodedData: str) -> int:
        """Upload a File

        Uploads a file to Infusionsoft. The optional contactID parameter is
        used to place the file in a specific contact's filebox.
        """
        pass


class FunnelService:
    @staticmethod
    def achieveGoal(integration: str, callName: str, contactID: int) -> List:
        """Achieve a Goal
        """
        pass


class InvoiceService:
    @staticmethod
    def addManualPayment(invoiceID: int, amount: float, date: datetime,
                         paymentType: str, description: str,
                         bypassCommissions: bool) -> bool:
        """Add a Payment to an Invoice

        Adds a payment to an invoice without actually processing a charge
        through a merchant. This is useful if you accept cash/check, or handle
        payments outside of Infusionsoft.
        """
        pass

    @staticmethod
    def addOrderCommissionOverride(invoiceID: int, affiliateID: int,
                                   productID: int, percent: int, amount: float,
                                   payoutType: int, description: str,
                                   date: datetime) -> bool:
        """Add a Commission to an Invoice

        Adds a commission to an existing invoice
        """
        pass

    @staticmethod
    def addOrderItem(invoiceID: int, productID: int, type: int, price: float,
                     quantity: int, description: str, notes: str) -> bool:
        """Add an Item to an Invoice

        Adds a line item to an invoice.
        """
        pass

    @staticmethod
    def addPaymentPlan(invoiceID: int, autoCharge: bool, creditCardID: int,
                       merchantAccountID: int, daysUntilRetry: int,
                       maxRetry: int, initialPaymentAmount: float,
                       initialPaymentDate: datetime, planStartDate: datetime,
                       numberOfPayments: int,
                       daysBetweenPayments: int) -> bool:
        """Create a Custom Recurring Payment

        Creates a custom recurring payment for an invoice.
        """
        pass

    @staticmethod
    def addRecurringOrder(contactID: int, allowDuplicate: bool,
                          subscriptionID: int, quantity: int, price: float,
                          taxable: bool, merchantAccountID: int,
                          creditCardID: int, affiliateID: int,
                          trialPeriod: int) -> int:
        """Create a Contact Subscription

        Creates a subscription for a contact. Subscriptions are billed
        automatically by Infusionsoft within six hours of creation. If you want
        to bill immediately you will need to then call the
        InvoiceService.createInvoiceForRecurring and
        InvoiceService.chargeInvoice methods.
        """
        pass

    @staticmethod
    def calculateAmountOwed(invoiceID: int) -> float:
        """Retrieve Invoice Amount Due

        Retrieves the outstanding amount of an invoice
        """
        pass

    @staticmethod
    def chargeInvoice(invoiceID: int, notes: str, creditCardID: int,
                      merchantAccountID: int, bypassComissions: bool) -> Dict[
        str, any]:
        """Pay an Invoice

        Charges the specified card the amount currently due on the invoice.
        """
        pass

    @staticmethod
    def createBlankOrder(contactID: int, name: str, orderDate: datetime,
                         leadAffiliateID: int, saleAffiliateID: int) -> int:
        """Create an Invoice

        Creates a blank invoice with no line items that has not yet been paid.
        """
        pass

    @staticmethod
    def createInvoiceForRecurring(subscriptionID: int) -> int:
        """Create a Subscription Invoice

        Creates an invoice for all charges due on a subscription. If the
        subscription has multiple billing cycles due, it will create a single
        invoice with charges for all charges due.
        """
        pass

    @staticmethod
    def deleteInvoice(invoiceID: str) -> bool:
        """Delete an Invoice

        Deletes an invoice. Also deletes the order within the Job table tied to
        the invoice.
        """
        pass

    @staticmethod
    def deleteSubscription(subscriptionID: str) -> bool:
        """Delete a Subscription

        Deletes the specified subscription, as well as all invoices tied to the
        subscription.
        """
        pass

    @staticmethod
    def getAllPaymentOptions() -> Dict[str, any]:
        """Retrieve Available Payment Options

        Retrieves all payment types available within the requested Infusionsoft
        account
        """
        pass

    @staticmethod
    def getAllShippingOptions() -> None:
        """Retrieve Available Shipping Options

        Retrieves all shipping options available in the specified Infusionsoft
        account
        """
        pass

    @staticmethod
    def getPayments(invoiceID: int) -> List:
        """Retrieve Invoice Payments
        """
        pass

    @staticmethod
    def locateExistingCard(contactID: int, lastFour: str) -> int:
        """Retrieve Credit Card

        Retrieves a credit card for the specified contact
        """
        pass

    @staticmethod
    def recalculateTax(invoiceID: int) -> bool:
        """Calculate Invoice Tax

        Calculates tax based on the line items of the invoice, and adds the
        amount to the invoice.
        """
        pass

    @staticmethod
    def updateJobRecurringNextBillDate(subscriptionID: int,
                                       nextBillDate: date) -> bool:
        """Update Subscription Billing Date

        Changes the next date a subscription is paid
        """
        pass

    @staticmethod
    def validateCreditCard(cardID: int) -> Dict[str, any]:
        """Validate an Existing Credit Card
        """
        pass


class OrderService:
    @staticmethod
    def placeOrder(contactID: int, cardID: int, planID: int, productIDs: List,
                   subscriptionIDs: List, processSpecials: bool,
                   promoCodes: List, leadAffiliateID: int,
                   saleAffiliateID: int) -> Dict[str, any]:
        """Create an Order
        """
        pass


class ProductService:
    @staticmethod
    def deactivateCreditCard(cardID: int) -> bool:
        """Deactivate a Credit Card
        """
        pass

    @staticmethod
    def decreaseInventory(productID: int, quantity: int) -> bool:
        """Decrease a Product's Available Inventory

        Decreases the available inventory for the specified product.
        """
        pass

    @staticmethod
    def decrementInventory(productID: str) -> bool:
        """Decrement Available Product Inventory

        Decrements the specified product's inventory by one unit.
        """
        pass

    @staticmethod
    def getInventory(productID: int) -> int:
        """Retrieve Available Product Inventory
        """
        pass

    @staticmethod
    def increaseInventory(productID: int, quantity: int) -> bool:
        """Increase a Product's Available Inventory

        Increases the available inventory for the specified product.
        """
        pass

    @staticmethod
    def incrementInventory(productID: int) -> bool:
        """Increment Available Product Inventory

        Increments the specified product's inventory by one unit.
        """
        pass


class SearchService:
    @staticmethod
    def getAllReportColumns(savedSearchID: int, userID: int) -> Dict[str, any]:
        """Retrieve a Report's Available Fields
        """
        pass

    @staticmethod
    def getAvailableQuickSearches(userID: int) -> Dict[str, any]:
        """Retrieve Available Quick Searches
        """
        pass

    @staticmethod
    def getDefaultQuickSearch(userID: int) -> str:
        """Retrieve the Default Quick Search
        """
        pass

    @staticmethod
    def getSavedSearchResults(savedSearchID: int, userID: int, pageNumber: int,
                              returnFields: List) -> List:
        """Retrieve a Partial Report from a Saved Search
        """
        pass

    @staticmethod
    def getSavedSearchResultsAllFields(savedSearchID: int, userID: int,
                                       pageNumber: int) -> List:
        """Retrieve a Complete Report from a Saved Search
        """
        pass

    @staticmethod
    def quickSearch(searchType: int, userID: int, searchData: str, page: int,
                    limit: int) -> List:
        """Retrieve a Quick Search Report

        Returns a quick search, equivalent to using the search box in the
        Infusionsoft application.
        """
        pass


class ShippingService:
    @staticmethod
    def getAllShippingOptions() -> List:
        """Retrieve Available Shipping Options
        """
        pass

    @staticmethod
    def getFlatRateShippingOption(optionID: str) -> Dict[str, any]:
        """Retrieve Flat Rate Shipping Options
        """
        pass

    @staticmethod
    def getOrderQuantityShippingOption(optionID: int) -> Dict[str, any]:
        """Retrieve Order Quantity Shipping Options
        """
        pass

    @staticmethod
    def getOrderTotalShippingOption(optionID: int) -> List:
        """Retrieve Order Shipping Options
        """
        pass

    @staticmethod
    def getOrderTotalShippingRanges(optionID: int) -> List:
        """Retrieve Order Shipping Ranges
        """
        pass

    @staticmethod
    def getProductBasedShippingOption(optionID: int) -> Dict[str, any]:
        """Retrieve Product Shipping Options
        """
        pass

    @staticmethod
    def getUpsShippingOption(optionID: int) -> Dict[str, any]:
        """Retrieve UPS Shipping Option
        """
        pass

    @staticmethod
    def getWeightBasedShippingOption(optionID: int) -> Dict[str, any]:
        """Retrieve Weight-Based Shipping Options
        """
        pass


class WebFormService:
    @staticmethod
    def getHTML(formID: int) -> str:
        """Retrieve a Form's HTML
        """
        pass

    @staticmethod
    def getMap() -> Dict[str, any]:
        """Retrieve Webform IDs
        """
        pass
