#!/usr/bin/env python3

import argparse
from urllib.request import urlopen
from urllib.parse import urlencode, urlunparse, ParseResult

def main():
    args = parse_args()
    if args.server_address:
        search_in_vault(args.SEARCH_STRING, args.server_address)
    else:
        search_in_vault(args.SEARCH_STRING)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.description = ("Vault containing commands notes")
    parser.add_argument("SEARCH_STRING",
                        help="string to search for in vault")
    parser.add_argument("-s", "--server-address",
                        help=("use custom server address:port instead of the "
                              "default. -s www.example.com:port"))
    args = parser.parse_args()
    return args

def search_in_vault(search_string, server_address="localhost:1471"):
    parse_result = ParseResult(scheme="http", netloc=server_address, params='',
                               path='/get',
                               query="search={}".format(search_string),
                               fragment='')
    url = urlunparse(parse_result)
    result = urlopen(url)
    print(result.read().decode().rstrip())

if __name__ == "__main__":
    main()
