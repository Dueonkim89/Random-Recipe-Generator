from flask import Flask, render_template, request, url_for, flash, redirect
import requests
from utils import decode_to_string, get_countries_from_string

app = Flask(__name__)

# Global variables to cache user choice
cache = {}
chosen_country = None
cached_recipe_list_per_country = {}
cached_recipes = {}

spoonacular_api_key = "81bd5951a8ee44bc9d54fbb1858704b0"
countries_in_spoonacular = {'French', 'Thai', 'Italian', 'Indian', 'Spanish', 'Greek', 'Mexican'}
countries_in_all_recipes = {'Turkey', 'Argentina', 'Portgual'}

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/selection", methods=["GET", "POST"])
def selection():
    if request.method == "POST":
        number = request.form.get("select_number_of_countries")
        # make request to microservice, requires a parameter of numbers at the end
        # https://stackoverflow.com/questions/15463004/how-can-i-send-a-get-request-from-my-flask-app-to-another-site
        micro_service_url = 'https://malliuxservice.herokuapp.com/countries/'
        micro_service_url += number
        r = requests.get(micro_service_url)
        data = decode_to_string(r.content)
        arr_of_countries = get_countries_from_string(data)
        # render html based on number of countries in arr_of_countries
        return render_template('country_list.html', countries=arr_of_countries)
    else:
        return render_template('selection.html')


@app.route("/recipes_for_country", methods=["GET", "POST"])
def find_recipe():
    # POST route
    if request.method == "POST":
        # parse JSON
        data = request.json
        country = data['country']
        global chosen_country
        chosen_country = country
    
        # make request to spoonacular API and get all recipes
        if country in countries_in_spoonacular:
            # if in cache, pass info from cache into HTML template
            if country in cached_recipe_list_per_country:
                print("LINE 52")
                print(cached_recipe_list_per_country[country]['results'])
                return render_template('country_recipes.html', country=country)
            else:
                # make API call to spoonacular    
                base_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey="
                base_url += spoonacular_api_key
                base_url += '&cuisine='
                base_url += country
                response = requests.get(base_url)

                # store data into global cache, to avoid repetitive API calls
                cached_recipe_list_per_country[country] = response.json()

                # gather recipe data and redirect to country_recipes.html
                print("LINE 67")
                print(cached_recipe_list_per_country[country]['results'])
                return render_template('country_recipes.html', country=country)

        # else, scrap data from website all_recipes and get all recipes
        
    # GET request, send recipe list from cached country


# route to get specific recipe instruction
        
