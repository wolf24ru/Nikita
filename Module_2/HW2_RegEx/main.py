import re
import csv
from pprint import pprint

# def format_fio(contacts_list):
#     pass

if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    phone_patern = re.compile(
        r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})')
    phone_patern_add = re.compile(
        r'(\+7|8)+[\s(]*(\d{3,3})[\s)-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s]*[(доб.\s]*(\d+)[)]*')
    # (r'доб[.\s]+(\d+)'))
    for person_list in contacts_list[1:]:
        n = 0
        for fio_in_list in person_list[0:2]:
            # поместить Фамилию, Имя и Отчество человека в поля
            # lastname, firstname и surnameсоответственно.
            # В записной книжке изначально может быть
            # Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О;

            n += 1
            fio = fio_in_list.split()

            if len(fio) > 1:
                if n == 1:
                    for i in range(0, len(fio)):
                        person_list[i] = fio[i]
                elif n == 2:
                    for i in range(1, len(fio) + 1):
                        person_list[i] = fio[i - 1]

    # привести все телефоны в формат +7(999)999-99-99.
    # Если есть добавочный номер, формат будет такой:
    # +7(999)999-99-99 доб.9999;
        for str_list in person_list:
            index_list = person_list.index(str_list)
            person_list[index_list] = phone_patern_add.sub(
                r'+7(\2)\3-\4-\5 доб.\6', str_list)
        for str_list in person_list:
            index_list = person_list.index(str_list)
            person_list[index_list] = phone_patern.sub(
                r'+7(\2)\3-\4-\5', str_list)

    # без понятия почему в одном цикле не работает

    # объединить все дублирующиеся записи о человеке в одну.
    result_list = []
    repit_items = set()
    for num, one_person in enumerate(contacts_list):
        merge_list = []
        fio = [name for name in one_person[:2]]
        for index_1, list_p in enumerate(contacts_list[num + 1:]):
            if fio[0] in list_p and fio[1] in list_p:
                for i in range(len(list_p)):
                    one = contacts_list[num][i]
                    tow = list_p[i]
                    repit_items.add(num)
                    repit_items.add(num + index_1 + 1)
                    if one == tow:
                        merge_list.append(one)
                    elif one == '' and tow != '':
                        merge_list.append(tow)
                    else:
                        merge_list.append(one)
        if num in repit_items:
            if merge_list:
                result_list.append(merge_list)
        else:
            result_list.append(one_person)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(result_list)
