from src.v2.pizza import Pizza

class ThinCrust(Pizza):
    def is_veggetarian(self):
        return True
    def is_dairy_free(self):
        return True
    def calculate_price(self):
        return 8.0