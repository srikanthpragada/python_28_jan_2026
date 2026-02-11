
s = "how do you do"
cf = {}  # Empty dict

for c in s:
    if c not in cf:
       cf[c] = s.count(c)

print(cf)

