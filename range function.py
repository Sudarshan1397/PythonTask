#range() built in function is used to generate sequence of int in given range
#range(start,stop,step) stop is not included
#range(start,stop) here step is by default 1
#range(stop) 0 to stop step is 1 start by default 0

"""
for i in range(start,stop,step):
    # statement
"""
from dictionaries import groceries

for i in range(1,11,2): #1,3,5,7,9 stop is not included
    print(i)

# generate even numbers between 1 and 10(10 excluded)
for i in range(2,10,2):
    print(i)

# generate number in reverse order 20 to 10 (excluding 10)
for i in range(20,10,-2):
    print(i)
#
for i in range(5): # start=0,step=1,= 0,1,2,3,4
    print(i)

groceries=['salt','milk','sugar']

for index in range(len(groceries)):
    print(index)        #0,1,2

prfits=[9,11,6,10]
for index in range(len(prfits)):
    q=index+1
    print(f" profit for quarter {q} is {prfits[index]}")