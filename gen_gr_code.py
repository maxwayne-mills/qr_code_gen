#!/usr/bin/env python3

import pyqrcode

def gen_qr_code(user_url):
    url = pyqrcode.create(user_url)
    url.png('url.png', scale=8) # Change scale level in increase or decrease size of png image
    print("Printing QR code for URL " + str(user_url) )
    print(url.terminal())

if __name__ == '__main__':
    user_url = input("Enter URL: ")
    gen_qr_code(user_url)