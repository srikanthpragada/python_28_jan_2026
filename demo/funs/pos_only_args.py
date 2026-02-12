#  Positional-only args
def wish(user, message, /):
    print(message, user)

wish('Mark', 'Hi')
#wish(message = 'Hi', user = 'Steve')