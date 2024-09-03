from flask import Flask, render_template, redirect
from Display import create_banner
from PIL import Image
import WaveShareV4 as Display
from threading import Thread
import config
import random
import json
import time
import os

def load_json(filename="config.json"):
    with open(filename, "r") as file:
        return json.load(file)

def save_json(data, filename="config.json"):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def create_brain(): 
    data = {
        "device":  {
            "name": random.choice(config.PossibleNames),
            "level": 1,
            "created": time.strftime("%d.%m.%y // %T")
        }
    }
    save_json(data)

def init():
    if not os.path.exists("brain.json"):
        create_brain()
    print("Initial proccess successfully exited!")
    main()

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

init()