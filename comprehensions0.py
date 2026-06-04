"""List comprehension offers a shorter syntax 
when you want to create a new list 
based on the values of an existing list."""

#print square of this list 
num = [1,2,3,4,5]
num1 = []
for x in num:
    num1.append(x*x)

print("Simple way = ",num1)

#using another way (comprehension)
num2 = [x*x for x in num]
print ("another way num2 = ",num2)