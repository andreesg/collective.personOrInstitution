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

# # # # # # # # # # # # # # # 
# Dexterity imports         # 
# # # # # # # # # # # # # # # 
from five import grok
from collective import dexteritytextindexer
from plone.dexterity.browser.view import DefaultView
from plone.dexterity.content import Container
from plone.dexterity.browser import add, edit

# # # # # # # # # # # # # # # # # #
# !PersonOrInstitution specific imports!   #
# # # # # # # # # # # # # # # # # #
from collective.personOrInstitution import MessageFactory as _
from .utils.vocabularies import *
from .utils.interfaces import *
from .utils.views import *

# # # # # # # # # # # # #
# # # # # # # # # # # # #
# # PersonOrInstitution schema  # #
# # # # # # # # # # # # #
# # # # # # # # # # # # #

class IPersonOrInstitution(form.Schema):

    text = RichText(
        title=_(u"Body"),
        required=False
    )

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
        required=False
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

    nameInformation_name_nameNotes = schema.TextLine(
        title=_(u'Name notes'),
        required=False
    )
    dexteritytextindexer.searchable('nameInformation_name_nameNotes')

    # Relation with other names
    nameInformation_relationWithOtherNames_use = ListField(title=_(u'Use'),
        value_type=DictRow(title=_(u'Use'), schema=IUse),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_use=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_relationWithOtherNames_use')

    nameInformation_relationWithOtherNames_usedFor = ListField(title=_(u'Used for'),
        value_type=DictRow(title=_(u'Used for'), schema=IUsedFor),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_usedFor=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_relationWithOtherNames_usedFor')

    nameInformation_relationWithOtherNames_equivalent = ListField(title=_(u'Equivalent'),
        value_type=DictRow(title=_(u'Equivalent'), schema=IEquivalent),
        required=False)
    form.widget(nameInformation_relationWithOtherNames_equivalent=DataGridFieldFactory)
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
    nameInformation_contacts = ListField(title=_(u'Website'),
        value_type=DictRow(title=_(u'Website'), schema=IContacts),
        required=False)
    form.widget(nameInformation_contacts=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_contacts')

    # Miscellaneous
    nameInformation_miscellaneous_group = ListField(title=_(u'Group'),
        value_type=DictRow(title=_(u'Group'), schema=IGroup),
        required=False)
    form.widget(nameInformation_miscellaneous_group=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_miscellaneous_group')

    nameInformation_miscellaneous_notes = ListField(title=_(u'Notes'),
        value_type=DictRow(title=_(u'Notes'), schema=INotes),
        required=False)
    form.widget(nameInformation_miscellaneous_notes=DataGridFieldFactory)
    dexteritytextindexer.searchable('nameInformation_miscellaneous_notes')



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
                alsoProvides(widget, IFormWidget)

class AddView(add.DefaultAddView):
    form = AddForm
    

class EditForm(edit.DefaultEditForm):
    template = ViewPageTemplateFile('personOrInstitution_templates/edit.pt')
    
    def update(self):
        super(EditForm, self).update()
        for group in self.groups:
            for widget in group.widgets.values():
                alsoProvides(widget, IFormWidget)

