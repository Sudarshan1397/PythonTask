#comma separated key-value pairs
#dictioneries do not have indexes
from Lists import student

groceries={'milk':60,'rice':90.5,'eggs':5}
print(groceries)
#print(groceries[60]) cant use value for fetching
print(groceries['rice'])
#print(groceries['bread']) this will throw error
groceries['milk']=70 #update value of key
print(groceries)

student1={"maths":80.5,"eng":76.0,"phy":89}
print(student1)
print(student1["maths"])
#get()
#print(student1["chem"])  if not present this will give you error

print(student1.get("chem")) # return None if not present
print(student1.get("che",40)) # return default value if not present ie 40 here
print(student1.get("eng",50)) # return original value if present
