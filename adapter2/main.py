from adapter2.user import User
from adapter2.card import Card
from adapter2.user_card import UserCardAdapter

if __name__ == '__main__':
    user = User()
    card = Card()

    adapter = UserCardAdapter(user, card)

    #printer.print_user()
    #printer.print_card()
    adapter.print_user_and_card()
