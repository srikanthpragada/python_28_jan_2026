
s = "how do you do"

cf = {}  # Empty dict

for c in sorted(set(s)):
    cf[c] = s.count(c)

print(cf)

