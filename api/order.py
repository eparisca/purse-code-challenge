import re
import api.date_parser
import api.db


def validate_order_number(order_number):
    pattern = re.compile(r"^\d{3}-\d{7}-\d{7}$")
    try:
        if pattern.match(order_number).group() != order_number:
            raise ValueError
    except AttributeError:
        raise ValueError


def create_order_model(order_number, date_string):
    validate_order_number(order_number)
    dates = api.date_parser.parse_date_string(date_string)
    end_date = dates[0]
    return {
        "order": order_number,
        "delivery": api.date_parser.format_date_as_iso8601(end_date)
    }


def persist_order_model(order_model):
    api.db.persist_order(order_model)


def get_all_orders():
    return api.db.get_all_orders()


def get_order(order_number):
    row = api.db.get_order(order_number)
    return {
        "order": row["order"],
        "delivery": api.date_parser.format_date_as_iso8601(row["delivery"])
    }
