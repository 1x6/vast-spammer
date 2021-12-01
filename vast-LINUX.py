#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import os, json, subprocess, sys
if sys.version_info < (3, 7):
    print('Please upgrade your Python version to 3.9.0-3.9.8')
    print(sys.version_info)
    input()
    sys.exit()
if sys.version_info > (3, 10):
    print('Please downgrade your Python version to 3.9.0-3.9.8')
    print(sys.version_info)
    input()
    sys.exit()
from os import system
if os.name == "nt":
    from win10toast import ToastNotifier
elif os.name == "posix":
    pass
else:
    print("the fuck kind of operating system do you use")
    input()
try:
    import base64
except:
    system("pip install base64")
try:
    from random import random
except:
    system("pip install random")
try:
    from pymongo import MongoClient
except:
    system("pip install pymongo")
try:
    import fade
except:
    system("pip install fade")
try:
    from colorama import *
except:
    system("pip install colorama")
try:
    import datetime
except:
    system("pip install datetime")
try:
    from time import sleep
except:
    system("pip install time")
try:
    import ctypes
except:
    system("pip install ctypes")
try:
    import requests
except:
    system("pip install requests")
try:
    import threading
except:
    system("pip install threading")
try:
    from urllib.request import Request, urlopen
except:
    system("pip install urllib3")
try:
    import re
except:
    system("pip install re")
try:
    if os.name == "nt":
        import webbrowser
    if os.name == "posix":
        pass
except:
    pass
import base64
from random import random
from pymongo import MongoClient
import subprocess
if os.name == "nt":
    from win10toast import ToastNotifier
elif os.name == "posix":
    pass
else:
    print("the fuck kind of operating system do you use")
import fade
from colorama import *
import datetime
import os
from time import sleep
import sys
import time
import json
import ctypes
import requests
import threading
from urllib.request import Request, urlopen
import re
import webbrowser
if os.name == "nt":
    toast_noti = ToastNotifier()


Groups = []


try:
    lines_seen = set()
    with open("data/groups/groups.txt", "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if i not in lines_seen:
                f.write(i)
                lines_seen.add(i)
        f.truncate()
except:
    pass

def decode(string1, string2, string3, string4):
    entire_string = str(string1+string2+string3+string4)
    base64_bytes = entire_string.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')



try:
    Mongo = MongoClient("mongodb+srv://vast:vast123@vast.qqo4j.mongodb.net/test?ssl=true&ssl_cert_reqs=CERT_NONE")
    mydb=Mongo["Users"]
    db = mydb["Whitelisted"]
except Exception as e:
    print(e)
    sys.exit()

menu = """                      
                                     :::     :::     :::      ::::::::  ::::::::::: 
                                     :+:     :+:   :+: :+:   :+:    :+:     :+:     
                                     +:+     +:+  +:+   +:+  +:+            +:+     
                                     +#+     +:+ +#++:++#++: +#++:++#++     +#+     
                                      +#+   +#+  +#+     +#+        +#+     +#+     
                                       #+#+#+#   #+#     #+# #+#    #+#     #+#     
                                         ###     ###     ###  ########      ### 
                                      

                           +══════════════════════════════╦════════════════════════════════+
                           |      [1] Group Creator       |      [6] Mass PFP Change       |
                           |      [2] Add/Remove People   |      [7] Group Count           |
                           |      [3] Change Token        |      [8] Change Colors         |
                           |      [4] Transfer Groups     |      [9] Call Crasher          |
                           |      [5] Name Changer        |      [10] Multi-Group Creator  | 
                           +══════════════════════════════╧════════════════════════════════+     


"""

colours = """                      
                                     :::     :::     :::      ::::::::  ::::::::::: 
                                     :+:     :+:   :+: :+:   :+:    :+:     :+:     
                                     +:+     +:+  +:+   +:+  +:+            +:+     
                                     +#+     +:+ +#++:++#++: +#++:++#++     +#+     
                                      +#+   +#+  +#+     +#+        +#+     +#+     
                                       #+#+#+#   #+#     #+# #+#    #+#     #+#     
                                         ###     ###     ###  ########      ### 
                                      

                           +══════════════════════════════╦════════════════════════════════+
                           |      [1] Black & White       |      [5] Pink & Red            |
                           |      [2] Purple & Pink       |      [6] Purple & Blue         |
                           |      [3] Green & Blue        |      [7] Brazil                |
                           |      [4] Water               |      [8] Random                |
                           +══════════════════════════════╧════════════════════════════════+     


"""

text = """

   :::     :::     :::      ::::::::  ::::::::::: 
   :+:     :+:   :+: :+:   :+:    :+:     :+:     
   +:+     +:+  +:+   +:+  +:+            +:+     
   +#+     +:+ +#++:++#++: +#++:++#++     +#+     
    +#+   +#+  +#+     +#+        +#+     +#+     
     #+#+#+#   #+#     #+# #+#    #+#     #+#     
       ###     ###     ###  ########      ###                                               

"""

default_text = fade.greenblue(text)






class Authentication:

    def get_uuid():
        if os.name == "nt":
            cmd = 'wmic csproduct get uuid'
            uuid = str(subprocess.check_output(cmd))
            pos1 = uuid.find("\\n")+2
            uuid = uuid[pos1:-15]
            return uuid.rstrip()
        elif os.name == "posix":
            cmd = 'sudo dmidecode -s system-uuid' #make this run and do output on linux :crylaugh:

            
    
    def check_whitelist():
        check = db.count_documents({"uuid": Authentication.get_uuid()})
        if check >= 1:
            return True
        else:
            return False
    

    def get_user(key:str):
        does_user_exist = Authentication.check_whitelist()
        if does_user_exist:
            user = {"uuid": Authentication.get_uuid()}
            try:
                return db.find_one(user)[key]
            except: 
                pass
        else:
            return False



def license_config(key):
    try:
        with open("data/config/license.json") as f:
            li_conf = json.load(f)
        return li_conf.get(key)
    except:
        pass


def config(key):
    try:
        with open("data/config/config.json") as f:
            li_conf = json.load(f)
        return li_conf.get(key)
    except:
        pass


def update_title(title, token=None):
    if token == None:
        try:
            if os.name == "nt":
                ctypes.windll.kernel32.SetConsoleTitleW(f"{title}")
            if os.name == "posix":
                print(f'\33]0;{title}\a', end='', flush=True)
        except:
            pass
    else:
        h = {'Authorization': token, 'Content-Type': 'application/json'} 
        r = requests.get(f'https://discord.com/api/v9/users/@me', headers=h)
        if r.status_code == 200:
            username = r.json()['username']+'#'+r.json()['discriminator']
            try:
                if os.name == "nt":
                    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}  •  Logged in as {username}")
                if os.name == "posix":
                    print(f'\33]0;{title}  •  Logged in as {username}\a', end='', flush=True)
            except:
                pass
        else:
            try:
                if os.name == "nt":
                    ctypes.windll.kernel32.SetConsoleTitleW(f"{title}  •  Logged in as INVALID TOKEN")
                if os.name == "posix":
                    print(f'\33]0;{title}  •  Logged in as INVALID TOKEN\a', end='', flush=True)
            except:
                pass


def percentage(part, whole):
    percentage = 100 * float(part)/float(whole)
    return str(percentage)[:-13]

def print_menu():
    if config("menu") == "blackwhite": print(fade.blackwhite(menu))
    if config("menu") == "purplepink": print(fade.purplepink(menu))
    if config("menu") == "greenblue": print(fade.greenblue(menu))
    if config("menu") == "water": print(fade.water(menu))
    if config("menu") == "pinkred": print(fade.pinkred(menu))
    if config("menu") == "purpleblue": print(fade.purpleblue(menu))
    if config("menu") == "brazil": print(fade.brazil(menu))
    if config("menu") == "random": print(fade.random(menu))




def print_text():
    if config("menu") == "blackwhite": print(fade.blackwhite(text))
    if config("menu") == "purplepink": print(fade.purplepink(text))
    if config("menu") == "greenblue": print(fade.greenblue(text))
    if config("menu") == "water": print(fade.water(text))
    if config("menu") == "pinkred": print(fade.pinkred(text))
    if config("menu") == "purpleblue": print(fade.purpleblue(text))
    if config("menu") == "brazil": print(fade.brazil(text))
    if config("menu") == "random": print(fade.random(text))


def print_colours():
    if config("menu") == "blackwhite": print(fade.blackwhite(colours))
    if config("menu") == "purplepink": print(fade.purplepink(colours))
    if config("menu") == "greenblue": print(fade.greenblue(colours))
    if config("menu") == "water": print(fade.water(colours))
    if config("menu") == "pinkred": print(fade.pinkred(colours))
    if config("menu") == "purpleblue": print(fade.purpleblue(colours))
    if config("menu") == "brazil": print(fade.brazil(colours))
    if config("menu") == "random": print(fade.random(colours))

def trigger_notification(title, description):
    try:
        toast_noti.show_toast(f'{title}', description, icon_path="data/images/logo.ico", duration=6, threaded=True)
    except:
        pass


def get_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M")
    return current_time


def clear():
  if os.name != 'nt':
    os.system('clear')
  else:
    os.system('cls')



def print_with_ends(content):
    colour = config("menu")

    if colour == "blackwhite":
        print(f"  {Fore.LIGHTWHITE_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTWHITE_EX}=>{Fore.WHITE} {content}",end='')

    elif colour == "purplepink":
        print(f"  {Fore.LIGHTMAGENTA_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTMAGENTA_EX}=>{Fore.WHITE} {content}",end='')
    
    elif colour == "greenblue":
        print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTCYAN_EX}=>{Fore.WHITE} {content}",end='')

    elif colour == "water":
        print(f"  {Fore.LIGHTBLUE_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTBLUE_EX}=>{Fore.WHITE} {content}",end='')
    
    elif colour == "pinkred":
        print(f"  {Fore.LIGHTRED_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTRED_EX}=>{Fore.WHITE} {content}",end='')

    elif colour == "purpleblue":
        print(f"  {Fore.LIGHTBLUE_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTBLUE_EX}=>{Fore.WHITE} {content}",end='')
    
    elif colour == "brazil":
        print(f"  {Fore.LIGHTGREEN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTGREEN_EX}=>{Fore.WHITE} {content}",end='')

    elif colour == "random":
        print(f"  {Fore.LIGHTWHITE_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTWHITE_EX}=>{Fore.WHITE} {content}",end='')
    
    else:
        print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTCYAN_EX}=>{Fore.WHITE} {content}",end='')



def print_module(name):
    colour = config("menu")

    if colour == "blackwhite":
        print(f"  {Fore.LIGHTWHITE_EX} {name}\n")

    elif colour == "purplepink":
        print(f"  {Fore.LIGHTMAGENTA_EX} {name}\n")
    
    elif colour == "greenblue":
        print(f"  {Fore.LIGHTCYAN_EX} {name}\n")

    elif colour == "water":
        print(f"  {Fore.LIGHTBLUE_EX} {name}\n")
    
    elif colour == "pinkred":
        print(f"  {Fore.LIGHTRED_EX} {name}\n")

    elif colour == "purpleblue":
        print(f"  {Fore.LIGHTBLUE_EX} {name}\n")
    
    elif colour == "brazil":
        print(f"  {Fore.LIGHTGREEN_EX} {name}\n")

    elif colour == "random":
        print(f"  {Fore.LIGHTWHITE_EX} {name}\n")
    
    else:
        print(f"  {Fore.LIGHTCYAN_EX} {name}\n")


def print_group_create(name, group_id):
    colour = config("menu")

    if colour == "blackwhite":
        print(f"    Group Created - {Fore.LIGHTWHITE_EX}{name}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{group_id} ")

    elif colour == "purplepink":
        print(f"    Group Created - {Fore.LIGHTMAGENTA_EX}{name}{Fore.RESET} | {Fore.LIGHTMAGENTA_EX}{group_id} ")
    
    elif colour == "greenblue":
        print(f"    Group Created - {Fore.LIGHTCYAN_EX}{name}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{group_id} ")

    elif colour == "water":
        print(f"    Group Created - {Fore.LIGHTBLUE_EX}{name}{Fore.RESET} | {Fore.LIGHTBLUE_EX}{group_id} ")
    
    elif colour == "pinkred":
        print(f"    Group Created - {Fore.LIGHTRED_EX}{name}{Fore.RESET} | {Fore.LIGHTRED_EX}{group_id} ")

    elif colour == "purpleblue":
        print(f"    Group Created - {Fore.LIGHTBLUE_EX}{name}{Fore.RESET} | {Fore.LIGHTBLUE_EX}{group_id} ")
    
    elif colour == "brazil":
        print(f"    Group Created - {Fore.LIGHTGREEN_EX}{name}{Fore.RESET} | {Fore.LIGHTGREEN_EX}{group_id} ")

    elif colour == "random":
        print(f"    Group Created - {Fore.LIGHTWHITE_EX}{name}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{group_id} ")
    
    else:
        print(f"    Group Created - {Fore.LIGHTCYAN_EX}{name}{Fore.RESET} | {Fore.LIGHTCYAN_EX}{group_id} ")
#this dont work btw


def vast_print(content):

    colour = config("menu")

    if colour == "blackwhite":
        print(f"  {Fore.LIGHTWHITE_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")

    elif colour == "purplepink":
        print(f"  {Fore.LIGHTMAGENTA_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")
    
    elif colour == "greenblue":
        print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")

    elif colour == "water":
        print(f"  {Fore.LIGHTBLUE_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")
    
    elif colour == "pinkred":
        print(f"  {Fore.LIGHTRED_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")

    elif colour == "purpleblue":
        print(f"  {Fore.LIGHTBLUE_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")
    
    elif colour == "brazil":
        print(f"  {Fore.LIGHTGREEN_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")

    elif colour == "random":
        print(f"  {Fore.LIGHTWHITE_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")
    
    else:
        print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.RED}=>{Fore.WHITE} {content}")



def print_menu_choice():

    colour = config("menu")

    if colour == "blackwhite":
        print(f"                                                  {Fore.LIGHTWHITE_EX}Menu Choice => ", end='')

    elif colour == "purplepink":
        print(f"                                                  {Fore.LIGHTMAGENTA_EX}Menu Choice => ", end='')
    
    elif colour == "greenblue":
        print(f"                                                  {Fore.LIGHTCYAN_EX}Menu Choice => ", end='')

    elif colour == "water":
        print(f"                                                  {Fore.LIGHTBLUE_EX}Menu Choice => ", end='')
    
    elif colour == "pinkred":
        print(f"                                                  {Fore.LIGHTRED_EX}Menu Choice => ", end='')

    elif colour == "purpleblue":
        print(f"                                                  {Fore.LIGHTBLUE_EX}Menu Choice => ", end='')
    
    elif colour == "brazil":
        print(f"                                                  {Fore.LIGHTGREEN_EX}Menu Choice => ", end='')

    elif colour == "random":
        print(f"                                                  {Fore.LIGHTWHITE_EX}Menu Choice => ", end='')
    
    else:
        print(f"                                                  {Fore.LIGHTCYAN_EX}Menu Choice => ", end='')


def print_colour_choice():

    colour = config("menu")

    if colour == "blackwhite":
        print(f"                                                  {Fore.LIGHTWHITE_EX}Colour Choice => ", end='')

    elif colour == "purplepink":
        print(f"                                                  {Fore.LIGHTMAGENTA_EX}Colour Choice => ", end='')
    
    elif colour == "greenblue":
        print(f"                                                  {Fore.LIGHTCYAN_EX}Colour Choice => ", end='')

    elif colour == "water":
        print(f"                                                  {Fore.LIGHTBLUE_EX}Colour Choice => ", end='')
    
    elif colour == "pinkred":
        print(f"                                                  {Fore.LIGHTRED_EX}Colour Choice => ", end='')

    elif colour == "purpleblue":
        print(f"                                                  {Fore.LIGHTBLUE_EX}Colour Choice => ", end='')
    
    elif colour == "brazil":
        print(f"                                                  {Fore.LIGHTGREEN_EX}Colour Choice => ", end='')

    elif colour == "random":
        print(f"                                                  {Fore.LIGHTWHITE_EX}Colour Choice => ", end='')
    
    else:
        print(f"                                                  {Fore.LIGHTCYAN_EX}Colour Choice => ", end='')



def change_colours():
    update_title(f"Vast Spammer  •  Change Colour", config('token'))
    clear()
    print_colours()
    print_colour_choice()
    choice = int(input())

    if choice == 1:
        colour = "blackwhite"

    elif choice == 2:
        colour = "purplepink"

    elif choice == 3:
        colour = "greenblue"

    elif choice == 4:
        colour = "water"

    elif choice == 5:
        colour = "pinkred"

    elif choice == 6:
        colour = "purpleblue"

    elif choice == 7:
        colour = "brazil"

    elif choice == 8:
        colour = "random"
    
    else:
        change_colours()
    


    data = {
        "token": config("token"),
        "menu": colour
    }

    json.dump(data, open("data/config/config.json","w+"), indent=4)

def percentage(part, whole):
  percentage = 100 * float(part)/float(whole)
  return str(percentage)[:-13]

def add_groups():
    Groups.clear()
    if os.path.exists('data/groups/groups.txt'):
        with open("data/groups/groups.txt", "r") as f:
            for line in f:
                Groups.append(line.strip().replace("\n", ""))


def one_token_create():
    update_title(f"Vast Spammer  •  Group Creator", config('token'))
    clear()
    print_text()
    print_module("Group Creator")
    print_with_ends(f"Group Icon (Smaller image = quicker): ")
    icon = input()
    if '"' in icon: icon = icon.split('"')
    clear()
    print_text()
    vast_print("Started Group Creator, it will stop creating group chats when you close the program")
    trigger_notification("Group Creator", "Started")
    sleep(3)
    token = config('token')

    while True:
        for i in range(10):
            try:
                group = requests.post("https://discord.com/api/v9/users/@me/channels", headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4609.3 Safari/537.36", "Content-Type": "application/json"}, json={"recipients":[], "name": "balls"})
                try:
                    group_id = group.json()['id']
                    open("data/groups/groups.txt", "a+").write(f"\n{group_id}")
                    worked = True

                except:
                    worked = False
                
                if worked == False:
                    vast_print("Group spammer stopped due to ratelimit.")
                    time.sleep(1)
                    trigger_notification("Group Creator Ratelimit", f"Trying again in {group.json()['retry_after']} seconds")
                    time.sleep(5)
                
                elif worked == True:

                    def send(group_id):
                        headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4609.3 Safari/537.36", "Content-Type": "application/json"}
                        messagedata = {"content":"xeny, jonah & qoft were here <33 \n ```vast on top``` ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| @everyone discord.gg/Hwj7ETmuJy","nonce":"","tts":"true"}
                        send_msg = requests.post(f"https://discord.com/api/v9/channels/{group_id}/messages", json=messagedata, headers=headers)
                        if send_msg.status_code == 429:
                            sleep(2)
                            send(group_id)

                    def edit(group_id):
                        headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4609.3 Safari/537.36", "Content-Type": "application/json"}
                        with open(icon, "rb") as image_file:
                            encoded_string = base64.b64encode(image_file.read())
                            encoded_string = encoded_string.decode('utf-8')
                        #edit = {"name": name, "icon": "data:image/png;base64," + encoded_string}
                        namae = os.urandom(random.randint(20,40)).hex()
                        edit = {"name": namae, "icon": "data:image/png;base64," + encoded_string} 
                        # xeny here to save the day!! if u use a specific name then its easy asf to make a script which leaves all groups with that name.
                        # its much better to use a random hex
                        # its even safer to have the hex a random length so nobody can leave all groups with a certain length
                        # :Catkiss: (life tip #584)
                        edit_grp = requests.patch(f"https://discord.com/api/v9/channels/{group_id}", json=edit, headers=headers)
                        if edit_grp.status_code == 429:
                            time.sleep(2)
                            edit(group_id)
                        print_group_create(namae, group_id) 
                    edit(group_id)
                    send(group_id)
            
            except:
                pass
            
            time.sleep(600)






def namechanger(token, group_id, name):
    try:
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        edit = {"name": f"{name}"}
        edit_grp = requests.patch(f"https://discord.com/api/v9/channels/{group_id}", json=edit, headers=headers)
        if edit_grp.status_code == 429:
            sleep(1)
            edit(group_id)
        
    except Exception as e:
        if "Max retries" in str(e):
            vast_print("Unable to connect to discord.com")
        if "429" in str(e):
            vast_print("Too many requests")

def pfpchanger(token, group_id, imgb64):
    try:
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        edit = {"icon": "data:image/png;base64," + imgb64}
        edit_grp = requests.patch(f"https://discord.com/api/v9/channels/{group_id}", json=edit, headers=headers)
        if edit_grp.status_code == 429:
            time.sleep(2)
            edit(group_id)
        
    except Exception as e:
        pass

def groupadder(token, group_id, user_id, user_choice):
    try:
        headers = {
            "Authorization":
            token,
            "accept":
            "*/*",
            "accept-language":
            "en-US",
            "connection":
            "keep-alive",
            "cookie":
            f'__cfduid={os.urandom(43).hex()}; __dcfduid={os.urandom(32).hex()}; locale=en-US',
            "DNT":
            "1",
            "origin":
            "https://discord.com",
            "sec-fetch-dest":
            "empty",
            "sec-fetch-mode":
            "cors",
            "sec-fetch-site":
            "same-origin",
            "referer":
            "https://discord.com/channels/@me",
            "TE":
            "Trailers",
            "User-Agent":
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) discord/1.0.9001 Chrome/83.0.4103.122 Electron/9.3.5 Safari/537.36",
            "X-Super-Properties":
            "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRGlzY29yZCBDbGllbnQiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfdmVyc2lvbiI6IjEuMC45MDAxIiwib3NfdmVyc2lvbiI6IjEwLjAuMTkwNDIiLCJvc19hcmNoIjoieDY0Iiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODMwNDAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9"
        }
        if user_choice == "add":
            requests.put(f"https://discord.com/api/v9/channels/{group_id}/recipients/{user_id}", headers=headers)
        #group3 = requests.put("https://discord.com/api/v9/channels/898665952563060807/recipients/898634379348279297", headers=headers)
        if user_choice == "remove":
            requests.delete(f"https://discord.com/api/v9/channels/{group_id}/recipients/{user_id}", headers=headers)

    except Exception as e:
        print(e)



def check(token):
    h = {'Authorization': str(token), 'Content-Type': 'application/json'} 
    r = requests.get(f'https://discord.com/api/v9/users/@me', headers=h)
    if r.status_code == 200:
        return r.json()['id']

def multi_account_create(token, user_id, transfer_id):
    for _ in range(10):
        try:
            group = requests.post("https://discord.com/api/v9/users/@me/channels", headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4609.3 Safari/537.36", "Content-Type": "application/json"}, json={"recipients":[], "name": "balls"})
            try:
                group_id = group.json()['id']
                open("data/groups/groups.txt", "a+").write(f"{group_id}\n")
                worked = True
            except:
                worked = False
                if group.status_code == 401 or 429 or 403:
                    vast_print("IP Blacklisted by discord. Please connect/reconnect to a VPN")
                else:
                    pass
            
            if worked == False:
                break
            
            elif worked == True:

                groupadder(token, group_id, transfer_id, "add")

                def send(group_id):
                    headers={"Authorization": token, "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4609.3 Safari/537.36", "Content-Type": "application/json"}
                    messagedata = {"content":"xeny, jonah & qoft were here\n ```vast on top``` ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| @everyone https://www.youtube.com/watch?v=pA_wzHc4q6M","nonce":"","tts":"true"}
                    send_msg = requests.post(f"https://discord.com/api/v9/channels/{group_id}/messages", json=messagedata, headers=headers)
                    if send_msg.status_code == 429:
                        time.sleep(2)
                        send(group_id)


                send(group_id)
                groupadder(token, group_id, user_id, "remove")
        except Exception as e:
            pass





def get_groups():
    add_groups()
    count = 0 
    for group_id in Groups:
        count = count + 1
    trigger_notification("Group Count", f"{count} groups")


def main_menu():
    amount = 0
    token = config('token')
    update_title(f"Vast Spammer  •  Main Menu", token)
    clear()
    print_menu()
    print_menu_choice()
    choice = input()

    try:
        choice = int(choice)
    except:
        main_menu()


    if choice == 1:
        clear()
        one_token_create()
        main_menu()
    
    elif choice == 2:
        update_title(f"Vast Spammer  •  Add/Remove", token)
        clear()
        print_text()
        print_module("Add/Remove Users")
        print_with_ends(f"User ID: ")
        user_id = input()
        print_with_ends(f"Add or Remove: ")
        user_choice = input().lower()
        clear()
        print_text()
        vast_print("Started add/remove users module.")
        start = time.perf_counter()
        if user_choice == "add":
            user_print = "Added"
        elif user_choice == "remove":
            user_print = "Removed"
        group_amount = 0
        sex = open("data/groups/groups.txt", "r")
        for line in sex:
            if line != "\n":
                group_amount += 1
        sex.close()
        with open("data/groups/groups.txt","r") as f:
            # dont look at this im retarded
            for line in f:
                amount += 1
                sleep(0.02)
                update_title(f"Vast Spammer  •  Add/Remove • {user_print} {amount}/{group_amount} times • {percentage(amount, group_amount)}% Done")
                stripped_line = line.strip()
                group_id = stripped_line.replace("\n", "")
                threading.Thread(target=groupadder, args=[token, group_id, user_id, user_choice]).start()
        finish = time.perf_counter()
        trigger_notification("Add/Remove User", f"Completed task in {round(finish-start, 2)} seconds")
        main_menu()
    
    elif choice == 3:
        update_title(f"Vast Spammer  •  Change Token", token)
        clear()
        print_text()
        print_module("Change Token")
        print_with_ends(f"New Token: ")
        token = input()
        if '"' in token: token = token.split('"')[1]
        menuC = config("menu")
        data = {
            "token": token,
            "menu": menuC
        }
        json.dump(data, open("data/config/config.json","w+"), indent=4)
        trigger_notification("Vast Spammer", "Token changed")
        main_menu()


    elif choice == 4:
        update_title(f"Vast Spammer  •  Transfer Groups", token)
        clear()
        print_text()
        print_module("Transfer Groups")
        vast_print("All groups must only have you in it.")
        sleep(2)
        print_with_ends("Do all your groups have only you in them? (yes/no): ")
        check_input = input().lower()
        if check_input == "no":
            vast_print("Please remove everyone from the groups, then run this module again.")
            sleep(4)
            main_menu()
        elif check_input == "yes":
            print()
            print_with_ends("Are you friends with the user you want to transfer to? (yes/no): ")
            check_input = input().lower()
            if check_input == "no":
                vast_print("Please add the user, then run this module again.")
                sleep(4)
                main_menu()
            
            elif check_input == "yes":
                print_with_ends("User ID you want to transfer to: ")
                transfer_id = input()
                print()
                vast_print("Getting your ID.....")
                h = {'Authorization': token, 'Content-Type': 'application/json'} 
                r = requests.get(f'https://discord.com/api/v9/users/@me', headers=h)
                try:
                    user_id = r.json()["id"]
                    vast_print(f"Fetched ID: {user_id}")
                except:
                    vast_print("Invalid token....")
                    sleep(2)
                    main_menu()
                
                sleep(2)
                clear()
                print_text()
                print_module("Transfer Groups")
                
                try:
                    get_uinfo = requests.get(f"https://discord.com/api/v9/users/{transfer_id}", headers={"Authorization": config("token")}).json()
                    username = get_uinfo["username"]+"#"+get_uinfo["discriminator"]
                except:
                    vast_print("Invalid Transfer ID....")
                    sleep(2)
                    main_menu()
                vast_print(f"Group Owner ID: {user_id}")
                vast_print(f"Started transferring groups to {username}.")
                print()
                vast_print(f"Adding {username} to group chats")
                with open("data/groups/groups.txt","r") as f:
                    for line in f:
                        amount += 1
                        update_title(f"Vast Spammer  •  Transfer Groups • Transfered {amount} groups")
                        sleep(0.02)
                        stripped_line = line.strip()
                        group_id = stripped_line.replace("\n", "")
                        
                        t = threading.Thread(target=groupadder, args=[token, group_id, transfer_id, "add"])
                        t.start()

                vast_print("Leaving group chats....")
                with open("data/groups/groups.txt","r") as f:
                    for line in f:
                        sleep(0.02)
                        stripped_line = line.strip()
                        group_id = stripped_line.replace("\n", "")
                        t = threading.Thread(target=groupadder, args=[token, group_id, user_id, "remove"])
                        t.start()

        else:
            vast_print("Not a valid option..")
        main_menu()





    elif choice == 5: # Name Changer
        update_title(f"Vast Spammer • Name Changer", token)
        clear()
        print_text()
        print_module("Name Changer")
        vast_print("Leave blank for random name")
        print_with_ends(f"Name: ")
        namesex = input("")
        clear()
        print_text()
        vast_print("Started name changer module.")
        group_amount = 0
        sex = open("data/groups/groups.txt", "r")
        for line in sex:
            if line != "\n":
                group_amount += 1
        sex.close()
        
        with open("data/groups/groups.txt", "r") as f:
            if namesex:
                for line in f:
                    name = ""
                    name = f"{namesex} | {os.urandom(3).hex()}"
                    amount += 1
                    update_title(f"Vast Spammer  •  Name Changer • Changed name of {amount}/{group_amount} groups to {name} • {percentage(amount, group_amount)}% Done") 
                    time.sleep(0.06)
                    stripped_line = line.strip()
                    group_id = stripped_line.replace("\n", "")
                    t = threading.Thread(target=namechanger, args=[token, group_id, name])
                    t.start()
            elif not namesex:
                for line in f:
                    name = os.urandom(15).hex()
                    amount += 1
                    update_title(f"Vast Spammer  •  Name Changer • Changed name of {amount}/{group_amount} groups to {name} • {percentage(amount, group_amount)}% Done") 
                    time.sleep(0.06)
                    stripped_line = line.strip()
                    group_id = stripped_line.replace("\n", "")
                    t = threading.Thread(target=namechanger, args=[token, group_id, name])
                    t.start()
        trigger_notification("Mass Name Changer", "Completed")
        main_menu()


    elif choice == 6:
        update_title(f"Vast Spammer  •  Mass PFP Change", token)
        clear()
        print_text()
        print_module("Mass PFP Change")
        vast_print("Cannot be a link, has to be a image saved to your PC")
        print_with_ends(f"Image file (make sure its under 50kb): ") 
        image = input()
        if '"' in image: image = image.split('"')[1]
        clear()
        print_text()
        vast_print("Started Mass PFP module.")
        start = time.perf_counter()
        with open(image, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
            encoded_string = encoded_string.decode('utf-8')
        group_amount = 0
        sex = open("data/groups/groups.txt", "r")
        for line in sex:
            if line != "\n":
                group_amount += 1
        sex.close()
        with open("data/groups/groups.txt", "r") as f:
            for line in f:
                amount += 1
                update_title(f"Vast Spammer  •  Mass PFP Change • Changed {amount}/{group_amount} pfps • {percentage(amount, group_amount)}% Done")
                time.sleep(0.25)
                stripped_line = line.strip()
                group_id = stripped_line.replace("\n", "")
                t = threading.Thread(target=pfpchanger, args=[token, group_id, encoded_string])
                t.start()
        finish = time.perf_counter()
        trigger_notification("Mass PFP Changer", f"Completed task in {round(finish-start, 2)} seconds")
        main_menu()

    elif choice == 7:
        get_groups()
        main_menu()
    
    elif choice == 8:
        change_colours()
        main_menu()

    elif choice == 9:
        webbrowser.open('https://github.com/8ua/Discord-Call-Crasher', new=2)
        trigger_notification("Call Crasher", f"Opened Call Crasher Source")
        main_menu()
    
    elif choice == 10:
        amount = 0
        update_title(f"Vast Spammer  •  Multi-Account Group Creator", token)
        clear()
        print_text()
        print_module("Multi-Account Group Creator")
        vast_print("This module requires valid Discord tokens.")
        sleep(1)
        vast_print("All your tokens must have the transfer ID account added")
        sleep(0.5)
        print()
        print_with_ends("Tokens File: ")
        tokens = input()
        print_with_ends("Transfer ID: ")
        transfer_id = input()
        if '"' in tokens:
            tokens = tokens.split('"')[1]
        tokens = open(tokens).read().splitlines()
        clear()
        print_text()
        vast_print("The module will stop when you close the program.")
        vast_print("If you want to use other modules open another Vast Spammer")
        sleep(1)
        print()
        print_with_ends("Press enter to start: ")
        input()
        while True:
            vast_print(f"Creating groups")
            for token in tokens:
                amount += 1
                update_title(f"Vast Spammer  •  Multi-Account Group Creator • Created {amount*10} groups")
                user_id = requests.get(f'https://discord.com/api/v9/users/@me', headers={'Authorization': str(token), 'Content-Type': 'application/json'}).json()['id']
                threading.Thread(target=multi_account_create, args=[token, user_id, transfer_id]).start()
                sleep(0.1)
            vast_print("Ratelimited on all tokens, starting functions again in 10 minutes")
            sleep(600)
            # hi 

    else:
        main_menu()



def auth():
    clear()
    if not os.path.exists("data/config/license.json"):
        authentication_done = False
        while authentication_done == False:
            print(default_text)
            vast_print("Vast Authentication")
            sleep(1)
            print_with_ends(f"Enter license key: ")
            license_key = input()
            print_with_ends("")
            text = "Checking license key...\n"
            for char in text:
                sys.stdout.write(char)
                time.sleep(.05)
            
            check_license = Authentication.get_user('license')
            if check_license == license_key:
                vast_print(f"Authentication successful!")
                sleep(2)
                authentication_done = True
                print_with_ends(f"Token: ")
                token = input()
                data = {
                    "token": token.strip(),
                    "menu": "greenblue"
                }
                json.dump(data,open("data/config/config.json","w+"),indent=4)

                data = {
                    "license": license_key.strip()
                }
                json.dump(data,open("data/config/license.json","w+"),indent=4)
                sleep(3)
                main_menu()

            else:
                vast_print("Authentication failed..")
                sleep(3)
                clear()
    
    else:
        print_text()
        vast_print("Vast Authentication")
        sleep(1)
        vast_print("Auto-detected previous license key....")
        sleep(1)
        vast_print("Checking license key...\n")
        try:
            license = license_config('license')
        except:
            license = None

        check_license = Authentication.get_user('license')

        if license == check_license:
            vast_print(f"Authentication successful!")
            sleep(0.5)
            main_menu()
        else:
            try:
                os.remove("data/config/license.json")
                auth()
                
            except Exception as e:
                pass



def setup():
    update_title(f"Vast Spammer Setup  •  #Winning")
    print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTBLACK_EX}=>{Fore.WHITE} Downloading Vast Spammer dependencies...")
    try:
        os.mkdir("data")
        os.mkdir("data/config")
        os.mkdir("data/images")
        os.mkdir('data/groups')
    except:
        pass
    r = requests.get("https://cdn.discordapp.com/attachments/854115180836028416/854569042596331590/logo.ico").content
    with open('data/images/logo.ico', 'wb') as handler:
        handler.write(r)    
    sleep(1)
    print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTBLACK_EX}=>{Fore.WHITE} Download complete...")
    trigger_notification('Vast Spammer', f'Download complete')
    print(f"  {Fore.LIGHTCYAN_EX}[{get_time()}]{Fore.RESET} {Fore.LIGHTBLACK_EX}=>{Fore.WHITE} Re-directing to setup...\n")
    sleep(3)
    auth()


def init():
    print(default_text)
    if not os.path.exists("data/"):
        setup()
    else:
        auth()


if __name__ == "__main__":
    update_title(f"Vast Spammer  •  #Winning")
    init()