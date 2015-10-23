#!/usr/bin/python
# -*- coding: utf-8 -*-

#
# Zope dependencies
#
from zope import schema
from zope.interface import invariant, Invalid, Interface, implements
from zope.interface import alsoProvides
from zope.schema.vocabulary import SimpleVocabulary
from zope.schema.fieldproperty import FieldProperty
from zope.component import getMultiAdapter

#
# Plone dependencies
#
from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.interfaces import IImageScaleTraversable
from plone.supermodel import model
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

#
# z3c.forms dependencies
#
from z3c.form import group, field
from z3c.form.form import extends
from z3c.form.browser.textlines import TextLinesFieldWidget

#
# DataGridFields dependencies
#
from collective.z3cform.datagridfield import DataGridFieldFactory, DictRow
from collective.z3cform.datagridfield.blockdatagridfield import BlockDataGridFieldFactory
from collective.z3cform.datagridfield.interfaces import IDataGridField

# # # # # # # # # # # # # # # 
# Dexterity imports         # 
# # # # # # # # # # # # # # # 
from five import grok
from collective import dexteritytextindexer
from plone.dexterity.browser.view import DefaultView
from plone.dexterity.content import Container
from plone.dexterity.browser import add, edit
from plone.app.widgets.dx import AjaxSelectFieldWidget

# # # # # # # # # # # # # # # # # #
# !PersonOrInstitution specific imports!   #
# # # # # # # # # # # # # # # # # #
from collective.personOrInstitution import MessageFactory as _
from .utils.vocabularies import *
from .utils.interfaces import *
from .utils.views import *

from z3c.relationfield.schema import RelationChoice
from z3c.relationfield.schema import RelationList
from collective.object.utils.widgets import SimpleRelatedItemsFieldWidget, AjaxSingleSelectFieldWidget
from collective.object.utils.source import ObjPathSourceBinder
from plone.directives import dexterity, form


# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # PersonOrInstitution schema  # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #

from plone.app.content.interfaces import INameFromTitle
class INameFromPersonNames(INameFromTitle):
    def title():
        """Return a processed title"""

class NameFromPersonNames(object):
    implements(INameFromPersonNames)
    
    def __init__(self, context):
        self.context = context

    @property
    def title(self):
        self.context.setTitle(self.context.nameInformation_name_name)
        return self.context.nameInformation_name_name

class IPersonOrInstitution(form.Schema):

    text = RichText(
        title=_(u"Body"),
        required=False
    )

    # priref
    priref = schema.TextLine(
        title=_(u'priref'),
        required=False
    )
    dexteritytextindexer.searchable('priref')


    # # # # # # # # # # # #
    # Name Information    #
    # # # # # # # # # # # #
    model.fieldset('name_information', label=_(u'Name information'), 
        fields=['nameInformation_name_name', 'nameInformation_name_institutionNumber',
                'nameInformation_name_nameType', 'nameInformation_name_nameNotes',
                'nameInformation_relationWithOtherNames_use', 'nameInformation_relationWithOtherNames_usedFor',
                'nameInformation_relationWithOtherNames_equivalent', 'nameInformation_addressDetails',
                'nameInformation_telephoneFaxEmail_telephone', 'nameInformation_telephoneFaxEmail_fax',
                'nameInformation_telephoneFaxEmail_email', 'nameInformation_telephoneFaxEmail_website',
                'nameInformation_contacts', 'nameInformation_miscellaneous_group', 'nameInformation_miscellaneous_notes']
    )

    nameInformation_name_name = schema.TextLine(
        title=_(u'Name'),
        required=True
    )
    dexteritytextindexer.searchable('nameInformation_name_name')

    nameInformation_name_institutionNumber = schema.TextLine(
        title=_(u'Institution number'),
        required=False
    )
    dexteritytextindexer.searchable('nameInformation_name_institutionNumber')

    nameInformation_name_nameType = ListField(title=_(u'Name type'),
        value_type=DictRow(title=_(u'Name type'), schema=INameType),
        required=False)
    form.widget(nameInformation_name_nameType=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_name_nameType')

    nameInformation_name_nameNotes = schema.Text(
        title=_(u'Name notes'),
        required=False
    )
    dexteritytextindexer.searchable('nameInformation_name_nameNotes')

    # Relation with other names
    nameInformation_relationWithOtherNames_use = ListField(title=_(u'Use'),
        value_type=DictRow(title=_(u'Use'), schema=IUse),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_use=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_relationWithOtherNames_use')

    nameInformation_relationWithOtherNames_usedFor = ListField(title=_(u'Used for'),
        value_type=DictRow(title=_(u'Used for'), schema=IUsedFor),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_usedFor=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_relationWithOtherNames_usedFor')

    nameInformation_relationWithOtherNames_equivalent = ListField(title=_(u'Equivalent'),
        value_type=DictRow(title=_(u'Equivalent'), schema=IEquivalent),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_equivalent=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_relationWithOtherNames_equivalent')

    # Address details
    nameInformation_addressDetails = ListField(title=_(u'Address details'),
        value_type=DictRow(title=_(u'Address details'), schema=IAddressDetails),
        required=False)
    form.widget(nameInformation_addressDetails=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_addressDetails')


    # Telephone/fax/email
    nameInformation_telephoneFaxEmail_telephone = ListField(title=_(u'Telephone'),
        value_type=DictRow(title=_(u'Telephone'), schema=ITelephone),
        required=False)
    form.widget(nameInformation_telephoneFaxEmail_telephone=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_telephoneFaxEmail_telephone')

    nameInformation_telephoneFaxEmail_fax = ListField(title=_(u'Fax'),
        value_type=DictRow(title=_(u'Fax'), schema=IFax),
        required=False)
    form.widget(nameInformation_telephoneFaxEmail_fax=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_telephoneFaxEmail_fax')

    nameInformation_telephoneFaxEmail_email = ListField(title=_(u'Email'),
        value_type=DictRow(title=_(u'Email'), schema=IEmail),
        required=False)
    form.widget(nameInformation_telephoneFaxEmail_email=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_telephoneFaxEmail_email')

    nameInformation_telephoneFaxEmail_website = ListField(title=_(u'Website'),
        value_type=DictRow(title=_(u'Website'), schema=IWebsite),
        required=False)
    form.widget(nameInformation_telephoneFaxEmail_website=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_telephoneFaxEmail_website')

    # Contacts
    nameInformation_contacts = ListField(title=_(u'Contacts'),
        value_type=DictRow(title=_(u'Contacts'), schema=IContacts),
        required=False)
    form.widget(nameInformation_contacts=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_contacts')

    # Miscellaneous
    nameInformation_miscellaneous_group = schema.List(
        title=_(u'Group'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('nameInformation_miscellaneous_group', AjaxSelectFieldWidget, vocabulary="collective.personOrInstitution.group")

    nameInformation_miscellaneous_notes = ListField(title=_(u'Notes'),
        value_type=DictRow(title=_(u'Notes'), schema=INotes),
        required=False)
    form.widget(nameInformation_miscellaneous_notes=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_miscellaneous_notes')

    # # # # # # # # # # # #
    # Person details      #
    # # # # # # # # # # # #
    model.fieldset('person_details', label=_(u'Person details'), 
        fields=['personDetails_birthDetails_dateStart' , 'personDetails_birthDetails_dateEnd',
                'personDetails_birthDetails_precision', 'personDetails_birthDetails_place', 
                'personDetails_birthDetails_notes', 'personDetails_deathDetails_dateStart',
                'personDetails_deathDetails_dateEnd', 'personDetails_deathDetails_precision',
                'personDetails_deathDetails_place', 'personDetails_deathDetails_notes',
                'personDetails_nationality_nationality', 'personDetails_nationality_language',
                'personDetails_ocupation_ocupation', 'personDetails_ocupation_schoolStyle',
                'personDetails_placeOfActivity', 'personDetails_biographies']
    )

    # Birth details
    personDetails_birthDetails_dateStart = schema.TextLine(
        title=_(u'Date (start)'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_birthDetails_dateStart')

    personDetails_birthDetails_dateEnd = schema.TextLine(
        title=_(u'Date (end)'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_birthDetails_dateEnd')

    personDetails_birthDetails_precision = schema.TextLine(
        title=_(u'Precision'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_birthDetails_precision')


    personDetails_birthDetails_place = schema.List(
        title=_(u'Place'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('personDetails_birthDetails_place', AjaxSingleSelectFieldWidget, vocabulary="collective.personOrInstitution.place")

    personDetails_birthDetails_notes = ListField(title=_(u'Notes'),
        value_type=DictRow(title=_(u'Notes'), schema=INotes),
        required=False)
    form.widget(personDetails_birthDetails_notes=DataGridFieldFactory)
    dexteritytextindexer.searchable('personDetails_birthDetails_notes')

    # Death details
    personDetails_deathDetails_dateStart = schema.TextLine(
        title=_(u'Date (start)'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_birthDetails_dateStart')

    personDetails_deathDetails_dateEnd = schema.TextLine(
        title=_(u'Date (end)'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_birthDetails_dateEnd')

    personDetails_deathDetails_precision = schema.TextLine(
        title=_(u'Precision'),
        required=False
    )
    dexteritytextindexer.searchable('personDetails_deathDetails_precision')

    personDetails_deathDetails_place = schema.List(
        title=_(u'Place'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('personDetails_deathDetails_place', AjaxSingleSelectFieldWidget, vocabulary="collective.personOrInstitution.place")

    personDetails_deathDetails_notes = ListField(title=_(u'Notes'),
        value_type=DictRow(title=_(u'Notes'), schema=INotes),
        required=False)
    form.widget(personDetails_deathDetails_notes=DataGridFieldFactory)
    dexteritytextindexer.searchable('personDetails_deathDetails_notes')

    # Nationality
    personDetails_nationality_nationality = ListField(title=_(u'Nationality'),
        value_type=DictRow(title=_(u'Nationality'), schema=INationality),
        required=False)
    form.widget(personDetails_nationality_nationality=DataGridFieldFactory)
    dexteritytextindexer.searchable('personDetails_nationality_nationality')

    personDetails_nationality_language = schema.List(
        title=_(u'Language'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('personDetails_nationality_language', AjaxSelectFieldWidget, vocabulary="collective.personOrInstitution.language")

    # Ocupation
    personDetails_ocupation_ocupation = schema.List(
        title=_(u'Occupation'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('personDetails_ocupation_ocupation', AjaxSelectFieldWidget, vocabulary="collective.personOrInstitution.ocupation")

    personDetails_ocupation_schoolStyle = schema.List(
        title=_(u'School/style'),
        required=False,
        value_type=schema.TextLine(),
        missing_value=[],
        default=[]
    )
    form.widget('personDetails_ocupation_schoolStyle', AjaxSelectFieldWidget, vocabulary="collective.personOrInstitution.schoolStyle")

    # Place of activity
    personDetails_placeOfActivity = ListField(title=_(u'Place of activity'),
        value_type=DictRow(title=_(u'Place of activity'), schema=IPlaceOfActivity),
        required=False)
    form.widget(personDetails_placeOfActivity=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('personDetails_placeOfActivity')

    # Biography
    personDetails_biographies = ListField(title=_(u'Biography'),
        value_type=DictRow(title=_(u'Biography'), schema=IBiography),
        required=False)
    form.widget(personDetails_biographies=BlockDataGridFieldFactory)
    dexteritytextindexer.searchable('personDetails_biographies')



# # # # # # # # # # # # # # # # # # # # #
# PersonOrInstitution declaration       #
# # # # # # # # # # # # # # # # # # # # #

class PersonOrInstitution(Container):
    grok.implements(IPersonOrInstitution)
    pass

# # # # # # # # # # # # # # # # # # # # # # #
# PersonOrInstitution add/edit views        # 
# # # # # # # # # # # # # # # # # # # # # # #

class AddForm(add.DefaultAddForm):
    template = ViewPageTemplateFile('personOrInstitution_templates/add.pt')
    def update(self):
        super(AddForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                if IDataGridField.providedBy(widget):
                    widget.auto_append = False
                    widget.allow_reorder = True
                alsoProvides(widget, IFormWidget)

class AddView(add.DefaultAddView):
    form = AddForm
    

class EditForm(edit.DefaultEditForm):
    template = ViewPageTemplateFile('personOrInstitution_templates/edit.pt')
    
    def update(self):
        super(EditForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                if IDataGridField.providedBy(widget):
                    widget.auto_append = False
                    widget.allow_reorder = True
                alsoProvides(widget, IFormWidget)

