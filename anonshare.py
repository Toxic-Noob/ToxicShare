#!/bin/usr/python3
#################################################
# Coded By HunterSl4d3
# A Product of ToxicNoob
# https://github.com/Toxic-Noob/
# Do Not try to copy any code
# Copying others code will not make you a Coder
#################################################

import os
import sys
import json
import time
import subprocess as s
import requests
import mechanize

br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

def logopsb(z):
    for l in z + '\n':
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.003)
        
def psb(x):
    for t in x + '\n':
        sys.stdout.write(t)
        sys.stdout.flush()
        time.sleep(0.03)

def logo():
    os.system("clear")
    logopsb("\033[0;92m _____         _      ____  _                    \n|_   _|____  _(_) ___/ ___|| |__   __ _ _ __ ___ \n  | |/ _ \ \/ / |/ __\___ \| '_ \ / _` | '__/ _ \ \n  | | (_) >  <| | (__ ___) | | | | (_| | | |  __/\n  |_|\___/_/\_\_|\___|____/|_| |_|\__,_|_|  \___|\n                                                 ")
    logopsb("\033[3;90m			A Product Of ToxicNoob\033[0;92m")
    time.sleep(0.6)
    logopsb("\033[34m\n|****************************************************|\n|\033[3m Author   : HunterSl4d3                             \033[0;34m|\n|\033[3m Tool     : Anonymous Share                         \033[0;34m|\n|\033[3m Version  : 1.0                                     \033[0;34m|\n|\033[3m Link     : https://www.github.com/Toxic-Noob/	     \033[0;34m|\n|\033[3m Coded By : HunterSl4d3      		     	     \033[0;34m|\n******************************************************")
    time.sleep(0.8)

def upload():
    path = input("\n\033[92;3m[*] Enter Your File Location:> ")
    if os.path.exists(path):
        psb("\n[*] Upload Process Started..")
        psb("[*] Please Wait..")
    else:
        psb("\n\033[31m[!] File Not Found!!")
        psb("[!] Check Your File Location And Try Again!!\033[40;37;0m")
        time.sleep(1)
        os.system("python anonshare.py")
    
    JData = s.getoutput("curl -F \'file=@"+path+"\' https://api.anonfiles.com/upload")

    JData = JData.split("\n")
    JData = JData[-1]

    JData = json.loads(JData)
    long_url = (JData["data"]["file"]["url"]["full"])
    short_url = (JData["data"]["file"]["url"]["short"])

    print("\n[Long URL]:\t\033[35m"+long_url)
    print("\n\033[92m[Short URL]:\033[35m\t"+short_url+"\n\033[37;40;0m") 
    
    
    
def download():
    if not os.path.exists("/sdcard/Anon_Downloads"):
        os.mkdir("/sdcard/Anon_Downloads")

    link = input("\n\033[92;3m[*] Enter URL of your File:> ")
    try:
        br.open(link)
    except:
        psb("\n\033[31m[!] Given URL is not correct..")
        psb("[!] Check your URL and try Again..\033[37;40;0m")
        time.sleep(1)
        os.system("python anonshare.py")
    psb("\n[*] Please Wait, Downloading in Process...")
    src = requests.get(link)
    TEMP = open(".temp.txt", "w")
    TEMP.write(src.text)
    TEMP.close()
    file = open(".temp.txt")
    src = file.readlines()
    line = 62
    url = src[line]
    while not "https://cdn-" in url:
            line = line + 1
            url = src[line]
    start = url.find("href=\"") + len("href=\"")
    end = url.find("\">")
    download_link = url[start:end]
    download_path = "/sdcard/Anon_Downloads"
    os.system("wget -P "+download_path+" "+download_link+" > /dev/null 2>&1")
    psb("\n[*] Your File Downloaded Successfully..")
    psb("[*] Saved in "+download_path+" Directory...\n\033[40;37;0m")
     
     
def options():
     psb("\n\033[92;3m[01] Upload File .")
     psb("[02] Download File .")
     psb("[03] Exit .")
     
     choise = input("\n[*] Enter Your Choise:> ")
     
     if(choise=="01") or (choise=="1"):
         upload()
     elif(choise=="02") or (choise=="2"):
         download()
     elif(choise=="03") or (choise=="3"):
         exit()
     else:
         psb("\n\033[31m[!] Please Choose a Correct Option..\033[37;40;0m")
         time.sleep(1)
         os.system("python anonshare.py")
         
if __name__=='__main__':
     logo()
     options()
