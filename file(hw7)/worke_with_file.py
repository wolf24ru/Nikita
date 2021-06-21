import pprint
from pathlib import Path
from tkinter.filedialog import askopenfilename


def Сook_book_dic(FILE_NAME):
    file_dir = Path(FILE_NAME)
    cook_book = {}
    with file_dir.open() as recipe_file:
        while True:
            dish_name = recipe_file.readline().strip()
            cook_book.update({dish_name: []})
            for num_ingredients in range(int(recipe_file.readline().strip())):
                ingredient = recipe_file.readline().strip()

                ingredient_name, quantity, measure = ingredient.split(' | ')
                cook_book[dish_name] += [{'ingredient_name': ingredient_name,
                                          'quantity': quantity,
                                          'measure': measure}]
            str_line = recipe_file.readline()
            if not(str_line):
                break
    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    ingredient_num_dict = {}
    for x in dishes:
        if x in cook_book:
            for i in cook_book[x]:
                if i['ingredient_name'] not in (ingredient_num_dict):
                    ingredient_num_dict.update({i['ingredient_name']:
                                                {'measure': i['measure'],
                                                 'quantity': int(i['quantity']) * person_count}})
                else:
                    quantity_repeat = int(i['quantity']) * person_count
                    ingredient_num_dict[i['ingredient_name']]['quantity'] = int(
                        ingredient_num_dict[i['ingredient_name']]['quantity']) + quantity_repeat
                    # ingredient_num_dict.update({i['ingredient_name']
                    # ['quantity']}) += '5'
    return ingredient_num_dict


if __name__ == '__main__':
    # FILE_NAME = '/home/user/Nikita/git/Nikita/file(hw7)/kooking.txt'
    FILE_NAME = askopenfilename()
    cook_book = Сook_book_dic(FILE_NAME)

    print('---------------')
    # print(cook_book)
    pprint.pprint(cook_book)
    print('---------------')
    print()
    dish_for_some_people = get_shop_list_by_dishes(
        ['Омлет', 'Молоко', 'Фахитос'], 2)
    pprint.pprint(dish_for_some_people)
