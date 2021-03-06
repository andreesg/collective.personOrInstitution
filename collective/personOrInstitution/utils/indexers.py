#!/usr/bin/python
# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from ..personOrInstitution import IPersonOrInstitution

@indexer(IPersonOrInstitution)
def nameInformation_addressDetails_place(object, **kw):
    try:
        terms = []
        if hasattr(object, 'nameInformation_addressDetails'): 
            items = object.nameInformation_addressDetails
            if items:
                for item in items:
                    if item['place']:
                        for term in item['place']:
                            if term:
                                terms.append(term)

        if hasattr(object, 'personDetails_birthDetails_place'):
            items = object.personDetails_birthDetails_place
            if items:
                for item in items:
                    terms.append(item)

        if hasattr(object, 'personDetails_deathDetails_place'):
            items = object.personDetails_deathDetails_place
            if items:
                for item in items:
                    terms.append(item)
        
        if hasattr(object, 'personDetails_placeOfActivity'): 
            items = object.personDetails_placeOfActivity
            if items:
                for item in items:
                    if item['place']:
                        for term in item['place']:
                            if term:
                                terms.append(term)
        return terms
    except:
        return []

@indexer(IPersonOrInstitution)
def nameInformation_addressDetails_country(object, **kw):
    try:
        if hasattr(object, 'nameInformation_addressDetails'):
            terms = []
            items = object.nameInformation_addressDetails
            if items:
                for item in items:
                    if item['country']:
                        for term in item['country']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
    except:
        return []

@indexer(IPersonOrInstitution)
def nameInformation_name_nameType_type(object, **kw):
    try:
        if hasattr(object, 'nameInformation_name_nameType'):
            terms = []
            items = object.nameInformation_name_nameType
            if items:
                for item in items:
                    if item['type']:
                        terms.append(item['type'])

            return terms
        else:
            return []
    except:
        return []


