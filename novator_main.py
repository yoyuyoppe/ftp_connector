import sys
from ftplib import FTP
from Lib import tempfile
from os.path import isfile
from os.path import exists
from os.path import join as joinpath
from os import mkdir
from os import listdir
from os import remove
from src.ftp.ftp_connector import FtpConnector


#temppath = tempfile.gettempdir()+'\orders'
temppath = "E:\\upload\\НоваТор"

# Directory of new orders
DIR_NEW_ORDERS = (temppath+'\orders')
# Directory of new submission
DIR_NEW_ORDRSP = (temppath+'\submission')

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

ftp = FTP("178.74.69.118", "700", "ord-f066da5a-cd0920cf-b11177d0-46f66e92")
print(ftp.pwd())

#ftp = FtpConnector("178.74.69.118", "700", "ord-f066da5a-cd0920cf-b11177d0-46f66e92")
#ftp.get_files('ORDERSACCEPT')


