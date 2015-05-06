#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.personOrInstitution import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))

class ListField(schema.List):
    """We need to have a unique class for the field list so that we
    can apply a custom adapter."""
    pass

# # # # # # # # # # # # #
# Widget interface      #
# # # # # # # # # # # # #

class IFormWidget(Interface):
    pass

# # # # # # # # # # # # # #
# DataGrid interfaces     # 
# # # # # # # # # # # # # #
class INameType(Interface):
    type = schema.TextLine(title=_(u'Name type'), required=False)

class IUse(Interface):
    term = schema.TextLine(title=_(u'Use'), required=False)

class IUsedFor(Interface):
    term = schema.TextLine(title=_(u'Used for'), required=False)

class IEquivalent(Interface):
    name = schema.TextLine(title=_(u'Equivalent'), required=False)

class IAddressDetails(Interface):
    addressType = schema.TextLine(title=_(u'Address type'), required=False)
    address = schema.TextLine(title=_(u'Address'), required=False)
    postalCode = schema.TextLine(title=_(u'Postal code'), required=False)
    place = schema.TextLine(title=_(u'Place'), required=False)
    country = schema.TextLine(title=_(u'Country'), required=False)

class ITelephone(Interface):
    phone = schema.TextLine(title=_(u'Telephone'), required=False)

class IFax(Interface):
    fax = schema.TextLine(title=_(u'Fax'), required=False)

class IEmail(Interface):
    email = schema.TextLine(title=_(u'Email'), required=False)

class IWebsite(Interface):
    url = schema.TextLine(title=_(u'Website'), required=False)

class IContacts(Interface):
    name = schema.TextLine(title=_(u'Name'), required=False)
    jobTitle = schema.TextLine(title=_(u'Job title'), required=False)
    phone = schema.TextLine(title=_(u'Phone'), required=False)

class IGroup(Interface):
    term = schema.TextLine(title=_(u'Group'), required=False)

class INotes(Interface):
    note = schema.TextLine(title=_(u'Note'), required=False)

## Person details

class INationality(Interface):
    nationality = schema.TextLine(title=_(u'Nationality'), required=False)

class ILanguage(Interface):
    term = schema.TextLine(title=_(u'Language'), required=False)

class IOcupation(Interface):
    term = schema.TextLine(title=_(u'Occupation'), required=False)

class ISchoolStyle(Interface):
    term = schema.TextLine(title=_(u'School/style'), required=False)

class IPlaceOfActivity(Interface):
    place = schema.TextLine(title=_(u'Place'), required=False)
    dateStart = schema.TextLine(title=_(u'Date (start)'), required=False)
    dateEnd = schema.TextLine(title=_(u'Date (end)'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)


