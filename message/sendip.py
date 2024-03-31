import netifaces
import schedule
import time
from wechat import send_message

last_ips = None

def get_all_ips():
    ips = []
    for interface in netifaces.interfaces():
        addr_info = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addr_info:
            for addr in addr_info[netifaces.AF_INET]:
                if addr['addr'].startswith('10.'):
                    ips.append(addr['addr'])
    return sorted(ips)

def check_ip():
    global last_ips
    current_ips = get_all_ips()
    if current_ips != last_ips:
        send_message(str(current_ips))  # 发送通知
        last_ips = current_ips

def daily_notification():
    current_ips = get_all_ips()
    send_message(str(current_ips))  # 发送通知

def main():
    schedule.every(5).minutes.do(check_ip)
    schedule.every(24).hours.do(daily_notification)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()