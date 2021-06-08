from flask import Flask, render_template
from utils import *


app = Flask("Portfolio")

@app.route("/")
def index():
    data = get_pics()
    return render_template("index.html",
        pics=data[0],
        years=data[1]
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")