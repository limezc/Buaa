import socket
from srun4k import *
import getpass
import requests


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

if __name__ == '__main__':
    gatewayUrl = "https://gw.buaa.edu.cn"

    username = input("请输入用户名：").strip()
    password = getpass.getpass("请输入密码：").strip()

    ret = do_login(gatewayUrl, username, password)
    if ret['success']:
        print('Success!')
        ip = get_host_ip()
        post_data("raspberry pi", "info", "ip : "+ip+"\n login success")
    else:
        print('error! \n' + ret['reason'])