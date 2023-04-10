# coding=utf-8
from srun4k import *
import sys
import os
import getpass

def print_help():
    print("Usage: \n python login.py [option] [username] [password]")
    print("Options:")
    print("0: login")
    print("1: logout")
    print("2: logout all")
    print("3: check online")


def get_option(option):
    if option in options.keys():
        return option
    elif option in options.values():
        for key, value in options.items():
            if value == option:
                return key
    else:
        return None
    

def get_user_info(option):
    
    username = None
    password = None

    if option != "3":
        if len(sys.argv) == 2:
            if os.path.exists(user_info_file):
                with open(user_info_file, "r") as f:
                    username = f.readline().strip()
                    if option == "0" or option == "2":
                        password = f.readline().strip()
            else:
                username = input("请输入用户名：").strip()
                if option == "0" or option == "2":
                    password = getpass.getpass("请输入密码：").strip()

        elif len(sys.argv) == 3:
            username = sys.argv[2].strip()
            if option == "0" or option == "2":
                password = getpass.getpass("请输入密码：").strip()

        elif len(sys.argv) == 4:
            username = sys.argv[2].strip()
            password = sys.argv[3].strip()
        
        else:
            print_help()
    
    return username, password
    


def run(option, username=None, password=None):
    if option == "0":
        if username is not None and password is not None:
            ret = do_login(gatewayUrl, username, password)
            if ret['success']:
                print('成功！')
            else:
                print('失败！\n' + ret['reason'])
        else:
            print_help()
            return
        

    elif option == "1":
        if username is not None:
            ret = do_logout(gatewayUrl, username)
            if ret['success']:
                print('成功！')
            else:
                print('失败！\n' + ret['reason'])
        else:
            print_help()
            return
        

    elif option == "2":
        if username is not None and password is not None:
            ret = force_logout(gatewayUrl, username, password)
            if ret['success']:
                print('成功！')
            else:
                print('失败！\n' + ret['reason'])
        else:
            print_help()
            return
        

    elif option == "3":
        print(check_online(gatewayUrl))


    else:
        print_help()


def main():
    if len(sys.argv) < 2:
        print_help()
        return

    option = get_option(sys.argv[1])

    if option is None:
        print_help()
        return

    username, password = get_user_info(option)

    run(option, username, password)
    




if __name__ == "__main__":
    gatewayUrl = "https://gw.buaa.edu.cn"
    user_info_file = "user_info.txt"
    options = {"0":"login", "1":"logout", "2":"logout_all", "3":"check_online"}
    main()
