
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }
def read_cook_book(filename):
    cook_book = {}

    with open (filename, 'r', encoding='utf-8') as f:
        while True:
            # Чтение названий блюд
            dish_name = f.readline().strip()
            if not dish_name:
                break
            # Чтение кол-ва ингредиентов
            ing_count = int(f.readline().strip())

            ingredients = [] # Чтение ингредиентов
            for _ in range(ing_count):
                ing_line = f.readline().strip()
                if ing_line:
                    ingredient_name, quantity, measure = map(str.strip, ing_line.split('|'))
                    ingredients.append({
                        'ingredient_name': ingredient_name,
                        'quantity': int(quantity),
                        'measure': measure
                    })

            cook_book[dish_name] = ingredients
            f.readline()

    return cook_book


cook_book = read_cook_book('vulgarity.txt')
print("Cook_book:")
for dish, ingredients in cook_book.items():
    print(f"{dish}: {ingredients}")


def get_shop_list_by_dishes(dishes, person_count):

    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                ing_name = ingredient['ingredient_name']
                quantity = ingredient['quantity'] * person_count
                measure = ingredient['measure']

                if ing_name in shop_list:
                    shop_list[ing_name][quantity] += quantity
                else:
                    shop_list[ing_name] = {
                        'measure': measure,
                        'quantity': quantity
                    }

    return shop_list


print("\nСписок покупок для ['Запеченный картофель', 'Омлет'] на 2 персоны:")
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
for k, v in shop_list.items():
    print(f"{k}: {v}")






