import argparse
from sys import argv
from ftplib import FTP, all_errors
from Lib import tempfile
from os.path import isfile, exists, join as joinpath
from os import mkdir, listdir, remove, walk



#temppath = tempfile.gettempdir()+'\orders'
temppath = "E:\\upload\\НоваТор"

# Directory of new orders
DIR_NEW_ORDERS = (temppath+'\orders')
# Directory of new submission
DIR_NEW_ORDRSP = (temppath+'\submission')
# Host FTP server
HOST = ''
# Login FTP server
LOGIN = ''
# Password from login
PASSW = ''
# Timeout for connection FTP
TIMEOUT = 0


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server')
    parser.add_argument('-l', '--login')
    parser.add_argument('-p', '--passw')
    parser.add_argument('-t', '--timeout', default=0)

    return parser


def get_orders(ftp):
    _cwd = '/ORDERSLOADED'
    if ftp.pwd() != _cwd:
        ftp.cwd(_cwd)

    #ftp.retrlines('LIST')

    count = 5
    for files in walk(_cwd):
        for file in files:
            full_name = joinpath(_cwd, file)
            # Name files on FTP
            fname = str(file)
            # Create local file
            localfile = open(DIR_NEW_ORDRSP+'\%s' % fname, 'wb')
            # Download and write ftp-file to local file
            ftp.retrbinary('RETR %s' % fname, localfile.write())

            #Close localfile
            localfile.close()
            count -= 1

        if count == 0:
            break


if not exists(DIR_NEW_ORDERS):
    # Create new directory
    mkdir(DIR_NEW_ORDERS)

if not exists(DIR_NEW_ORDRSP):
    # Create new directory
    mkdir(DIR_NEW_ORDRSP)

# Delete the file from the directory DIR_NEW_ORDERS
for i in listdir(DIR_NEW_ORDERS):
    _path = joinpath(DIR_NEW_ORDERS, i)
    if isfile(_path) and '.csv'.lower() in i:
        remove(_path)
    else:
        continue

# Delete the file from the directory DIR_NEW_ORDRSP
for i in listdir(DIR_NEW_ORDRSP):
    _path = joinpath(DIR_NEW_ORDRSP, i)
    if isfile(_path) and '.csv'.lower() in i:
        remove(_path)
    else:
        continue

# ++DEBUG
argv.append('-s 178.74.69.118')
argv.append('-l 700')
argv.append('-p ord-f066da5a-cd0920cf-b11177d0-46f66e92')
# --

parser = createParser()
namespace = parser.parse_args(argv[1:])

HOST = namespace.server
LOGIN = namespace.login
PASSW = namespace.passw
TIMEOUT = int(namespace.timeout)


if not (HOST or LOGIN or PASSW):
    # Write log
    print("Ошибка. Не найдены обязательные параметры запуска (-s, -l, -p)!")
    raise SystemExit

try:
    ftp = FTP(HOST.strip(), LOGIN.strip(), PASSW.strip())
except all_errors as e:
    # Write log
    print('ERROR: %s' % e)
    raise SystemExit

get_orders(ftp)
ftp.close()


