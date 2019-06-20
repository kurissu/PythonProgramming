def freq(message,character):
	count = 0
	for char in message:
		if char == character:
			count = count +1
	print('the frequency of '+character+' is ',end="")
	return (count/len(message))

print(freq('this is to test the frequency of a charater e in the message','e'))
