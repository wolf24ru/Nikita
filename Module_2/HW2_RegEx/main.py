import re
import csv
from pprint import pprint


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

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
        (\+7|8)\s?\(?(\d+)\s?\)?-?(\d+)
    pprint(contacts_list)
    # привести все телефоны в формат +7(999)999-99-99. Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999;

    # объединить все дублирующиеся записи о человеке в одну.


# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
