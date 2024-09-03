from PIL import Image, ImageDraw, ImageFont
import os
import time
import socket
import config

def get_ssid():
    try:
        ssid = os.popen("nmcli -t -f active,ssid dev wifi | grep '^yes' | cut -d':' -f2").read().strip()
        if ssid:
            return ssid
        else:
            ssid = os.popen("iwgetid -r").read().strip()
            return ssid
    except Exception as e:
        print(f"Fehler beim Abrufen der SSID: {e}")
        return None

def create_banner(device_name, level, theme ,filename="banner.bmp"):
    width, height = 250, 122

    if theme == "black":
        color = "white"
    else:
        color = "black"

    # Erstelle ein neues Bild mit weißem Hintergrund
    image = Image.new('RGB', (width, height), theme)
    draw = ImageDraw.Draw(image)


    try:
        font = ImageFont.truetype(config.font_family, 14)
    except IOError:
        print("Benutzerdefinierte Schrift konnte nicht gefunden werden!")
        font = ImageFont.load_default()


    draw.text((5, 5), f"WLAN: {get_ssid()}", fill=color, font=font)
    draw.line((5, 20, 245, 20), fill=color, width=1)

    draw.text((5, 35), f"Name: {device_name}", fill=color, font=font)
    draw.line((5, 50, 245, 50), fill=color, width=1)

    draw.text((5, 65), f"Level: {level}", fill=color, font=font)
    draw.line((5, 80, 245, 80), fill=color, width=1)

    draw.text((5, 95), f"Time: {time.strftime('%T')}", fill=color, font=font)
    draw.line((5, 110, 245, 110), fill=color, width=1)

    image.save(filename)
    print("Bild wurde erstellt und gespeichert.")

def create_bmp(name, level, theme, filename="banner.bmp"):
    width, height = 250, 122

    if theme == "black":
        color = "white"
    else:
        color = "black"


    # Erstelle ein neues Bild mit weißem Hintergrund
    image = Image.new('RGB', (width, height), theme)
    draw = ImageDraw.Draw(image)


    try:
        font = ImageFont.truetype(config.font_family, 14)
    except IOError:
        print("Benutzerdefinierte Schrift konnte nicht gefunden werden!")
        font = ImageFont.load_default()


    draw.text((5, 3), f"WLAN: {get_ssid()}", fill=color, font=font)
    draw.line((0, 20, 255, 20), fill=color, width=1)

    draw.text((10, 28), f"Name: {name}", fill=color, font=ImageFont.truetype(config.font_family, 20))
    draw.text((10, 48), f"Level : {level}", fill=color, font=ImageFont.truetype(config.font_family, 20))
    #draw.text((10, 68), f"Version: {version}", fill=color, font=ImageFont.truetype(config.font_family, 20))


    draw.text((8, 103), f"SSH: Active", fill=color, font=font)
    draw.text((100, 105), f"Prototyp of Project by harimtim", fill=color, font=ImageFont.truetype(config.font_family, 10))
    draw.line((0, 100, 255, 100), fill=color, width=1)
    draw.line((90, 100, 90, 180), fill=color, width=1)

    image.save(filename)
    print("Bild wurde erstellt und gespeichert.")

def create_clock(theme, filename="banner.bmp"):

    if theme == "black":
        color = "white"
    else:
        color = "black"

    image = Image.new("RGB", (250, 122), theme)
    draw = ImageDraw.Draw(image)

    draw.rectangle((100, 50, 100, 50), fill="white", width=20)

    #draw.rectangle((50, 50, 200, 200), outline=(255, 0, 0), width=5, fill="white")

    draw.text((250/2, 122/2), time.strftime("%T"), fill=color, font=ImageFont.truetype(config.font_family, 20), anchor="mm")
    

    image.save("banner.bmp")

def create_img(theme, filename="banner.bmp"):

    if theme == "black":
        color = "white"
    else:
        color = "black"

    image = Image.new("RGB", (250, 122), theme)
    draw = ImageDraw.Draw(image)

    draw.line((0, 20, 255, 20), fill=color, width=1)
    draw.text((5, 3), f"WLAN: ", font=ImageFont.truetype("arial.ttf", 14), fill="black")
    draw.rectangle((100, 50, 100, 50), fill="white", width=20)

    #draw.rectangle((50, 50, 200, 200), outline=(255, 0, 0), width=5, fill="white")

    draw.text((250/2, 122/2), time.strftime("%T"), fill=color, font=ImageFont.truetype(config.font_family, 20), anchor="mm")
    

    image.save("banner.bmp")