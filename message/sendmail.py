import os
import yagmail

def send_mail(to_addresses, subject, body, attachments=None):
    username = os.environ["QQ_USER"]
    passwd = os.environ["QQ_PASS"]
    smtp_host = 'smtp.qq.com'
    smtp = yagmail.SMTP(user=username, password=passwd, host=smtp_host)
    smtp.send(to_addresses, subject, body, attachments=attachments)


if __name__ == "__main__":
    to_addresses = ["xxx@gmail.com"]
    subject = "会议通知"
    body = "会议时间：2021-09-01 10:00"
    attachments = ["xxx.pdf"]
    send_mail(to_addresses, subject, body, attachments)



