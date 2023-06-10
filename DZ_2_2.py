
def read_recipes(file_path):
    cook_book = {}

    with open(file_path, 'r') as file:
        while True:
            recipe_name = file.readline().strip()
            if not recipe_name:
                break

            ingredient_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredient_count):
                ingredient_line = file.readline().strip().split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_line[0],
                    'quantity': int(ingredient_line[1]),
                    'measure': ingredient_line[2]
                }
                ingredients.append(ingredient)

            cook_book[recipe_name] = ingredients

            # Skip the empty line between recipes
            file.readline()

    return cook_book

def get_shop_list_by_dishes(dishes, person_count, cook_book):
    shop_list = {}

    for dish in dishes:
        if dish in cook_book:
            ingredients = cook_book[dish]

            for ingredient in ingredients:
                name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = ingredient['quantity'] * person_count

                if name in shop_list:
                    shop_list[name]['quantity'] += quantity
                else:
                    shop_list[name] = {'measure': measure, 'quantity': quantity}

    return shop_list

def main():
    file_path = 'recipes.txt'
    cook_book = read_recipes(file_path)
    dishes = ['Запеченный картофель', 'Омлет']
    person_count = 2

    shop_list = get_shop_list_by_dishes(dishes, person_count, cook_book)

    print("{")
    for ingredient, values in shop_list.items():
        print(f"  '{ingredient}': {values},")
    print("}")

if __name__ == '__main__':
    main()

