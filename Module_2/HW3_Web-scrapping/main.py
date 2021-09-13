import requests
import sys
from bs4 import BeautifulSoup
import_path_dec = '/home/user/Nikita/git/Nikita/Module_2/HW5_Decorators'
sys.path.insert(1,import_path_dec)
from Log_Decor import log_function

@log_function
def find_keywords(KEYWORDS):
    ret = requests.get('https://habr.com/ru/all/')
    ret.raise_for_status()
    result_list =[]

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
    return result_list

if __name__ == '__main__':
    KEYWORDS = ['дизайн', 'фото', 'web', 'python']
    result_list = find_keywords(KEYWORDS)

    
    print(result_list)
