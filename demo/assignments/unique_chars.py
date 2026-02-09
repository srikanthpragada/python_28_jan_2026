
names = ['Scott', 'Tom', 'Jackson', 'Anders', 'Bob']

uchars = []

for name in names:
    for c in name:
        if c not in uchars:
            uchars.append(c)

print(uchars)
