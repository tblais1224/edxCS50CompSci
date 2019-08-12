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
    payload = []
    payload.append(request.form.get("title"))
    payload.append(request.form.get("system"))
    payload.append(request.form.get("gridRadios"))
    payload.append(request.form.get("played"))
    myData = []
    with open('survey.csv', 'r') as readFile:
        reader = csv.reader(readFile)
        for row in reader:
            print(row)
            myData.append(row)
    myData.append(payload)
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
