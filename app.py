from flask import Flask
from flask import render_template
from random import choices

app = Flask(__name__)


def rollthedice():
    options = [1, 2, 3, 4, 5, 6]
    return choices(options)


@app.route("/")
def roll():
    mynumber = rollthedice()
    return render_template("index.html", title="Roll the Dice", number=mynumber)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="8080", debug=True)
