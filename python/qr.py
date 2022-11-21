import qrcode

link = 'https://www.instagram.com/luskald/?hl=pt-br'

img  = qrcode.make(link)

img.save('QRcode.png')