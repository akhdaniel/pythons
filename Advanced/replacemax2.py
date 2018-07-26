import re

text = "Python Excercises, PHP Excercises"

out = re.sub(r'[, .]', ":", text, 3)

print out
