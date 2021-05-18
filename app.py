from flask import Flask, render_template

app = Flask(__name__)

<<<<<<< HEAD
username = "John"    # Put your name here. Change message to use your name


@app.route("/", methods=["GET"])
def firstRoute():
    return render_template("index.html", message="Earthling")
=======
# Routes at present only handling http GETs


@app.route("/", methods=["GET"])
def redirect_get():
    if request.method == "GET":
        return render_template(
            "index.html", title="books", books=books
        )


@app.route("/books", methods=["GET"])
def book():
    if request.method == "POST":  # just send user back to index template
        return render_template(
            "index.html", title="books", books=books
        )
    elif request.method == "GET":
        return jsonify(books)
    else:
        return 400  # Bad Request Response
>>>>>>> 4ca1d7c27843bdf1372cf469c632a6b3f4846c6c


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
