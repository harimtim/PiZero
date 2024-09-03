from flask import Flask, render_template, request
from Images import create_banner, create_bmp, create_clock
from PIL import Image
import Display
from threading import Thread
import config
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
            "name":  config.device_name,
            "level": 1,
            "created": time.strftime('%d.%m.%y // %T')
        }
    }
    save_json(data)

def change_name(name):
    try:
        data = load_json()
        data["device"]["name"] = name
        save_json(data)
        return True
    except:
        return False

def init():
    try:
        if not os.path.exists("brain.json"):
            create_brain()
            print("Brain created!")
        change_name(config.device_name)
        print("Name changed!")
        print("Initial proccess successfully exited!")
        return True

    except:
        return False

def main(img_interval: int = 10):
    epd = Display.EPD()
    epd.init()
    while True:
        try:
            data = load_json()
            if config.banner_template == 2:
                create_bmp(data["device"]["name"], data["device"]["level"], theme=config.color_theme)
            elif config.banner_template == 3:
                create_clock(theme=config.color_theme)
            else:
                create_banner(device_name=data["device"]["name"], level=data["device"]["level"], theme=config.color_theme)
            epd.display(epd.getbuffer(Image.open("banner.bmp")), epd.getbuffer(Image.open("banner.bmp")))
        except Exception as e:
            os.system("clear")
            print(e)
        time.sleep(img_interval)


if init():
    main(config.display_refresh_interval)