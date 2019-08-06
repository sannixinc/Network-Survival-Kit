#!/usr/bin/python3

# IP Mapping - This tool will return the corresponding IP address of any domain entered.
# This tool will make use of the socket module. It will take stdin from the user and return the IP address in the format of: "The IP address of target is: 58.65.22.14"

import argparse
import socket


def ip_mapping():
    parser = argparse.ArgumentParser (
        prog="IP Mapping",
        description="This tool will return the corresponding IP address of any domain entered."
    )

    parser.add_argument("domain", help="IP Hostname")

    args = parser.parse_args()

    try:
        socket.gethostbyname(args.domain)

    except OSError:
        print("Domain name Invalid")

    else:
        print("Requested IP Address: {}".format(socket.gethostbyname(args.domain)))

if __name__ == "__main__":
    ip_mapping()
