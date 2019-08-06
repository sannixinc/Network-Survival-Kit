#!/usr/bin/python3

# Mac Address Lookup - This tool will return information on mac addresses.
# This tool will use the urllib2, json, and codecs modules.
# This tool will make an api call with mac address to http://macvendors.co/api
# It will take stdin from user, and will return a report in format of: "Company Name, Address".

import argparse
import codecs
import json
import urllib.request



parser = argparse.ArgumentParser (
    prog="Mac Address Lookup",
    description="This tool will return information on Mac Addresses."
)

parser.add_argument("mac", help="Mac Address")

args = parser.parse_args()

webUrL = urllib.request.urlopen("http://macvendors.co/api/" + args.mac)
json_dict = json.load(webUrL)

print(json_dict["result"]["Corporation"] + ", " + json_dict["result"]["Address"])