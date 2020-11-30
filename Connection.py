import pymysql


class MetaSingleton(type):
    _instances = {}

    def __cal__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    connection = None
    cursor = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='company',
                                              charset='utf8mb4')
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        return self.cursor


db1 = DataBase().connect()
print(db1)
db2 = DataBase().connect()
db3 = DataBase().connect()
db4 = DataBase().connect()
print(db2)
print(db3)
print(db4)

q = "select * from products"
db1.execute(q)
rows = db1.fetchall()
print(rows)


