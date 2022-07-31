#!/usr/bin/env python3

import time
from colorama import Fore
import os

while True:
	os.system("pip install colorama")
	os.system("apt install git python -y")
	os.system("clear")
	print(Fore.RED)
	os.system("figlet -f slant FTool")
	print(Fore.GREEN)
	print(""" 
                  Coder By. FHACK

[1] Aevsploit              [11] Hammer 
[2] Cupp                   [12] Sqlmap
[3] T-U-R-K                [13] XerXes
[4] Zphisher               [14] Instagram-Bruter
[5] Red_HAWK               [15] Userrecon
[6] Ip-Tracer              [16] Root Kullanıcısı
[7] Impulse-SMS            [17] Termux-Banner
[8] Nikto                  [18] PhoneInfoga
[9] İnstaspam
[10] Black-Hydra
""")	
	giris = input("FTool >>> ")

	if giris=="1":
		os.system("git clone https://github.com/aevx/Aevsploit")

	elif giris=="2":
       		os.system("git clone https://github.com/Mebus/cupp")

	elif giris=="3":
		os.system("git clone https://github.com/yamanefkar/T-U-R-K")

	elif giris=="4":
		os.system("git clone https://github.com/htr-tech/zphisher")

	elif giris=="5":
		os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")

	elif giris=="6":
		os.system("git clone https://github.com/rajkumardusad/IP-Tracer.git")

	elif giris=="7":
		os.system("git clone https://github.com/LimerBoy/Impulse")

	elif giris=="8":
		os.system("git clone https://github.com/sullo/nikto")

	elif giris=="9":
		os.system("git clone https://github.com/tarik0/instaspamv5")

	elif giris=="10":
		os.system("git clone https://github.com/Gameye98/Black-Hydra")

	elif giris=="11":
		os.system("git clone https://github.com/cyweb/hammer.git")

	elif giris=="12":
		os.system("git clone https://github.com/sqlmapproject/sqlmap.git")

	elif giris=="13":
		os.system("git clone https://github.com/CyberXCodder/XerXes.git")

	elif giris=="14":
		os.system("git clone https://github.com/Bitwise-01/Instagram-")

	elif giris=="15":
		os.system("git clone https://github.com/issamelferkh/userrecon")

	elif giris=="16":
		os.system("clear")
		os.system("figlet Not :")
		print(Fore.RED + "Dikkat!!! Root Kullanıcısına Geçiş Yapmak için root Yazmanız Yeterlidir")
		time.sleep(2)
		os.system("pkg install -y proot && git clone https://github.com/Anonymous-Zpt/T-root && cd T-root && bash install.sh && ./start")

	elif giris=="17":
		os.system("git clone https://github.com/Bhai4You/Termux-Banner")

	elif giris=="18":
		os.system("git clone https://github.com/abhinavkavuri/PhoneInfoga")

	elif giris=="0":
		quit()

	else:
		print(Fore.RED + "Hatalı Giriş! Anasayfaya Yönlendiriliyorsunuz...")
		time.sleep(2)
		os.system("clear")
