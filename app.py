from flask import Flask, render_template, request, url_for, flash, redirect
import requests
from utils import decode_to_string, get_countries_from_string

app = Flask(__name__)

# Global variables to cache user choice
cached_countries = None
chosen_country = None
cached_recipe_list_per_country = {}
cached_recipes = {}

# api key
spoonacular_api_key = "81bd5951a8ee44bc9d54fbb1858704b0"

country_search_word = {'France': 'French', 'Thailand': 'Thai', 'Italy': 'Italian', 
'India': 'Indian', 'Spain': 'Spanish', "Greece": 'Greek', 'Mexico': 'Mexican', 
'Turkey': 'Middle+Eastern', 'Argentina': 'Latin+American', 'Portugal': 'Mediterranean'}

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
        global cached_countries
        cached_countries = get_countries_from_string(data)
        # render html based on number of countries in arr_of_countries
        return render_template('country_list.html', countries=cached_countries)
    else:
        return render_template('selection.html')


@app.route("/country_list")
def country_list():
    return render_template('country_list.html', countries=cached_countries)


@app.route("/recipes_for_country", methods=["GET", "POST"])
def find_recipe():
    # POST route
    if request.method == "POST":
        country = country_search_word[request.form.get("countryRadios")]
        global chosen_country
        chosen_country = country
    
        # if in cache, pass info from cache into HTML template
        if country in cached_recipe_list_per_country:
            return render_template('country_recipes.html', country=request.form.get("countryRadios"), recipes=cached_recipe_list_per_country[country]['results'])
        else:
             # make request to spoonacular API and get all recipes
            base_url = "https://api.spoonacular.com/recipes/complexSearch?apiKey="
            base_url += spoonacular_api_key
            base_url += '&cuisine='
            base_url += country
            response = requests.get(base_url)

            # store data into global cache, to avoid repetitive API calls
            cached_recipe_list_per_country[country] = response.json()

            # gather recipe data and redirect to country_recipes.html
            return render_template('country_recipes.html', country=request.form.get("countryRadios"), recipes=cached_recipe_list_per_country[country]['results'])

    # GET request, send recipe list from cached country
        

# route to get specific recipe instruction
        
