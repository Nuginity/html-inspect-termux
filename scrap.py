import os
import time
import requests
import module
from bs4 import BeautifulSoup as bs

pilihan = 0

def garis(var):
    a = 0
    while a < var:
        a += 1
        print("--------------------------------------")

def space(var):
    a = 0
    while a < var:
        a += 1
        print("")

def sleep(var):
    time.sleep(var)

module.clear()
space(1)
print("...::: INSPECT / DOWNLOAD HTML :::...")
sleep(0.5)
garis(1)
space(1)

link = input("Website Url :")
module.clear()

space(1)
print("Option")
sleep(1)
garis(1)
print("1. Inspect Element")
print("2. Save as HTML")
garis(1)

def obj1():
    try:
        pilihan = int(input("Input option 1/2 : "))
    except:
        return obj1()
    if pilihan == 1:
        module.clear()
        print(bs.prettify(module.req(link)))
    elif pilihan == 2:
        module.clear()
        print("...:::LOADING PLEASE WAIT:::...")
        data = module.req(link)
        data2 = str(data)
        space(1)
        nama = input("Save As : ")
        nama_split = nama.split(".")
        nama_jumlah = len(nama_split)
        if nama_split[nama_jumlah - 1] == "html":
            module.save(data2, nama)
            space(1)
            print("Success, save as " + nama)
            space(1)
        else:
            nama2 = nama + ".html"
            module.save(data2, nama2)
            space(1)
            print("Success, save as " + nama2)
            space(1)
obj1()
