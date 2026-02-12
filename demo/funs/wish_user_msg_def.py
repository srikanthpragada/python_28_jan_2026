def wish(user='Guest', message='Hello'):
    print(message, user)


# Positional
wish('Mark')
wish('Scott', 'Hi')
wish()

# Keyword or named arguments
wish(message='Good Morning', user='Tom')
wish(user='Tom')
wish(message='Hi')
