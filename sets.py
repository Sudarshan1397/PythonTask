#sets are not in ordered slicing and indexing are not allowed
#list and sets are mutable tuples and frozen sets are immutable

#set cannot have duplicate elements
#list and tiple can have duplicate elements
# list=[1,35,7,5,3,6]
#tuple=(1,35,7,5,3,6)
#set={1,35,7,5,3,6,7}
#fs=frozenset({10,20,30})   -----frozen set
#set accept duplicate but stores only once occurrence
#concate does not work in sets but works with list and tuples


s1={10,2.4,10,30,20,10}
print(s1,type(s1))
s1.add(5)
print(s1)
s1.remove(30)#gets error if element is not present
print(s1)
s1.discard(30)#does not get error if element is not present
print(s1)
