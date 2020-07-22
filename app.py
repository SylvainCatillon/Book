from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    projects = [
        {
        "title": "PlanniTeam",
        "subtitle": "Application Django - Projet libre",
        "tag": "planniteam",
        "img": url_for('static', filename='img/PlanniTeam.jpg')
        },
        {
        "title": "Pur Beurre",
        "subtitle": "Application Django - Projet suivant un cahier des charges",
        "tag": "purbeurre",
        "img": url_for('static', filename='img/purbeurre.jpg')
        },
        {
        "title": "GrandPy Bot",
        "subtitle": "Application Flask - Projet avec API",
        "tag": "grandpy",
        "img": url_for('static', filename='img/grandpy.jpg')
        },
        {
        "title": "OCPizza",
        "subtitle": "Spécifications fonctionelles et techniques",
        "tag": "ocpizza",
        "img": url_for('static', filename='img/ocpizza.jpg')
        }
    ]
    return render_template('index.html', projects=projects)
