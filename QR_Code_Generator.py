import qrcode
img=qrcode.make(input("Enter A Url:-"))

img.save("d.png")