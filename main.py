from flask import Flask, render_template
from utils import *


app = Flask("Portfolio")

@app.route("/")
def index():
    return render_template("index.html",
        pics=get_pics(),
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")