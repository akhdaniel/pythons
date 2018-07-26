items = raw_input("enter comma separated words:")

# words = items.split(",")
# uniques = set(words)
# sorteds = sorted(uniques)
# print ",".join(sorteds)

print ",".join( sorted(set(items.split(","))) )
