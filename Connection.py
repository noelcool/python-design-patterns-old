import pymysql


class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class DataBase(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', db='company',
                                              charset='utf8mb4')
            self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)
        return self.cursor


if __name__ == '__main__':
    DataBase()
    d1 = DataBase().connect()
    d2 = DataBase().connect()
    print(DataBase(), DataBase())