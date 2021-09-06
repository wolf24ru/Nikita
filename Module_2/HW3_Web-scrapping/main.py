import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    result_list = []

    ret = requests.get('https://habr.com/ru/all/')
    ret.raise_for_status()

    soup = BeautifulSoup(ret.text, 'html.parser')
    articals = soup.find_all('article', class_='tm-articles-list__item')

    for artical in articals:
        artical_str = artical.get_text()
        for word in KEYWORDS:
            if artical_str.count(word):
                date = artical.find('time')['title']
                href = 'https://habr.com' + artical.find(
                    'a', class_='tm-article-snippet__title-link').get('href')
                title = artical.find(
                    'a', class_='tm-article-snippet__title-link').span.get_text()
                inter_result_list = [date, title, href]
                result_list.append(inter_result_list)
                break
    print(result_list)
