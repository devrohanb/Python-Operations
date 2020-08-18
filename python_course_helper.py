import sqlite3 as lite

# TODO: functionality goes here :


class DatabaseManage(object):
    def __init__(self):
        global con
        try:
            con = lite.connect("courses.db")
            with con:
                cur = con.cursor()
                cur.execute(
                    "CREATE TABLE IF NOT EXIST course(Id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, description TEXT, price TEXT, is_private BOOLEAN NOT NULL DEFAULT 1)")
        except Exception:
            print("Unable to connect to database !!")

    # TODO: Create data
    def insert_data(self, data):
        try:
            with con:
                cur = con.cursor()
                cur.execute(
                    "INSERT INTO course(name, description, price, is_private) VALUES(?,?,?,?)", data)
                return True
        except Exception:
            print("Error : Unable to insert data !!")

    # TODO: read data
    def fetch_data(self):
        try:
            with con:
                cur = con.cursor()
                cur.execute("SELECT * FROM course")
                return cur.fetchall()
        except Exception:
            print("Error : Unable to fetch data !! ")

    # TODO: delete data
    def delete_data(self, id):
        try:
            with con:
                cur = con.cursor()
                sql = "DELETE FROM course WHERE id = ?"
                cur.execute(sql, [id])
        except Exception:
            print("Error : Unable to delete data !!")

# TODO: Interface goes here :
# TODO: Here main() is like any other method/ function but not like __main__
    def main(self):
        print("* \n" * 40)
