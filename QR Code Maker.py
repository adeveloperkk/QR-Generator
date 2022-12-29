#please install qrcode library in python using below command on command Prompt or terminal
#pip install qrcode
import qrcode as qr
a=str(input("Enter Your Website\t= "))#Enter your website name
b=str(input("Enter The Name To QR Code Image\t= "))#enter the name for QR code
img=qr.make(a)
c=b+".png"
img.save(c)
img.show() 
