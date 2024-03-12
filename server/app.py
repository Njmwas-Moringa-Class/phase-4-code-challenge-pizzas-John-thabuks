#!/usr/bin/env python3

from flask import Flask, request, jsonify
from flask_migrate import Migrate
from models import db, Restaurant, RestaurantPizza, Pizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)


# GET /restaurants
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = db.session.query(Restaurant).all()
    return jsonify([restaurant.to_dict() for restaurant in restaurants]), 200


@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant_by_id(id):
    restaurant = db.session.query(Restaurant).get(id)
    if restaurant:
        return jsonify(restaurant.to_dict(include_pizzas=True)), 200
    else:
        return jsonify({"error": "Restaurant not found"}), 404


@app.route('/')
def index():
    return '<h1>Code challenge</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
