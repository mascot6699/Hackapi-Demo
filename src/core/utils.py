#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pprint import pprint
import requests
from django.conf import settings
from PyDictionary import PyDictionary
import wikipedia
import sendgrid

sid = settings.EXOTEL_SID
token = settings.EXOTEL_TOKEN
api = settings.SENDGRID_API_TOKEN


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
    meaning = "You searched for the word {}.  "
    dictionary = PyDictionary(word)
    our_meaning = dictionary.getMeanings()
    meaning = meaning.format(our_meaning.keys()[0])
    l = zip(our_meaning.values()[0].keys(),our_meaning.values()[0].values()[0])
    for idx in l:
        meaning += idx[0] + ":" + idx[1] + ", "
    return meaning[:-1]

def custom_send_email(msg):
    msg = msg.split(' ')
    from_email = msg[0]
    to_email = msg[1]
    body = " ".join(msg[2:])
    sg = sendgrid.SendGridClient(api)
    message = sendgrid.Mail(to=to_email, subject="Urgent Emails", text=body, from_email=from_email)
    status, msg = sg.send(message)
    print "status", status
    print "msg" ,msg
    if status==200:
        return "Email has been sent!"
    else:
        return "Email sending is delayed we are on it!"

    return " "


def connect_customer(sid, token, customer_no, exotel_no, callerid, url, timelimit=None, timeout=None, calltype="trans",
                     callback_url=None):
    return requests.post('https://twilix.exotel.in/v1/Accounts/{sid}/Calls/connect.json'.format(sid=sid),
        auth=(sid, token),
        data={
            'From': customer_no,
            'To': exotel_no,
            'CallerId': callerid,
            'Url': url,
            'TimeLimit': timelimit,
            'TimeOut': timeout,
            'CallType': calltype,
            'StatusCallback': callback_url
        })


if __name__ == '__main__':
    r = connect_customer(
        sid, token,
        customer_no="<Your-Customer's-Number>",
        exotel_no="<Your-Exotel-Landline-or-Mobile>",
        callerid="<Your-Exotel-virtual-number>",
        url="http://my.exotel.in/exoml/start/<flow_id>",
        timelimit="<time-in-seconds>",  # This is optional
        timeout="<time-in-seconds>",  # This is also optional
        calltype="trans",  # Can be "trans" for transactional and "promo" for promotional content
        callback_url="<http//: your company URL>"  # This is also also optional
        )
    print r.status_code
    pprint(r.json())

def get_help():
    message = "8050248326 email from_email to_email body \n" \
              "8050248326 dictionary term_to_search \n" \
              "8050248326 wiki thing_to_search_in_wiki \n" \
              "8050248326 song requested_song \n"
    print message
    return message