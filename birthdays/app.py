import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    birthdays = db.execute("SELECT * FROM birthdays")
    if request.method == "POST":
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")

        print(name)
        print(month)
        print(day)
        # TODO: Add the user's entry into the database
        months30 = ['4', '6', '9', '11'];
        if (month == '2' and int(day) > 29) or (month in months30 and int(day) > 30):
            return (render_template("index.html", birthdays=birthdays, errmsg="Invalid date entered"))
        else:
            db.execute("INSERT INTO birthdays ('name', 'month', 'day') VALUES (?, ?, ?)", name, month, day)
            return redirect("/")

    else:
        # TODO: Display the entries in the database on index.html
        return render_template("index.html", birthdays=birthdays)

@app.route("/del", methods=["POST"])
def delete():
    birthdays = db.execute("SELECT * FROM birthdays")
    id = request.form.get("id")
    matchedid = db.execute("SELECT * FROM birthdays WHERE id = ?", id)
    print(matchedid)
    if matchedid:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
        return redirect("/")
    else:
        return render_template("index.html", birthdays=birthdays, errmsg="Error deleting: birthday does not exist.")
