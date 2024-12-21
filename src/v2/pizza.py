class Pizza():
    def __init__(self, base_pizza=None):
        self.base = base_pizza
    def is_veggetarian(self):
        pass
    def calculate_price(self):
        pass
    def remove_topping(self, pizza_class):
        if isinstance(self, pizza_class):
            return self.base.remove_topping(pizza_class) if self.base else self
        elif self.base:
            self.base = self.base.remove_topping(pizza_class)
        return self