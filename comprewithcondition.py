# find out max number from even and odd num
list = [1,5,6,7,9,3]
even = [x for x in list if x%2 == 0]
print ("Max from even number",max(even))
odd = [x for x in list if x%2 !=0]
print ("Max among odd number: ",max(odd))