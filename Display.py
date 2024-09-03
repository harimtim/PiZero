from PIL import Image, ImageDraw, ImageFont
import os
import time
import socket

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

def create_banner(device_name, level ,filename="banner.bmp", standardColor=True):
    width, height = 250, 122

    if standardColor == True:
        bgColor = "white"
        normalColor = "black"
    else:
        bgColor = "black"
        normalColor = "white"

    # Erstelle ein neues Bild mit weißem Hintergrund
    image = Image.new('RGB', (width, height), bgColor)
    draw = ImageDraw.Draw(image)


    try:
        font = ImageFont.truetype("arial.ttf", 12)
    except IOError:
        print("Benutzerdefinierte Schrift konnte nicht gefunden werden!")
        font = ImageFont.load_default()


    draw.text((5, 5), f"WLAN: {get_ssid()}", fill=normalColor, font=font)
    draw.line((5, 20, 245, 20), fill=normalColor, width=1)

    draw.text((5, 35), f"Name: {device_name}", fill=normalColor, font=font)
    draw.line((5, 50, 245, 50), fill=normalColor, width=1)

    draw.text((5, 65), f"Level: {level}", fill=normalColor, font=font)
    draw.line((5, 80, 245, 80), fill=normalColor, width=1)

    draw.text((5, 95), f"Time: {time.strftime("%T")}", fill=normalColor, font=font)
    draw.line((5, 110, 245, 110), fill=normalColor, width=1)

    image.save(filename)
    print("Bild wurde erstellt und gespeichert.")
