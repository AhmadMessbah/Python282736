from mft.controller.stuff_controller import StuffController

controller = StuffController()
print(controller.save("mobile", "samsung", "description", 1000, "image", "rent_condition", 100))
# print(controller.edit(2, "laptop", "samsung", "description", 1000, "image", "rent_condition", 100))
# print(controller.remove(2))
for st in controller.find_all():
    print(st.__dict__)

