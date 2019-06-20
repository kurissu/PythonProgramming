codes = {}
#This function finds the frequency of each characters
def frequency (str) :
	freqs = {}
	for ch in str :
		freqs[ch] = freqs.get(ch,0) + 1
	return freqs
#This function sort the list of frequency characters
def sortFreq (freqs) :
	letters = freqs.keys()
	tuples = []
	for let in letters :
		tuples.append((freqs[let],let))
	tuples.sort()
	return tuples
#This function creates a Tree structure called Heap
def buildTree(tuples) :
	while len(tuples) > 1 :
		leastTwo = tuple(tuples[0:2])                  # get the 2 to combine
		theRest  = tuples[2:]                          # all the others
		combFreq = leastTwo[0][0] + leastTwo[1][0]     # the branch points freq
		tuples   = theRest + [(combFreq,leastTwo)]     # add branch point to the end
		tuples.sort(key=lambda t: t[0])                # sort it into place
	return tuples[0]            # Return the single tree inside the list
#This function takes out the counter of each character frequency off
def trimTree (tree) :
	p = tree[1]                                    # ignore freq count in [0]
	if type(p) == type("") : return p              # if just a leaf, return it
	else : return (trimTree(p[0]), trimTree(p[1])) # trim left then right and recombine
#This function assign Binary prefix code for each nodes
def assignCodes (node, pat='') :
	global codes
	if type(node) == type("") :
		codes[node] = pat                # A leaf. set its code
	else  :                              #
		assignCodes(node[0], pat+"0")    # Branch point. Do the left branch
		assignCodes(node[1], pat+"1")    # then do the right branch.
#This function encode the message
def encode (str) :
    global codes
    output = ""
    for ch in str : output += codes[ch]
    return output
#This function decode the message by passing in the prefix binary tree and the encoded binary message.
def decode (tree, str) :
    output = ""
    p = tree
    for bit in str :
        if bit == '0' : p = p[0]     # Head up the left branch
        else          : p = p[1]     # or up the right branch
        if type(p) == type("") :
            output += p              # found a character. Add to output
            p = tree                 # and restart for next character
    return output
#This is the lyric I chose from the song Ashes by Céline Dion
lyric = """What's left to say?
These prayers ain't working anymore
Every word shot down in flames
What's left to do with these broken pieces on the floor?
I'm losing my voice calling on you
'Cause I've been shaking
I've been bending backwards till I'm broke
Watching all these dreams go up in smoke
Let beauty come out of ashes
Let beauty come out of ashes
And when I pray to God all I ask is
Can beauty come out of ashes?
Can you use these tears to put out the fires in my soul?
'Cause I need you here, woah
'Cause I've been shaking
I've been bending backwards till I'm broke
Watching all these dreams go up in smoke
Let beauty come out of ashes
Let beauty come out of ashes
And when I pray to God all I ask is
Can beauty come out of ashes?
Can beauty come out of ashes?"""
#Find the frequency of each characters in the lyric
freqs = frequency(lyric)
#sort the dictionary of char and frequencies 
tuples = sortFreq(freqs)
#create the tree with the sorted dictionary
tree = buildTree(tuples)
#take out the frequency out of the Heap
trim = trimTree(tree)
#assign the prefix binary code to each nodes of the tree
assignCodes(trim)
#encode the lyric
encoded = encode(lyric)
print(freqs)
print('')
print(tuples)
print(trim)
#show the assign code for each characters.
print(codes)
#print out the endcoded message in prefix binary form.
print(encoded)
#Show that the decoded message was correct
print(decode(trim,encoded))
