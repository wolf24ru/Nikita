import requests
from bs4 import BeautifulSoup


def find_keywords_in_link(KEYWORDS, link):
    ret = requests.get(link)
    ret.raise_for_status()

    soup = BeautifulSoup(ret.text, 'html.parser')
    artical = soup.find('article',
                        class_='tm-page-article__content tm-page-article__content_inner')
    artica_text = artical.get_text()
    for word in KEYWORDS:
        if artica_text.count(word):
            date = artical.find('time')['title']
            href = link
            title = artical.find(
                'h1', class_='tm-article-snippet__title tm-article-snippet__title_h1').span.get_text()
            return [date, title, href]


if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    result_list = []
    ret = requests.get('https://habr.com/ru/all/')
    ret.raise_for_status()

    soup = BeautifulSoup(ret.text, 'html.parser')
    articals = soup.find_all('article', class_='tm-articles-list__item')
    for artical in articals:
        href = 'https://habr.com' + artical.find(
            'a', class_='tm-article-snippet__title-link').get('href')
        inter_result_list = find_keywords_in_link(KEYWORDS, href)
        if inter_result_list:
            result_list.append(inter_result_list)
    print(result_list)
