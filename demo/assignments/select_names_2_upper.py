names = ['George Micheal', 'BEATTLES', 'Micheal Jackson', 'Madonna', 'Ritchie', 'Bruise Springsteen']

def has2upper(st):
    count = 0
    for c in st:
        if c.isupper():
             count += 1

    return count >= 2


for name in filter(has2upper, names):
    print(name)
