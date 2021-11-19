def decode_to_string(bytes):
    '''convert bytes into string'''
    return bytes.decode("utf-8")

def get_countries_from_string(string):
    '''extract the countries from the string'''
    arr_of_countries = []
    start = None
    counter = 1
    # loop and slice countries from string
    for idx in range(len(string)):
        # " can be start or end of string
        if string[idx] == '"':
            # next char is a comma or closing bracket, indicates end of string
            if string[idx + 1] == ',' or string[idx + 1] == ']':
                arr_of_countries.append({'name': string[start:idx], 'id': "country" + str(counter)})
                counter += 1
            # else its the start of the string
            else:
                start = idx + 1

    return arr_of_countries

def get_name_and_image_of_recipe(country, cached_country_recipes, recipe_id):
    '''Retrieve image and name of recipe from cache'''

    # get recipe list
    recipe_list = cached_country_recipes[country]['results']

    # loop thru recipe list
    for idx in range(len(recipe_list)):
        curr_recipe = recipe_list[idx]
        if str(curr_recipe['id']) == recipe_id:
            return {'image': curr_recipe['image'], 'title': curr_recipe['title']}


def get_recipe_ingredients(id, recipe_list):
    '''Get all ingredients for recipe in cache'''
    ingredients_set = set()

    # nested loop to get each ingredient
    for idx in range(len(recipe_list[id][0]['steps'])):
        curr_ingredients = recipe_list[id][0]['steps'][idx]['ingredients']
        for j in range(len(curr_ingredients)):
            ingredients_set.add(curr_ingredients[j]['name'])

    # get data in set and convert into formatted data
    list_of_ingredients = []
    counter = 1

    for ingredient in ingredients_set:
        list_of_ingredients.append({"number": counter, "ingredient": ingredient})
        counter += 1

    return list_of_ingredients


def get_recipe_steps(id, recipe_list):
    '''Get recipe steps in cache'''
    steps_of_recipe = []

    # loop to get all the steps
    for idx in range(len(recipe_list[id][0]['steps'])):
        curr_step = recipe_list[id][0]['steps'][idx]['step']
        steps_of_recipe.append({"number": idx + 1, "step": curr_step})

    return steps_of_recipe
