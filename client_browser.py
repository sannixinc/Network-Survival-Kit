#!/usr/bin/python3


# Client Browser - This tool will act as your client browser to pull html from any domain.
# This tool will make use of the urllib module. It will be able to print the url, status code of request, request header info, server info, and the html.

import argparse
import socket
import urllib.request

def client_browser():
    parser = argparse.ArgumentParser (
        prog="Client Browser",
        description="This tool will act as your client browser to pull html from any domain."
    )

    parser.add_argument("domain", help="HTML Domain Information")

    args = parser.parse_args()

    try:
        socket.gethostbyname(args.domain)

    except OSError:
        print("Please check domain name...")

    else:
        url = urllib.request.urlopen( "http://" + args.domain)
        print("Url: \n {}".format( url.geturl()))
        print("Status code: \n {}".format( url.getcode()))
        print("Html: \n {}".format(url.read()))

if __name__ == "__main__":
    client_browser()
