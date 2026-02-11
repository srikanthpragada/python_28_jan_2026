names = ['Anders', 'Tom','Mark', 'Jack', 'Jason']

uchars = set()
for name in names:
    uchars = uchars | set(name)

print(uchars)

