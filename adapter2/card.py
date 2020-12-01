import abc


class Card:
    def __init__(self):
        self.__card_id = "card.card_id"
        self.__card_name = "card_name"
        self.__card_company = "card_company"

    @property
    def card_id(self):
        return self.__card_id

    @card_id.setter
    def card_id(self, value):
        self.__card_id = value

    @property
    def card_name(self):
        return self.__card_name

    @card_name.setter
    def card_name(self, value):
        self.__card_name = value

    @property
    def card_company(self):
        return self.__card_company

    @card_company.setter
    def card_company(self, value):
        self.__card_company = value

    def print_card(self):
        print("card : {}, {}, {}".format(self.__card_id, self.__card_name, self.__card_company))


