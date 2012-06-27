import time
import sys

def count_inversions(array, a, b):
	if (b-a) < 1:
		#print array, a, b
		#print "================"
		return 0
	a_max = a+(b-a)/2;
	x = count_inversions(array, a, a_max)
	y = count_inversions(array, a_max+1, b)
	c = []
	i = a
	j = a_max+1
	z = 0
	while i<=a_max or j<=b:
		if i<=a_max and j<=b:
			if array[i]<array[j]:
				c.append(array[i])
				i+=1
			else:
				c.append(array[j])
				j+=1
				z+=a_max-i+1
		else:
			if j<=b:
				c.append(array[j])
				j+=1
				z+=a_max-i+1
			if i<=a_max:
				c.append(array[i])
				i+=1

#	print array, a, a_max, b
	for pos, i in enumerate(c):
		array[a+pos] = i
#	print c

#	print array, x,y,z, x+y+z
#	print "================"
	return x+y+z

def count_inversions_n2(array, a, b):
	x = 0
	for i in range(0, len(array)):
		for j in range(i+1, len(array)):
			if array[i]>array[j]:
				x += 1
	return x


#lines = [6,4]
#lines = [int(line.strip()) for line in open('SimpleArray.txt')]
#lines = [5,6,9,7,8]


lines = [int(line.strip()) for line in open('IntegerArray.txt')]
start_time = time.clock()
print count_inversions(lines, 0, len(lines)-1)
print "n*log(n)", time.clock() - start_time

lines = [int(line.strip()) for line in open('IntegerArray.txt')]
start_time = time.clock()
print count_inversions_n2(lines, 0, len(lines)-1)
print "n*n", time.clock() - start_time
