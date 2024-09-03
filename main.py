from flask import Flask, render_template, request
from Images import create_banner
from PIL import Image
import Display
from threading import Thread
import json
import time
import os

def load_json(filename="brain.json"):
    with open(filename, "r") as file:
        return json.load(file)

def save_json(data, filename="brain.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def create_brain(): 
    data = {
        "device":  {
            "name": "harimtim",
            "level": 1,
            "created": time.strftime('%d.%m.%y // %T')
        }
    }
    save_json(data)

def init():
    try:
        if not os.path.exists("brain.json"):
            create_brain()
        print("Initial proccess successfully exited!")
        return True
    except:
        return False

def main():
    while True:
        try:
            create_banner(device_name=load_json()["device"]["name"], level=load_json()["device"]["level"])
            epd = Display.EPD()
            epd.init()
            epd.display(epd.getbuffer(Image.open("banner.bmp")), epd.getbuffer(Image.open("banner.bmp")))
        except Exception as e:
            os.system("clear")
            print(e)
        time.sleep(10)


if init():
    main()