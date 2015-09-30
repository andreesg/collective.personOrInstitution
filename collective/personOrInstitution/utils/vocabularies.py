#!/usr/bin/python
# -*- coding: utf-8 -*-

from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from collective.personOrInstitution import MessageFactory as _
from collective.object.utils.vocabularies import ATVMVocabulary, ObjectVocabulary
# # # # # # # # # # # # # #
# Vocabularies            #
# # # # # # # # # # # # # #

def _createPersonOrInstitutionTypeVocabulary():
    PersonOrInstitution_types = {
        "conservation": _(u"conservation"),
        "restauration": _(u"restauration"),
    }

    for key, name in PersonOrInstitution_types.items():
        term = SimpleTerm(value=key, token=str(key), title=name)
        yield term

def _createInsuranceTypeVocabulary():
    insurance_types = {
        "commercial": _(u"Commercial"),
        "indemnity": _(u"Indemnity"),
    }

    for key, name in insurance_types.items():
        term = SimpleTerm(value=key, token=str(key), title=name)
        yield term

def _createPriorityVocabulary():
    priorities = {
        "low": _(u"low"),
        "medium": _(u"medium"),
        "high": _(u"high"),
        "urgent": _(u"urgent")
    }

    for key, name in priorities.items():
        term = SimpleTerm(value=key, token=str(key), title=name)
        yield term

priority_vocabulary = SimpleVocabulary(list(_createPriorityVocabulary()))
insurance_type_vocabulary = SimpleVocabulary(list(_createInsuranceTypeVocabulary()))
PersonOrInstitutiontype_vocabulary = SimpleVocabulary(list(_createPersonOrInstitutionTypeVocabulary()))

NameTypeVocabularyFactory = ATVMVocabulary('PersonNameType')

PlaceVocabularyFactory = ObjectVocabulary('nameInformation_addressDetails_place')
CountryVocabularyFactory = ObjectVocabulary('nameInformation_addressDetails_country')
GroupVocabularyFactory = ObjectVocabulary('nameInformation_miscellaneous_group')
LanguageVocabularyFactory = ObjectVocabulary('personDetails_nationality_language')
OcupationVocabularyFactory = ObjectVocabulary('personDetails_ocupation_ocupation')
SchoolStyleVocabularyFactory = ObjectVocabulary('personDetails_ocupation_schoolStyle')
