def binary(decimal):
	if decimal==0:
		return
	binary(int(decimal/2))
	print(decimal%2, end="")
	return

def asciiBin(string):
	for i in string:
		binary(ord(i))
		print(' ')

asciiBin('abc')
