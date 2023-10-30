from flask import Flask, request, render_template

from mft.controller.stuff_controller import StuffController

app = Flask(__name__, template_folder="mft/view")


@app.route("/")
def home():
    return render_template("stuff.html")


@app.route("/stuff", methods=["POST"])
def stuff_view():
    controller = StuffController()
    controller.save(
        request.form.get("name"),
        request.form.get("brand"),
        request.form.get("description"),
        request.form.get("price"),
        None,
        # request.form.get("image"),
        request.form.get("rent_condition"),
        request.form.get("rent_price")
    )
    return render_template("stuff.html")


app.run(host="192.168.39.100", port=80)
