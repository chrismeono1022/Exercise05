from sys import argv

script, filename= argv

f = open(filename)
f.read()
f.close

count = 0

for char in f:
	print char
	count +=1
	print count
	
