import cs50
import csv
from prettytable import PrettyTable

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
    csv_file = open('survey.csv', 'r')
    csv_file = csv_file.readlines()
    line_1 = csv_file[0]
    line_1 = line_1.split(',')
    line_2 = csv_file[1]
    line_2 = line_2.split(',')
    x = PrettyTable(line_1[0],line_2[0])
    for a in range(1, len(line_1)):
        x.add_row([line_1[a],line_2[a]])
    html_code = x.get_html_string()
    print(html_code)
    html_file = open('sheet.html','w')
    html_file = html_file.write(html_code)
    html_file.close()
    return render_template("sheet.html")

