#!/usr/bin/env python3

import pyqrcode

def generate_qr():
    link_to_post = "https://www.opensitesolutions.com"
    url = pyqrcode.create(link_to_post)
    url.png('url.png', scale=2) # Change scale level in increase or decrease size of png image
    print("Printing QR code")
    print(url.terminal())


if __name__ == '__main__':
    generate_qr()