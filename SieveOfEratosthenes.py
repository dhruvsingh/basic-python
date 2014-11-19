print 'Show prime numbers till: '
x = int(raw_input())
numlist = range(2,x+1)
for num in numlist:
    p = 2
    while p < numlist[-1]:
        if (p * num) in numlist:
            numlist.remove(p * num)
        p = p + 1
print numlist
print 'Prime numbers till {0} are {1}'.format(x, len(numlist))
