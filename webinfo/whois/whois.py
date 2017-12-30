#!/usr/share/python
import requests as r
import socket,sys
import colorama
import json
from colorama import Fore, Back, Style
colorama.init()
index = """ 
   __   ___  ____                       _ _
|___ \ / _ \/ ___|  ___  ___ _   _ _ __(_) |_ _   _
  __) | (_) \___ \ / _ \/ __| | | | '__| | __| | | |
 / __/ \__, |___) |  __/ (__| |_| | |  | | |_| |_| |
|_____|  /_/|____/ \___|\___|\__,_|_|  |_|\__|\__, |
                                              |___/"""                                               

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("200.160.2.3",43))
s.send(sys.argv[1]+'\r\n')
resp = s.recv(1024)
print resp			
