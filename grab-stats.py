#!/usr/bin/env python
#
# grab-stats.py - quick python log -> graphite tailer

import time
import socket
import re

LOG_FILE = "/var/log/challenge/example.log"
CARBON_SERVER = "127.0.0.1"
CARBON_PORT = 2003
DEBUG = False

def tail(handle):
    handle.seek(0,2)
    while True:
        line = handle.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line

def main():
    con = socket.socket()
    con.connect((CARBON_SERVER, CARBON_PORT))

    file_handle = open(LOG_FILE)
    lines = tail(file_handle)

    for line in lines:
        line = re.sub('[ \t]+',' ',line).strip()
        status_code = line.split(' ')[8]

        if re.match('^1+', str(status_code)) is not None:
            carbon_msg = 'http.status.codes.1xx %s %d\n' % (status_code, int(time.time()))
        elif re.match('^2+', str(status_code)) is not None:
            carbon_msg = 'http.status.codes.2xx %s %d\n' % (status_code, int(time.time()))
        elif re.match('^3+', str(status_code)) is not None:
            carbon_msg = 'http.status.codes.3xx %s %d\n' % (status_code, int(time.time()))
        elif re.match('^4+', str(status_code)) is not None:
            carbon_msg = 'http.status.codes.4xx %s %d\n' % (status_code, int(time.time()))
        elif re.match('^5+', str(status_code)) is not None:
            carbon_msg = 'http.status.codes.5xx %s %d\n' % (status_code, int(time.time()))

        con.sendall(carbon_msg)
        print "%s" % str(carbon_msg) if DEBUG else None



    con.close()

    
if __name__ == '__main__':
    main()
