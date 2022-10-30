#!/usr/bin/env/python3

import os
from colorama import Fore
import time

os.system("clear")
time.sleep(1)
print(Fore.MAGENTA)
os.system("figlet -f slant  FTool")
time.sleep(1)
print(Fore.RED + "Gerekli Modüller Yükleniyor...")
os.system("pip install colorama > /dev/null 2>&1")
os.system("clear")
print(Fore.MAGENTA)
os.system("figlet -f slant FTool")
print(Fore.GREEN + "Gerekli Modüller Yüklendi ✓")
time.sleep(1)
print("~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(0.5)
print(Fore.RED + "Paketler Güncelleniyor...")
os.system("apt update > /dev/null 2>&1")
os.system("clear")
print(Fore.MAGENTA)
os.system("figlet -f slant FTool")
print(Fore.GREEN + "Gerekli Modüller Yüklendi ✓")
print("~~~~~~~~~~~~~~~~~~~~~~~")
print(Fore.GREEN + "Paketler Güncellendi ✓") 
time.sleep(0.5)
giris = input(Fore.RED + "\nFTool'u Başlatmak İstiyor musunuz? [Y/n] ")

if (giris == "y" or giris=="Y"):
	print(Fore.GREEN + "FTool Başlatılıyor...")
	time.sleep(2)
	os.system("python3 FTool.py")
