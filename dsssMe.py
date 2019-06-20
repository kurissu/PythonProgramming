#direct sequence spread spectrum
def encode(bit,chipping):
	index=0
	for i in chipping:
		chipping[index]=chipping[index]*bit
		index=index+1
	return chipping

chipping=[1,1,1,-1,1,-1,-1,-1]
bit=-1
enc=encode(bit,chipping)
print('the encoded message')
print(enc)

def decode(recv,chipping):
	dec=[]
	length=len(chipping)
	for i in chipping:
		dec.append(chipping[i]*recv[i])
	ret=0
	for i in dec:
		ret=ret+i
	decimal = ret/length
	print(decimal)
	if(1-decimal) < (decimal+1):
		return 1
	else:
		return -1

noise = [1,-1,1,-1,1,-1,1,-1]
def distortion(noise,recv):
	index=0
	for i in recv:
		recv[index]=noise[index]*recv[index]
		index=index+1
	return recv

print('the noise ')
print(noise)
dist = distortion(noise,enc)
print('the distortion ')
print(dist)
print(decode(enc,chipping))
print(decode(dist,chipping))
