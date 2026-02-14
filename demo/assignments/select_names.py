names = ['George Micheal', 'Micheal Jackson', 'Madonna', 'Ritchie', 'Bruise Springsteen']


def hasspace(st):
    return st.find(' ') >= 0


for name in filter(hasspace, names):
    print(name)
