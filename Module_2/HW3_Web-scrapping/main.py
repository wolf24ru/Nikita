import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']

    ret = requests.get('https://habr.com/ru/all/')
    # print(ret.text)

    soup = BeautifulSoup(ret.text, 'html.parser')
    articals = soup.find_all(class_='tm-articles-list__item')
    print(articals)
