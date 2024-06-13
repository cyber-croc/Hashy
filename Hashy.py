#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import requests
import argparse
from huepy import *

try:
    import os, sys, requests, argparse
    from huepy import *
except ImportError as e:
    print('''\033[91m
        +-----------------------------------------------------+
        |                ** Missing Modules **                |
        +-----------------------------------------------------+
        | requests, sys, os, argparse and huepy are required. |
        |      Check if any one of them are missing.          |
        |    try --> pip install -r requirements.txt          |
        +-----------------------------------------------------+
     ''')
    sys.exit(1)

os.system('cls' if os.name == 'nt' else 'clear')

parser = argparse.ArgumentParser(description='Hash Decryption Script')
parser.add_argument('-p', '--password', help='Hash which needs to be decoded.', dest='passw')
parser.add_argument('--md5', help='Decode as MD5 hash.', action='store_true')
parser.add_argument('--sha1', help='Decode as SHA-1 hash.', action='store_true')
parser.add_argument('--sha256', help='Decode as SHA-256 hash.', action='store_true')
parser.add_argument('--sha384', help='Decode as SHA-384 hash.', action='store_true')
parser.add_argument('--sha512', help='Decode as SHA-512 hash.', action='store_true')
args = parser.parse_args()

print(green(''' 
 _     _ _______ _______ _     _ __   __
 |_____| |_____| |______ |_____|   \_/  
 |     | |     | ______| |     |    |    \n'''))

if not len(sys.argv) > 1:
    hashvalue = input(info("Enter your hash.\n> "))
else:
    hashvalue = args.passw

if args.md5:
    print(info('Hash Function : MD5'))
    hashtype = 'md5'
elif args.sha1:
    print(info('Hash Function : SHA-1'))
    hashtype = 'sha1'
elif args.sha256:
    print(info('Hash Function : SHA-256'))
    hashtype = 'sha256'
elif args.sha384:
    print(info('Hash Function : SHA-384'))
    hashtype = 'sha384'
elif args.sha512:
    print(info('Hash Function : SHA-512'))
    hashtype = 'sha512'
else:

    if len(hashvalue) == 32:
        print(info('Hash Function : MD5'))
        hashtype = 'md5'
    elif len(hashvalue) == 40:
        print(info('Hash Function : SHA-1'))
        hashtype = 'sha1'
    elif len(hashvalue) == 64:
        print(info('Hash Function : SHA-256'))
        hashtype = 'sha256'
    elif len(hashvalue) == 96:
        print(info('Hash Function : SHA-384'))
        hashtype = 'sha384'
    elif len(hashvalue) == 128:
        print(info('Hash Function : SHA-512'))
        hashtype = 'sha512'
    else:
        print(bad('Unidentified Hash Function!'))
        exit(1)

def md5crack(hashvalue):
    try:
        r = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
        print(good('Password is >>> ' + green(r)))
    except requests.exceptions.RequestException as e:
        print(bad('Error during request: ' + str(e)))
        return False

def decrypter(hashvalue, hashtype):
    try:
        r = requests.get(
            'https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=cybercroc@protonmail.com&code=c5ddc9bbd5b07c45' % (hashvalue, hashtype)).text
        if len(r) != 0:
            print(good('Password is >>> ' + green(r)))
        else:
            print(bad('Hash was not found in the database.'))
            return False
    except requests.exceptions.RequestException as e:
        print(bad('Error during request: ' + str(e)))
        return False

if hashtype in ['sha1', 'sha256', 'sha384', 'sha512']:
    decrypter(hashvalue, hashtype)
elif hashtype == 'md5':
    md5crack(hashvalue)
else:
    exit()
