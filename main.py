import requests
from flask import Flask, render_template



app = Flask(__name__)
@app.route("/")
def page():
    return "<h1>Hello there<h2>"
@app.route("/guess/<name>")
def guess(name):
    genderize_url = f"https://api.genderize.io?name={name}"
    gender_r = requests.get(genderize_url)
    gender_json = gender_r.json()
    gender = gender_json["gender"]
    agify_url = f"https://api.agify.io?name={name}"
    age_r = requests.get(agify_url)
    age_data = age_r.json()
    age = age_data["age"]
    return render_template("guess.html", name = name, gender = gender, age= age)



if __name__ == '__main__':
    app.run(debug=True)


