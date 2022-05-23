import requests
from bs4 import BeautifulSoup as bs

user = input('Input Github Username: ')

base_url = 'https://github.com/'
data = requests.get(base_url + user)
soup = bs(data.content, 'html.parser')


def get_prof_img(soup):
    return soup.find('img', {'alt': 'Avatar'})['src']


print(get_prof_img(soup))
