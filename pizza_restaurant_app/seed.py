from random import randint, choice
from models import db, Restaurant, Pizza, Price, Ingredient
from app import app

restaurants = [
    {"name": "Dominion Pizza", "address": "Address 1"},
    {"name": "Pizza Hut", "address": "Address 2"}
]

with app.app_context():
    Restaurant.query.delete()
    db.session.commit()
    
with app.app_context():
    print('🍕 Obtaining Restaurants')
    for restaurant in restaurants:
        existing_restaurant = Restaurant.query.filter_by(name=restaurant["name"]).first()
        if existing_restaurant is None:
            new_restaurant = Restaurant(name=restaurant["name"], address=restaurant["address"])
            db.session.add(new_restaurant)
            db.session.commit()

pizzas = [
    {"name": "Cheese"},
    {"name": "Pepperoni"}
]

with app.app_context():
    print('🍕 Odering Pizza')
    for pizza in pizzas:
        new_pizza = Pizza(name=pizza["name"])
        db.session.add(new_pizza)
        db.session.commit()

ingredients = [
    {"ingredient": "Dough", "pizza": "Cheese"},
    {"ingredient": "Tomato Sauce", "pizza": "Cheese"},
    {"ingredient": "Cheese", "pizza": "Cheese"},
    {"ingredient": "Dough", "pizza": "Pepperoni"},
    {"ingredient": "Tomato Sauce", "pizza": "Pepperoni"},
    {"ingredient": "Cheese", "pizza": "Pepperoni"},
    {"ingredient": "Pepperoni", "pizza": "Pepperoni"}
]

with app.app_context():
    print('🍕 Placing Toppings on Pizzas')
    for ingredient in ingredients:
        pizza = Pizza.query.filter_by(name=ingredient["pizza"]).first()
        if pizza is not None:
            new_ingredient = Ingredient(name=ingredient["ingredient"], pizza_id=pizza.id)
            db.session.add(new_ingredient)
            db.session.commit()

prices = [
    {"price": 5, "pizza": "Cheese"},
    {"price": 10, "pizza": "Pepperoni"}
]

with app.app_context():
    print('🍕 Obtaining Price')
    for price in prices:
        pizza = Pizza.query.filter_by(name=price["pizza"]).first()
        if pizza is not None:
            new_price = Price(value=price["price"], pizza_id=pizza.id)
            db.session.add(new_price)
            db.session.commit()
           
print("🍕 Your Pizza is on the way!")
