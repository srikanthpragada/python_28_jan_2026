def wish(*users, message = 'Hello'):
    for u in users:
        print(message,u)


wish('Andy', 'Bob', 'Gary')
wish('Mark', 'Jack', message = 'Hi')
wish()

