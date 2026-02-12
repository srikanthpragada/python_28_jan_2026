# Keyword-only args
def wish(*, message, user):
    print(message, user)

#wish('Mark', 'Hi')
wish(message = 'Hi', user = 'Steve')