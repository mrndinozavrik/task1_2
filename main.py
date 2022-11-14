# Задание 1
from pprint import pprint
file_path = '/Users/admin/PycharmProjects/task1/recipes.txt'


def makecookbook(name_file):
  cook_book = {}
  with open('recipes.txt', encoding='UTF-8') as file:
    for i in file:
      name_food = i.strip()
      kol_vo = int(file.readline())
      ingrid = []
      for ingr in range(kol_vo):
        ingr = file.readline().split(' | ')
        ingredients = {'ingredientname': ingr[0].strip(), 'quantity': int(ingr[1]), 'measure': ingr[2].strip()}
        ingrid.append(ingredients)
      cook_book[name_food] = ingrid
      file.readline()
    return cook_book


pprint(makecookbook(file_path), width=70)
makecookbook(file_path)


# Задание 2

def get_shop_list_by_dishes(dishes: list, file_path: str, person_count=1):
    cook_book = makecookbook(file_path)
    ingrid = {}
    for dish_name in dishes:
        for ingredients in cook_book.get(dish_name, []):
            if ingredients['ingredientname'] in ingrid:
                ingrid[ingredients['ingredientname']]['quantity'] += ingredients['quantity'] * person_count
            else:
                ingrid[ingredients['ingredientname']] = {'quantity': ingredients['quantity'] * person_count, 'measure': ingredients['measure']}
    return ingrid
print(get_shop_list_by_dishes([ 'Омлет', 'Фахитос'], file_path,2))


get_shop_list_by_dishes('Омлет', file_path,3 )