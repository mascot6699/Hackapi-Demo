#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import requests
from django.conf import settings
import wikipedia
from PyDictionary import PyDictionary

sid = settings.EXOTEL_SID
token = settings.EXOTEL_TOKEN


def send_message(sid, token, sms_from, sms_to, sms_body):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Sms/send.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': sms_from,
            'To': sms_to,
            'Body': sms_body
        })

if __name__ == '__main__':

    r = send_message(sid, token,
        sms_from='8050248326',  # sms_from='8808891988',
        sms_to='8050248326', # sms_to='9052161119',
        sms_body='Some message is sent')
    print r.status_code
    pprint(r.json())


def process_wiki(word):
    return wikipedia.summary(word)

def process_dictionary(word):
    return wikipedia.summary(word)