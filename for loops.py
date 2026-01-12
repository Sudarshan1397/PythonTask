"""
#loop with string
x="Apple"
for char in x:
    print(char)
print("End of the loop")
"""
# loop with dictionary
employee={'empid':1001,'name':'John Doe', "Department":"HR"}
#print(employee)
for i in employee:  #this loop will prints only keys of Dictionary
    print(i)

for i in employee:  # this will print key value of dict
    print(i,employee[i])

print(employee.items()) # this will print key value pair in the form of tuple
for i in employee.items():
    print(i)       # this will print key value pair in the form of tuple on below one

for i in employee.items():
    print(i[0],i[1])
