def change_char(str1):
	char = str1[0]
	str2 = str1.replace(char, '$') # $esta$t
	str2 = char + str2[1:]  # resta$t
	return str2


print change_char("restart")

