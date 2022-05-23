from bs4 import BeautifulSoup
import requests
# import smtplib
import datetime
# import email.mime

curr_time = datetime.datetime.now()

content = ''


def extract_news(url):
    print('Extracting Hacker News Stories....')
    local_content = '<b>HN Top Stories: <b>\n'
    local_content += '<br>' + '-'*50 + "<br>"

    response = requests.get(url)
    cont = response.content
    soup = BeautifulSoup(cont, 'html.parser')

    for i, tag in enumerate(soup.find_all()):
        i
