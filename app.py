from flask import Flask, render_template, request, url_for, flash, redirect
import requests
from utils import decode_to_string, get_countries_from_string

app = Flask(__name__)
cache = None

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
