import time
import sys


def choosepivot1(a, l, r):
	return l
def choosepivot2(a, l, r):
	return r
def choosepivot3(a, l, r):
	x = a[l]
	y = a[l+(r-l)/2]
	z = a[r]
	result = [x,y,z]
	result.sort()

	if result[1]==x:
		return l
	if result[1]==y:
		return l+(r-l)/2
	if result[1]==z:
		return r

def quicksort(choosepivot, a, l, r):
	if  r-l < 1:
		return 0

	# choose pivot
	pivot = choosepivot(a, l, r)
	(a[l], a[pivot]) = (a[pivot], a[l])
	p = a[l]

	m = r-l

	#partition
	i = l+1
	for j in range (l+1, r+1):
		if a[j]<p:
			(a[j], a[i]) = (a[i], a[j])
			i+=1
	(a[l], a[i-1]) = (a[i-1], a[l])

	#recursively a
	m += quicksort(choosepivot, a, l, i-2)

	#recursively b
	m += quicksort(choosepivot, a, i, r)

	return m


lines = [int(line.strip()) for line in open('QuickSort.txt')]
#lines = [3,8,1,5,2,4,7,6]
#start_time = time.clock()
#lines = [4,5,6,7]
print quicksort(choosepivot1, lines, 0, len(lines)-1)
#print "1:", time.clock() - start_time
#print lines


lines = [int(line.strip()) for line in open('QuickSort.txt')]
print quicksort(choosepivot2, lines, 0, len(lines)-1)

lines = [int(line.strip()) for line in open('QuickSort.txt')]
print quicksort(choosepivot3, lines, 0, len(lines)-1)
