human = ["Misti","Mariam","Sabiha","ArzU","dipty"]
new = []
for a in human:
    if "r" in a :
        new.append(a)
print(new)

# we can do it in one line.
# [expression for item in list if condition]

newnew = [x for x in human if "i" in x]
print(newnew)