import pymysql, copy


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
            print('새로운 인스턴스 생성')
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    def __init__(self):
        self.__host = '127.0.0.1'
        self.__port = 3306
        self.__user = 'root'
        self.__password = '123456'
        self.__db_name = 'company'

    @property
    def host(self):
        return self.__host

    @host.setter
    def host(self, value):
        self.__host = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value

    def connection(self):
        conn = pymysql.connect(host=self.__host, port=self.__port, user='root', password=self.__password,
                               db=self.__db_name, charset='utf8mb4')
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return cursor


class Execute:
    @staticmethod
    def select(cursor, query, args={}):
        cursor.execute(query, args)


if __name__ == '__main__':
    d = DataBase()
    d.host = 'localhost'
    d.password = '123456'
    print(d.host)
    d1 = d.connection()

    execute = Execute()
    execute.select(d1, "SELECT * FROM products")
    
    old = d1.fetchall()
    new = copy.deepcopy(old[:])
    new[0]['id'] = 99
    print(old, new)
