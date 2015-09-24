#!/usr/bin/python
# -*- coding: utf-8 -*-

from plone.indexer.decorator import indexer
from ..personOrInstitution import IPersonOrInstitution

@indexer(IPersonOrInstitution)
def nameInformation_addressDetails_place(object, **kw):
    try:
        if hasattr(object, 'nameInformation_addressDetails'):
            terms = []
            items = object.nameInformation_addressDetails
            if items:
                for item in items:
                    if item['place']:
                        for term in item['place']:
                            if term:
                                terms.append(term)

            return terms
        else:
            return []
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