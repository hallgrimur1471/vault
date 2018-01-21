#!/usr/bin/env python3

from urllib.request import urlopen
from urllib.parse import urlencode

def main():
    args = parse_args()

def parse_args():
    parser = argparse.ArgumentParser()
    parser.description = ("Vault")
    parser.add_argument("SEARCH_STRING",
            help="string to search for in vault")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    main()
