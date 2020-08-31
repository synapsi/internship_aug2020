products = [
    {"name": "Prod1", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod2", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod3", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod4", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod5", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod6", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod7", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod8", "amount": {"min": 10000, "max": 99999}, "price": {"min": 1, "max": 100}},
    {"name": "Prod9", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
    {"name": "Prod10", "amount": {"min": 10000, "max": 99999}, "price": {"min": 0, "max": 100}},
]
obj_list = []


class ParentProduct:
    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(f"Name of this product is {self.name}")
