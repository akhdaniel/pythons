

# open file
fo = open("data2.txt", "wb+")

# write
content ="""Ini adalah data yang akan
ditulis ke dalam file.

Berikut karakter enternya

"""

fo.write(content)

# close
fo.close()
