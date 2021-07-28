import psycopg2
import psycopg2.extras


def connect():
    conn = psycopg2.connect("dbname='purse' user='dbuser' host='purse-db' password='fakePass'")
    return conn


def persist_order(model):
    conn = connect()
    cur = conn.cursor()
    cur.execute("""INSERT INTO orders ("order", delivery) VALUES (%s, %s)""", (model["order"], model["delivery"]))


def get_all_orders():
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""SELECT * from orders""")
    rows = cur.fetchall()
    return rows


def get_order(order_number):
    conn = connect()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("""SELECT * from orders WHERE "order" = %s""", (order_number, ))
    row = cur.fetchone()
    return row
