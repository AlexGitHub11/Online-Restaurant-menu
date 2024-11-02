import qrcode

# QR code to scan for menu
image = qrcode.make("http://127.0.0.1:8000")
image.save("qr.png")
