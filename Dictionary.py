"""
Dictionary items are ordered, changeable, 
and do not allow duplicates.

*items are presented in key:value pairs
"""

student = {
    "name":"Iqbal",
    "age":22,
    "CG":3.83,
    "Uni":"Daffodil internation university"
}

# .items() method returns both the key and value together.
for key,value in student.items():
    print(key ,":", value)


"""
student.keys() → returns only keys.
student.values() → returns only values.
student.items() → returns both key and value as tuples.
"""