import requests
from bs4 import BeautifulSoup
import smtplib
# import time
from tkinter import Tk, Canvas, BOTH, Frame, Label, Text, Button, END

header = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'}


def find_price(URL):
    page = requests.get(URL, headers=header)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:])
    print(converted_price)
    outtext.insert(END, converted_price)
    b = float(input('Enter the desired price: '))
    if converted_price < b:
        send_email(URL)
    else:
        return None


def send_email(URL):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('Your e-mail here', 'Your oauth code here')

    subject = 'Price fell down'
    body = f'check the amazon link: {URL}'
    msg = f"Subject: {subject}\n\n{body}"
    receiver = input("Add receiver's e-mail id: ")
    server.sendmail('kb13000231@gmail.com', receiver, msg)

    print('Email has been sent')
    server.quit()


root = Tk()
root.title('Amazon Price Scrapper')
root.state('zoomed')


def getInput():
    inp = intext.get(1.0, "end-1c")
    find_price(inp)
    # lbl.config(text = "Provided Input: "+inp)


canvas = Canvas(root, bg='white', highlightthickness=0)
canvas.pack(fill=BOTH, expand=True)

a = '''Welcome, this is an Amazon Price Scrapper, Enter the URL below to get
the price of the desired item'''

infoframe = Frame(root, bg='blue')
infoframe.place(relwidth=0.6, relheight=0.2, relx=0.2)
infotext = Label(infoframe, text=a)
infotext.pack()

inframe = Frame(root, bg='red')
inframe.place(relwidth=0.6, relheight=0.3, relx=0.2, rely=0.2)
intext = Text(inframe, bg='green')
intext.pack()

outframe = Frame(root, bg='red')
outframe.place(relwidth=0.6, relheight=0.4, relx=0.2, rely=0.5)
outtext = Text(outframe, bg='yellow')
outtext.pack()

metaframe = Frame(root, bg='orange')
metaframe.place(relwidth=0.6, relheight=0.1, relx=0.2, rely=0.9)
inbutton = Button(metaframe, text='Item URL', command=getInput)
inbutton.pack()

# while True:
#     find_price()
#     time.sleep(60*60)

root.mainloop()
