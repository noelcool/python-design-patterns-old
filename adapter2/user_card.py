class UserCardAdapter:
    def __init__(self, user, card):
        self.user = user
        self.card = card

    def print_user(self):
        self.user.print_user()

    def print_card(self):
        self.card.print_card()

    def print_user_and_card(self):
        self.card.print_card()
        self.user.print_user()
