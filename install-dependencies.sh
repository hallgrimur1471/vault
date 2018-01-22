#!/usr/bin/env bash

set -x # print bash commands
set -e # stop on first error

if [ "$EUID" -eq 0 ];
  then echo "Do not run this script as root"
  exit 1
fi

# install pycryptodome and it's dependencies
sudo apt-get install build-essential libgmp3-dev python3-dev
sudo -H pip3 install pycryptodomex

# test pycryptodome install
python3 -m Cryptodome.SelfTest
