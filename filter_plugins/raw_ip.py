#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : raw_ip.py
# Author            : Rustam Khafizov <super.rustamm@gmail.com>
# Date              : 26.09.2020
# Last Modified Date: 26.09.2020
# Last Modified By  : Rustam Khafizov <super.rustamm@gmail.com>

import re

def raw_ip(url, key="ip"):
    ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', url)[0]
    port = int(re.findall(r'[0-9]+(?:\.[0-9]+){3}(:[0-9]+)?', url)[0][1:])
    if key == "port":
        return port
    return ip

class FilterModule(object):
    def filters(self):
        return ( { 'raw_ip': raw_ip } )

if __name__ == "__main__":
    import sys
    print(raw_ip(sys.argv[1], sys.argv[2]))
