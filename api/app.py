import flask
from flask import Flask, render_template, request
import api.order

app = Flask(__name__)


@app.route('/')
def display_form():
    return render_template('orders.html')


@app.route('/api/1.0/orders', methods=["POST"])
def create_order():
    data = request.get_json(force=True)
    model = api.order.create_order_model(data["orderNumber"], data["estimatedDelivery"])
    api.order.persist_order_model(model)
    return model


@app.route('/api/1.0/orders', methods=["GET"])
def get_orders():
    return api.order.get_all_orders()


@app.route('/api/1.0/orders/<order_number>', methods=["GET"])
def get_order(order_number):
    model = api.order.get_order(order_number)
    if model is None:
        flask.abort(404)
    app.logger.info(model)
    return model


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
