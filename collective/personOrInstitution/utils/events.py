#!/usr/bin/python
# -*- coding: utf-8 -*-
import string
from plone.api import content as c

def move_person(obj):
    base_folder = "/nl/intern/personen-en-instellingen"
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    alphabet = list(string.ascii_uppercase)

    title = getattr(obj, 'title', "")
    if title:
        first_letter = title[0]
        if first_letter.upper() in alphabet:
            source = obj
            folder_path = '%s/%s' %(base_folder, first_letter.upper())
            target = c.get(path=folder_path)
            if source and target:
                c.move(source=source, target=target)

        elif first_letter.upper() in numbers:
            source = obj
            path = '%s/0-9' %(base_folder)
            target = c.get(path=path)
            if source and target:
                c.move(source=source, target=target)
        else:
            source = obj
            path = '%s/meer' %(base_folder)
            target = c.get(path=path)
            if source and target:
                c.move(source=source, target=target)
    else:
        pass

def personModifiedEvent(object, event):
    #move_person(object)
    return True
    


