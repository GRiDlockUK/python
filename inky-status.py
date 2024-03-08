#!/usr/bin/env python3

import time
import os
import socket

from inky.auto import auto
inky_display = auto()
inky_display.set_border(inky_display.WHITE)

from PIL import Image, ImageFont, ImageDraw
img = Image.new("P", (inky_display.WIDTH, inky_display.HEIGHT))
draw = ImageDraw.Draw(img)

from font_fredoka_one import FredokaOne
font = ImageFont.truetype(FredokaOne,20)

def get_ipaddress():
   ip_address = '';
   s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
   s.connect(("8.8.8.8",80))
   ip_address = s.getsockname()[0]
   return ip_address

ip_address=get_ipaddress()

def disk_stat(path):
    disk = os.statvfs(path)
    percent = (disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail) + 1
    return percent

diskfree=str(round(disk_stat("/"),1))

from gpiozero import CPUTemperature
cpu = CPUTemperature()

cputemp=str(round((cpu.temperature),1))

currtime=time.strftime("%D %T", time.localtime())

message="address: " + ip_address + "\ntemperature: " + cputemp + "°c\ndisk used: " + diskfree + "%\ndate: " + currtime

draw.text((0,0), message, inky_display.RED, font)
inky_display.set_image(img)
inky_display.show()
