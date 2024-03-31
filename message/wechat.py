import requests
import os


def send_message(content):
    headers = {"Authorization": os.environ["AUTODL_KEY"]}
    resp = requests.post("https://www.autodl.com/api/v1/wechat/message/send",
                        json={
                            "title": '',
                            "name": content,
                            "content": ''
                        }, headers = headers)
    print(resp.content.decode())