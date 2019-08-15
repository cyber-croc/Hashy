try:
    import requests
    import sys
    import os
    from huepy import *
except:
    print('''\033[91m
        +-------------------------------------------+
        |          ** Missing Modules **            |
        +-------------------------------------------+
        | requests, sys, os and huepy are required. |
        |   Check if any one of them are missing.   |
        | try --> pip install -r requirements.txt   |
        +-------------------------------------------+
     ''')
    exit()
    
os.system('clear')

print(green('''
 _     _ _______ _______ _     _ __   __
 |_____| |_____| |______ |_____|   \_/
 |     | |     | ______| |     |    |

 '''))

hashvalue = input(info('Enter your hash\n> '))

print()

if len(hashvalue) == 32:
    print(info('Hash Function : MD5'))
    hashtype = "md5"
elif len(hashvalue) == 40:
    print(info('Hash Function : SHA-1'))
    hashtype = "sha1"
elif len(hashvalue) == 64:
    print(info('Hash Function : SHA-256'))
    hashtype = "sha256"
elif len(hashvalue) == 96:
    print(info('Hash Function : SHA-384'))
    hashtype = "sha384"
elif len(hashvalue) == 128:
    print(info('Hash Function : SHA-512'))
    hashtype = "sha512"
else:
    print(bad('Unidentified Hash Function!'))
    exit(1)


def decryptSHA(hashvalue, hashtype):
    r = requests.get(
        'https://md5decrypt.net/Api/api.php?hash=%s&hash_type=%s&email=cybercroc@protonmail.com&code=c5ddc9bbd5b07c45' % (hashvalue, hashtype)).text
    if len(r) != 0:
        print(good('Password is >>> ' + green(r)))
    else:
        print(bad('Hash was not found in the database.'))
        return False


def decryptMD5(hashvalue, hashtype):
    r = requests.get('http://www.nitrxgen.net/md5db/' + hashvalue).text
    if len(r) != 0:
        print(good('Password is >>> ' + green(r)))
    else:
        print(bad('Hash was not found in the database.'))
        return False


if hashtype == "md5":
    decryptMD5(hashvalue, hashtype)
elif hashtype == "sha1":
    decryptSHA(hashvalue, hashtype)
elif hashtype == "sha256":
    decryptSHA(hashvalue, hashtype)
elif hashtype == "sha384":
    decryptSHA(hashvalue, hashtype)
elif hashtype == "sha512":
    decryptSHA(hashvalue, hashtype)
else:
    exit()
