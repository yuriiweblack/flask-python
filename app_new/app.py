from flask import Flask, render_template, request,redirect

app = Flask(__name__)

REGISTRANTS = {}

SPORTS = [
    "Basketball",
    "Football",
    "Сhess",
    "Tennis"
]

@app.route('/')
def index():
    return render_template("index.html", sports=SPORTS )


@app.route("/register", methods=["POST"])
def register():
    # global REGISTRANTS
    name = request.form['name']
    if not name:
        return render_template("failure.html")
    sport = request.form['sport']
    if sport not in SPORTS:
        return render_template("failure.html")
    REGISTRANTS[name] = sport

    # print(name, sport)

    print(REGISTRANTS)
    return render_template("success.html")


@app.route("/registrants")
def registrants():
    return render_template("registrants.html", registrants=REGISTRANTS)

# print(REGISTRANTS)

if __name__ == '__main__':
    app.run(debug=True)