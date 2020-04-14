#!/usr/bin/env python3
from gpiozero import Button
from time import sleep
#from uArmWrapper import uArmWrapper
import os

button = Button(26)

while True:
    if button.is_pressed:
        print("Pressed")
        os.system('sudo shutdown -h now')
    # else:
        # print("Released")
    sleep(0.1)
