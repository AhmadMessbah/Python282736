from mft.controller.stuff_controller import StuffController

controller = StuffController()
# print(controller.save("mobile", "samsung1111", "description", 1000, "image", "rent_condition", 100))
# print(controller.edit(2, "laptop", "samsung", "description", 1000, "image", "rent_condition", 100))
# print(controller.remove(2))
print(controller.find_all())

