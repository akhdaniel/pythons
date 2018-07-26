import re


def text_match(text):
	match = re.search(r'ab*?', text)
	if match:
		return 'match'
	else:
		return 'not match'


print(text_match("ac"))
print(text_match("abc"))
print(text_match("abbbbbbc"))
print(text_match("jika ada ditengah abbc"))