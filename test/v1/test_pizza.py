import src.v1.pizza as p
import pytest

def test_pizza_invalid_crust():
    with pytest.raises(AttributeError):
        p.make_pizza('strudle')

def test_pizza_invalid_topping_paper():
    with pytest.raises(AttributeError):
        pizza = p.make_pizza('thin')
        pizza.add_topping('paper')

def test_pizza_is_veggetarian_simple_crust():
    pizza = p.make_pizza('deepdish')
    assert(p.is_veggetarian(pizza))
    assert(p.calculate_price() == 8.0)

def test_pizza_is_veggetarian_simple_crust():
    pizza = p.make_pizza('deepdish')
    p.add_topping(pizza, 'black_olive')
    p.add_topping(pizza, 'cheese')
    assert(p.is_veggetarian(pizza))

def test_pizza_cost_cheese():
    # change src.pizza so this test passes
    pizza = p.make_pizza('hand_tossed')
    p.add_topping(pizza, 'cheese')
    assert(p.calculate_price(pizza) == 9.0)

def test_pizza_cost_stuffed_special():
    # change src.pizza so this test passes
    pizza = p.make_pizza('stuffed')
    p.add_topping(pizza, 'cheese')
    p.add_topping(pizza, 'pepperoni')
    p.add_topping(pizza, 'cheese')
    assert(not p.is_veggetarian(pizza))
    assert(p.calculate_price(pizza) == 14.0)

def test_pizza_remove_toppings():
    # change src.pizza so this test passes
    pizza = p.make_pizza('stuffed')
    p.add_topping(pizza, 'pepperoni')
    p.add_topping(pizza, 'pepperoni')
    p.add_topping(pizza, 'cheese')
    p.remove_topping(pizza, 'pepperoni')
    assert(p.is_veggetarian(pizza))
    assert(p.calculate_price(pizza) == 9.0)

def test_pizza_is_dairy_free_cheese():
    # change src.pizza so this test passes
    pizza = p.make_pizza('stuffed')
    p.add_topping(pizza, 'cheese')
    p.add_topping(pizza, 'pepperoni')
    assert(not p.is_dairy_free(pizza))

def test_pizza_is_dairy_free_cheeseless():
    # change src.pizza so this test passes
    pizza = p.make_pizza('stuffed')
    p.add_topping(pizza, 'pepperoni')
    assert(p.is_dairy_free(pizza))
