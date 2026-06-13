fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
new = []
for x in fruits:
    if x == "banana":
        new.append("orange")
    else:
       new .append(x)

print(new)

# we can do it in one line 
new1 = ["orange" if x == "banana" else x for x in fruits]
print(new1)
