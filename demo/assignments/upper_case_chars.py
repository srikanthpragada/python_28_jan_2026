
def get_upper_case(*names):
    upper_chars = []
    for name in names:
        for c in name:
            if c.isupper():
                upper_chars.append(c)

    return "".join(upper_chars)


print(get_upper_case('Joe', 'Mark', 'Bob Tabour'))