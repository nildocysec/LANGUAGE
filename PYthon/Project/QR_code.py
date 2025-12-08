# This program generates QR code for websites

'''
# Install set-up and activate and deactivate in virtual environment on terminal

sudo apt install python3-venv -y
python3 -m venv qr-env
source qr-env/bin/activate
pip install qrcode[pil]

deactivate

'''
import qrcode

data = input("Enter URL : ").strip() # remove whitespaces with strip

file_name = input("Enter file name : ").strip()

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)
image = qr.make_image(fill_color='black', back_color='white')
image.save(file_name)
print("Done")


print("END",end='')