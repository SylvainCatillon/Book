from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    projects = [
        {
        "title": "PlanniTeam",
        "subtitle": "Application Django - Projet libre",
        "tag": "planniteam",
        "btn_img": url_for('static', filename='img/PlanniTeam.jpg'),
        "content_img": url_for('static', filename='img/planniteam.jpg')
        },
        {
        "title": "Pur Beurre",
        "subtitle": "Application Django - Projet suivant un cahier des charges",
        "tag": "purbeurre",
        "btn_img": url_for('static', filename='img/purbeurre.jpg'),
        "content_img": url_for('static', filename='img/charte.jpg')
        },
        {
        "title": "GrandPy Bot",
        "subtitle": "Application Flask - Projet avec API",
        "tag": "grandpy",
        "btn_img": url_for('static', filename='img/grandpy.jpg'),
        "content_img": url_for('static', filename='img/slide_grandpy.jpg')
        },
        {
        "title": "OCPizza",
        "subtitle": "Spécifications fonctionelles et techniques",
        "tag": "ocpizza",
        "btn_img": url_for('static', filename='img/ocpizza.jpg'),
        "content_img": url_for('static', filename='img/ocpizza.jpg')
        }
    ]
    return render_template('index.html', projects=projects)

if __name__ == "__main__":
    app.run()
