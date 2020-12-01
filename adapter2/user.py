class User:
    def __init__(self):
        self.__user_id = "user_id"
        self.__user_name = "user_name"
        self.__card_id = "user.card_id"

    @property
    def user_id(self):
        return self.__user_id

    @user_id.setter
    def user_id(self, value):
        self.__user_id = value

    @property
    def name(self):
        return self.__user_name

    @name.setter
    def name(self, value):
        self.__user_name = value

    @property
    def card_id(self):
        return self.__card_id

    @card_id.setter
    def card_id(self, value):
        self.__card_id = value

    def print_user(self):
        print("user : {}, {}, {}".format(self.__user_id, self.__user_name, self.card_id))