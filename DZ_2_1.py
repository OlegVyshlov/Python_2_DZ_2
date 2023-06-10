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

file_path = 'recipes.txt'
cook_book = read_recipes(file_path)

print("cook_book = {")
for recipe_name, ingredients in cook_book.items():
    print(f"  '{recipe_name}': [")
    for ingredient in ingredients:
        print(f"    {ingredient},")
    print("  ],")
print("}")

