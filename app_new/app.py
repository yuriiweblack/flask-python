from flask import Flask, render_template, request,redirect

app = Flask(__name__)

REGISTRANTS = {}

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def register():
    # global REGISTRANTS
    name = request.form['name']
    sport = request.form['sport']
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