"""
Think of a file as
a notebook stored on your computer.
"""
file = open("data.txt","w")
file.write("I am arnob")
file.close()

file = open("data.txt","r")
print(file.read())
file.close()

file = open("data.txt","w")
file.write("I have a plan man. But this plan is stolen")
file.close()

file = open("data.txt","r")
print(file.read())
file.close()