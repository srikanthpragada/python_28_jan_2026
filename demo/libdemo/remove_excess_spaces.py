import re

with  open("story.txt", "rt") as f:
    content = f.read()

new_content = re.sub(" +", ' ', content)

with open("story.txt", "wt") as f:
    f.write(new_content)

