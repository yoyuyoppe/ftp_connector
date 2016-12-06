import ftplib


class FtpConnector:
    _FTP = ftplib.FTP
    LOGGER_ERROR = ''

    def __init__(self, host, login, passw):
        try:
            FtpConnector._FTP(host, login, passw)
            _pwd = FtpConnector._FTP.pwd()
        except ftplib.all_errors as e:
            FtpConnector.LOGGER_ERROR = "ERROR: %s" % e

    def get_files(self, dir):
        _pwd = FtpConnector._FTP.pwd()
        if _pwd != dir:
            self.set_curr_dir(dir)

        list = FtpConnector._FTP.nlst()
        for f in list:
            print(f)

    def set_curr_dir(self, dir):
        try:
            FtpConnector._FTP.cwd(dir)
        except ftplib.all_errors as e:
            FtpConnector.LOGGER_ERROR = "ERROR: %s" % e