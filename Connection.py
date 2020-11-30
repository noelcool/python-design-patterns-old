import pymysql, copy


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
            print("새로운 인스턴스 생성")
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    def __init__(self):
        self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='company', charset='utf8mb4')
        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def execute(self, query, args={}):
        self.cursor.execute(query, args)


if __name__ == '__main__':
    DataBase()
    d1 = DataBase().connection
    c1 = DataBase().cursor
    d2 = DataBase().connection
    c2 = DataBase().cursor
    #print(d1, d2)
    #print(c1, c2)
    c2.execute("SELECT * FROM products")

    #result = c2.fetchall()
    old = c2.fetchall()
    #new = old[:]
    new = copy.deepcopy(old[:])

    print("ori ", id(old), id(new))
    print(old is new)
    new[0]['id'] = 99
    print(old)
    print(new)

