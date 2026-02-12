def find_upper(st):
    for i, c in enumerate(st):
        if c.isupper():
            return i

    return -1  # no uppercase found


print(find_upper('AbC'))
print(find_upper('abc'))
