#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
from srun4k import *
import getpass
import requests
import time


def post_data(title, name, content):
    requests.post(
        "https://www.autodl.com/api/v1/wechat/message/push",
        json={
                "token": "",
                "title": title,
                "name": name,
                "content": content
            }
    )

def isNetOK(testserver):
    s=socket.socket()
    s.settimeout(3)
    try:
        status = s.connect_ex(testserver)
        if status == 0:
            s.close()
            return True
        else:
            return False
    except Exception as e:
        return False

def isNetChainOK(testserver=('www.baidu.com',443)):
    isOK = isNetOK(testserver)
    return isOK


def isNetUSAOK(testserver=('www.google.com',443)):
    isOK = isNetOK(testserver)
    return isOK

def isNetYouTubeOK(testserver=('www.youtube.com',443)):
    isOK = isNetOK(testserver)
    return isOK



def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    except:
        pass
    finally:
        s.close()
    return ip


def main():
    gatewayUrl = "https://gw.buaa.edu.cn"

    username = ""
    password = ""

    reconnect_times = 0
    reconnect_times_threshold = 10

    while 1:
        if isNetChainOK():
            time.sleep(300)
            continue
        ret = do_login(gatewayUrl, username, password)
        if ret['success']:
            print('Success!')
            ip = get_host_ip()
            post_data("raspberry pi", "info", "ip : "+ip)
        else:
            reconnect_times += 1
            print('error! \n' + ret['reason'])
            
        time.sleep(60)

        if reconnect_times > reconnect_times_threshold:
            time.sleep(600000000)


if __name__ == '__main__':
    main()
