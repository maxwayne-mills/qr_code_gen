# QR  code generator

Generate QR codes from scratch, code adapted from [Ngenge Senior](https://medium.com/@ngengesenior/qr-codes-generation-with-python-377735be6c5f)

- Setup environment
- log into virtual environment
- Install python modules
- execute python script.

## Set up environment

run the init script to create a virtual environment.
``` init.sh ```

## Log into virtual environment

source qrenv/bin/activate

## Install python modules

```pip3 install -r requirements```

## Execute python script

```./gen_qr_code.py ```

this will both display the QR code on the screen and within a file call url.png within the same directory. Updating the scale ```scale=8``` either up or down will create a larger or smaller PNG image.

###

Pyqrcode [Doc](https://pythonhosted.org/PyQRCode/)