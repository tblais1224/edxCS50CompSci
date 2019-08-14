import os

import requests
from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    user_id = session["user_id"]
    portfolios = db.execute(
        "SELECT * FROM portfolio WHERE user_id = %s", user_id)

    payload = []

    api_key = os.environ.get("API_KEY")
    for portfolio in portfolios:
        data = []
        data.append(portfolio["symbol"])
        data.append(portfolio["name"])
        data.append(portfolio["shares"])
        print(portfolio["symbol"])
        if portfolio["symbol"] == "CASH":
            data.append("x")
            data.append(portfolio["total"])
        else:
                    # "https://cloud-sse.iexapis.com//stable/stock/nflx/quote?token=pk_c68c80959746417aa4e351e5eb5cdb0d"
            api = requests.get("https://cloud-sse.iexapis.com/stable/stock/" + portfolio["symbol"] + "/quote?token=" + api_key + "").json()
            price = api["latestPrice"]
            data.append(price)
            total = price * portfolio["shares"]
            data.append(total)
        payload.append(data)
    net_total = 0.00
    for x in payload:
        net_total = net_total + x[4]

    return render_template("portfolio.html", data=payload, net_total=net_total)


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():  
    if request.method == "GET":
        return render_template("quote.html", data='GET')
    elif request.method == "POST":
        api_key = os.environ.get("API_KEY")
        api = requests.get("https://cloud-sse.iexapis.com/stable/stock/" + request.form.get("symbol") + "/quote?token=" + api_key + "").json()
        price = api["latestPrice"]
        name = api["companyName"]
        symbol = api["symbol"]
        payload = "A share of " + name + "(" + symbol + ") costs $" + str(price)
        return render_template("quote.html", data=payload)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    if request.method == "GET":
        return render_template("buy.html", data='GET')
    elif request.method == "POST":
        user_id = session["user_id"]
        portfolios = db.execute("SELECT * FROM portfolio WHERE user_id = %s", user_id)
        cash = 0.00
        cash_id = 0
        for x in portfolios:
            if x["symbol"] == "CASH":
                cash = x["total"]
                cash_id = x["id"]
        api_key = os.environ.get("API_KEY")
        api = requests.get("https://cloud-sse.iexapis.com/stable/stock/" + request.form.get("symbol") + "/quote?token=" + api_key + "").json()
        price = api["latestPrice"]
        name = api["companyName"]
        symbol = api["symbol"]
        shares = int(request.form.get("shares"))
        # print(type(shares), type(price), type(cash))
        cost = shares * price
        print(cash, cost)
        if cash < cost:
            return apology("Insufficient funds!")
        cash = cash - cost
        sql_command_buy = "INSERT INTO portfolio (user_id, symbol, name, shares) VALUES (%s, %s, %s, %s)"
        val = (user_id, symbol, name, shares)
        db.execute(sql_command_buy, val)
        sql_command_cash = "INSERT INTO portfolio WHERE user_id = %s (total) VALUES (%s, %s)"
        val2 = (cash_id, cash)
        db.execute(sql_command_cash, val2)
        return index()


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")

        # Ensure username was submitted
        if not username:
            return apology("must provide username", 403)
        # Ensure password was submitted
        elif not password:
            return apology("must provide password", 403)
        # Ensure password was submitted
        elif password != password2:
            return apology("Password and confirm password must be the same", 403)

        # Query database for username
        rows = db.execute(
            "SELECT username FROM users WHERE username = %s", username)
        # Ensure username doesnt exist
        if len(rows) > 0:
            return apology("this username exists", 403)

        hashed_password = generate_password_hash(
            password, method='pbkdf2:sha256', salt_length=8)

        # create user in db
        sql_command_register = "INSERT INTO users (username, hash) VALUES (%s, %s)"
        val = (username, hashed_password)
        db.execute(sql_command_register, val)
        user_id = db.execute(
            "SELECT id FROM users WHERE username = %s", username)[0]["id"]
        # add 10000 cash to user portfolio
        sql_command_portfolio = "INSERT INTO portfolio (user_id, symbol, name, shares, total) VALUES (%s, %s, %s, %s, %s)"
        values = (user_id, "CASH", "United States Dollar", "0", "10000.00")
        db.execute(sql_command_portfolio, values)
        return render_template("login.html")
    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")


def errorhandler(e):
    """Handle error"""
    if not isinstance(e, HTTPException):
        e = InternalServerError()
    return apology(e.name, e.code)


# Listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
