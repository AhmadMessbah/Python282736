from mft.controller.stuff_controller import StuffController

controller = StuffController()
# print(controller.save("mobile", "samsung1111", "description", 1000, "image", "rent_condition", 100))
# print(controller.edit(2, "laptop", "samsung", "description", 1000, "image", "rent_condition", 100))
# print(controller.remove(2))
print(controller.find_all())

# from flask import Flask,request,render_template
#
# app = Flask(__name__, template_folder="mft/view")
#
# @app.route("/stuff", methods=["GET","POST"])
# def stuff_view():
#     controller = StuffController()
#     if request.method == "GET":
#         return render_template("stuff.html")
#     elif request.method =="POST":
#         controller.save(
#             request.form.get("name"),
#             request.form.get("brand"),
#             request.form.get("description"),
#             request.form.get("price"),
#             request.form.get("image"),
#             request.form.get("rent_condition"),
#             request.form.get("rent_price")
#             )
#
#
#
#
# app.run(host="192.168.39.100", port=80)
