#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from srun4k import *
import getpass
import requests

if __name__ == '__main__':
    gatewayUrl = "https://gw.buaa.edu.cn"

    username = ""

    ret = do_logout(gatewayUrl, username)
    if ret['success']:
        print('成功！')
    else:
        print('失败！\n' + ret['reason'])
