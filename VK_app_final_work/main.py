import json
from tkinter import messagebox as mb
from datetime import datetime
from progress.bar import FillingSquaresBar
from YaDi import YandexDisk
from VK import FotoUpdate
from Insta import Insta_API

if __name__ == '__main__':
    # для работы программы необходимо каказть:
    # TOKEN_VK -- ключ доступа ВК (как получить - https://vk.com/dev/access_token);
    # TOKEN_YA -- OAuth-токен яндекса( как получить https://yandex.ru/dev/disk/rest/);
    # TOKEN_INSTA -- маркер доступа(действует 1 час)(как получить - https://developers.facebook.com/docs/instagram-basic-display-api/guides/getting-access-tokens-and-permissions/)
    #               для преобразования кода авторизации в маркер моно воспользоваться get_token_inst.py;
    # vk_user_id -- id пользователя в ВК для с которого получаем картинки
#______________Обязательное заполение________________________________________
    TOKEN_VK = ''
    TOKEN_YA = ''
    TOKEN_INSTA = ''
    vk_user_id =
#____________________________________________________________________________
    vk = FotoUpdate(TOKEN_VK)
    ya = YandexDisk(TOKEN_YA)
    insta = Insta_API(TOKEN_INSTA)

    now_date = datetime.now().date()
    choice_albums = {}
    n = 1

    for id_alnum, name_album in vk.albums_dict(vk_user_id).items():
        choice_albums.update({n: {'id_alnum': id_alnum,
                                  'name_album': name_album}})
        print(f'{n}: {name_album}')
        n += 1
    while True:
        chosen = int(
            input('Выберите номер албома из кооторого будут загруженны фотографии: '))
        if chosen in [x for x in range(1, len(choice_albums))]:
            break
        else:
            print('Введенного вами варианта не существует\
                \nПопробуйте снова:')    # def photos_get(self, owner_id):
    #     params = {
    #         'owner_id': owner_id,
    #         'album_id': 'profile',
    #         'count': 2,
    #         'access_token': self.vk_token,
    #         'v': 5.77
    #     }
    #     href = requests.get('https://api.vk.com/method/photos.get', params).json()
    #     # for photo in href['response']['items']:
    #     #     print(photo['sizes'][-1]['url'])
    #     print(href)
    #     return href

# запись из VK в яндекс
    folder_in_ya = f'{now_date}_vk'
    if ya.create_folder(folder_in_ya) == 201 or 409:
        names = [name['name']
                 for name in ya.get_files_list(folder_in_ya)['_embedded']['items']]
        vk_dic_photo = vk.photos_profile_get(vk_user_id,
                                             choice_albums[chosen]['id_alnum'],
                                             5)
        bar = FillingSquaresBar(
            'Download from VK in YA', max=len(vk_dic_photo))

        for photo in vk_dic_photo:

            if photo["file_name"] not in names:
                disk_file_path = f'{folder_in_ya}/{photo["file_name"]}'
            else:
                answer = mb.askyesno(
                    title="Вопрос",
                    message=f'Файл с именем {photo["file_name"]} уже существует\
                    \nЗаменить его?')
                if answer:
                    disk_file_path = f'{str(folder_in_ya)}/{photo["file_name"]}'
                else:
                    bar.next()
                    continue
            ya.upload_file_link_to_disk(disk_file_path,
                                        photo['url'])
            bar.next()
        bar.finish()
        print('all is done')
        with open('result.json', 'w') as fp:
            json.dump(vk_dic_photo, fp)
    else:
        print('Ошибка создания папки в Яндекс Диске')

# запись из инстограмма в яндекс
    folder_in_inst = f'{now_date}_inst'
    if ya.create_folder(folder_in_inst) == 201 or 409:
        photo_list_inst = insta.get_photo(6)['data']
        bar = FillingSquaresBar(
            'Download from Instagram in YA', max=len(photo_list_inst))
        for photo in photo_list_inst:
            disk_file_path = f'{folder_in_inst}/{photo["id"]}.jpg'
            ya.upload_file_link_to_disk(disk_file_path,
                                        photo['media_url'])
            bar.next()
    else:
        print('Ошибка создания папки в Яндекс Диске')
    bar.finish()
