# Import flask and template operators
from flask import Flask, render_template, request, json
import requests

# Could import flask extensions, such as SQLAlchemy, here
# from flask.ext.sqlalchemy import SQLAlchemy

# Define WSGI object
app = Flask(__name__)
app.config['TESTING'] = True

# Configurations
app.config.from_object('config')


# Some more example SQLAlchemy config
# Define the database object which is imported by modules and controllers
# db = SQLAlchemy(app)

# HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route("/name", methods=['POST'])
def name():
    try:
        r = requests.get("http://127.0.0.1:5000/api/v1/search/" + request.form['name'])
        if (r.status_code == 200):
            result = r.json()
            if (result['error'] == True):
                return render_template("home.html", error="Aucun résultat n'a été trouvée, veuillez essayer avec des mots clés en anglais")
            return render_template("result.html", result=result)
        else:
            return render_template("home.html", error="L'API a rencontrée une erreur")
    except:
        return render_template("home.html", error="L'API n'est pas disponible")

@app.route("/random", methods=['POST'])
def random():
    try:
        r = requests.get("http://127.0.0.1:5000/api/v1/random")
        if (r.status_code == 200):
            result = r.json()
            return render_template("result.html", result=result)
        else:
            return render_template("home.html", error="L'API a rencontrée une erreur")
    except:
        return render_template("home.html", error="L'API n'est pas disponible")
# Home page view
@app.route('/',  methods=['GET', 'POST'])
def home():
    return render_template('home.html')