import mysql.connector as mysql


def check_change_user(firstname_new, lastname_new):
    db = mysql.connect(host="127.0.0.1",
                       port="3307",
                       user="root",
                       password="",
                       database='litecart')

    cursor = db.cursor()

    cursor.execute("SELECT firstname, lastname "
                   "FROM lc_customers WHERE id=3")
    customers = cursor.fetchall()
    assert customers[0] == (firstname_new, lastname_new)
