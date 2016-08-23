#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope import schema
from zope.interface import Interface
from collective.personOrInstitution import MessageFactory as _
from ..utils.vocabularies import _createPriorityVocabulary, _createInsuranceTypeVocabulary
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from collective.object.utils.widgets import SimpleRelatedItemsFieldWidget, AjaxSingleSelectFieldWidget
from collective.object.utils.source import ObjPathSourceBinder
from plone.directives import dexterity, form

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
    type = schema.Choice(title=_(u'Name type'), required=True, vocabulary="collective.personOrInstitution.nametype", default="No value",  missing_value=" ")

class IUse(Interface):
    use = RelationList(
        title=_(u'Use'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            vocabulary='collective.object.relateditems'
        ),
        required=False
    )
    form.widget('use', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IUsedFor(Interface):
    usedFor = RelationList(
        title=_(u'Used for'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            vocabulary='collective.object.relateditems'
        ),
        required=False
    )
    form.widget('usedFor', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IEquivalent(Interface):
    name = RelationList(
        title=_(u'Equivalent'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            vocabulary='collective.object.relateditems'
        ),
        required=False
    )
    form.widget('name', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

class IAddressDetails(Interface):
    addressType = schema.TextLine(title=_(u'Address type'), required=False)
    address = schema.TextLine(title=_(u'Address'), required=False)
    postalCode = schema.TextLine(title=_(u'Postal code'), required=False)
    place = schema.List(
        title=_(u'Place'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('place', AjaxSingleSelectFieldWidget, vocabulary="collective.personOrInstitution.place")

    country = schema.List(
        title=_(u'Country'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('country', AjaxSingleSelectFieldWidget, vocabulary="collective.personOrInstitution.country")


class IBiography(Interface):
    biography = schema.Text(title=_(u'Biography'), required=False)

class ITelephone(Interface):
    phone = schema.TextLine(title=_(u'Telephone'), required=False)

class IFax(Interface):
    fax = schema.TextLine(title=_(u'Fax'), required=False)

class IEmail(Interface):
    email = schema.TextLine(title=_(u'Email'), required=False)

class IWebsite(Interface):
    url = schema.TextLine(title=_(u'Website'), required=False)

class IContacts(Interface):
    name = RelationList(
        title=_(u'Name'),
        default=[],
        missing_value=[],
        value_type=RelationChoice(
            title=u"Related",
            vocabulary='collective.object.relateditems'
        ),
        required=False
    )
    form.widget('name', SimpleRelatedItemsFieldWidget, vocabulary='collective.object.relateditems')

    jobTitle = schema.TextLine(title=_(u'Job title'), required=False)
    phone = schema.TextLine(title=_(u'Phone'), required=False)

class IGroup(Interface):
    term = schema.TextLine(title=_(u'Group'), required=False)

class INotes(Interface):
    note = schema.Text(title=_(u'Note'), required=False)

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
    place = schema.List(
        title=_(u'Place'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('place', AjaxSingleSelectFieldWidget, vocabulary="collective.personOrInstitution.place")
    dateStart = schema.TextLine(title=_(u'Start date'), required=False)
    dateEnd = schema.TextLine(title=_(u'End date'), required=False)
    notes = schema.TextLine(title=_(u'Notes'), required=False)


