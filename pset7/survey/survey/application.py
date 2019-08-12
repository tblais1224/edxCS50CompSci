import cs50
import csv

from flask import Flask, jsonify, redirect, render_template, request

# Configure application
app = Flask(__name__)

# Reload templates when they are changed
app.config["TEMPLATES_AUTO_RELOAD"] = True


@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET"])
def get_index():
    return redirect("/form")


@app.route("/form", methods=["GET"])
def get_form():
    return render_template("form.html")


@app.route("/form", methods=["POST"])
def post_form():
    title = request.form.get("title")
    system = request.form.get("system")
    radios = request.form.get("gridRadios")
    played = request.form.get("played")

    with open('survey.csv', 'r') as readFile:
        reader = csv.reader(readFile)
    for row in reader:
        print(row)
    myData = [[1, 2, 3], ['Good Morning', 'Good Evening', 'Good Afternoon']]
    myFile = open('survey.csv', 'w')
    with myFile:
        writer = csv.writer(myFile)
        writer.writerows(myData)
        
    readFile.close()
    myFile.close()
    return render_template("sheet.html")


@app.route("/sheet", methods=["GET"])
def get_sheet():
    return render_template("sheet.html")
