import re

with  open("softstory.txt", "rt") as f:
    story = f.read()

words = re.findall(r'[a-zA-Z_]+', story)

for w in sorted(set(words)):
    print(f"{w:15} -  {words.count(w):2}")
