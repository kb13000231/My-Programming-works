import qrcode

print('Welcome to QR code generator!')

text = input('Please enter the text to be encoded: ')

img = qrcode.make(text)

img.save(input('Please enter the file name: ') + '.png')
