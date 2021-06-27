import requests
import time
import os
from bs4 import BeautifulSoup as bs

def req(data):
    link = requests.get(data)
    a = bs(link.content.decode('utf-8'), 'html.parser')
    return a

def rm(var):
    if os.name == "nt":
        os.system("del " + var)
    else:
        os.system("rm -r " + var)

def save(data, var):
    mksure = os.path.exists(var)
    if mksure == True:
        rm(var)
    f = open(var, "w")
    f.write(data)
    f.close

def clear():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
