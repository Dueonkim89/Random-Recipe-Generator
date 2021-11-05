from flask import Flask, render_template, request, url_for, flash, redirect
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/selection", methods=["GET", "POST"])
def selection():
    if request.method == "POST":
        number = request.form.get("select_number_of_countries")
        print("******************** number is: ", number)
        # make request to microservice, requires a parameter of numbers at the end
        # https://stackoverflow.com/questions/15463004/how-can-i-send-a-get-request-from-my-flask-app-to-another-site
        micro_service_url = 'https://malliuxservice.herokuapp.com/countries/'
        return(number)
    else:
        return render_template('selection.html')
