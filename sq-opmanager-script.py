#!/usr/bin/env python3
# 
# Python3 script to post Opmanager alerts to Squadcast.
# This script has been tested with Python 3.7.4
#
import sys
import os
import json
import urllib.request

def print_usage():
    """Print the script usage"""
    print("Usage:\n ./sq-opmanager-script.py <url> <alarmid> <message> <displayName> <category> <severity> <ip> <time> <eventType> <entity>")

def form_payload(alarmid = "", message = "",displayName = "",category = "",severity = "",ip ="",time = "",eventType="",entity=""):
    """Forms the python representation of the data payload to be sent from the passed configuration"""

    payload_rep = {"alarmid" : alarmid,"message":message,"displayName":displayName,"category":category,"severity":severity,"ip":ip,"time":time,"eventType":eventType,"entity":entity }

    return payload_rep

def post_to_url(url, payload):
    """Posts the formed payload as json to the passed url"""
    try:
        req = urllib.request.Request(url, data=bytes(json.dumps(payload), "utf-8"))
        req.add_header("Content-Type", "application/json")
        resp = urllib.request.urlopen(req)
        if resp.status > 299:
           print("[sq-opmanager-script] Request failed with status code %s : %s" % (resp.status, resp.read()))
    except urllib.request.URLError as e:
        if e.code >= 400 and e.code < 500:
           print("[sq-opmanager-script] Some error occured while processing the event")

if __name__ == "__main__":


    url =sys.argv[1]
    alarmid = sys.argv[2]
    message = sys.argv[3]
    displayName = sys.argv[4]
    category = sys.argv[5]
    severity = sys.argv[6]
    ip = sys.argv[7]
    time=sys.argv[8]
    eventType=sys.argv[9]
    entity=sys.argv[10]

    print("Sending data to squadcast")
    post_to_url(url, form_payload(alarmid,message,displayName,category,severity,ip,time,eventType,entity))
    print("Done.")
