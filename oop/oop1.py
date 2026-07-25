class arnob:
     age = 20
     #Every normal method inside a class must have self as the first parameter.
     #constructor
     def __init__(self,s1,s2,s3):
          self.s1 = s1
          self.s2 = s2
          self.s3 = s3
          print("sub1 = ",s1)
          print("sub2 = ",s2)
          print("sub3 = ",s3)
    #Fuction
     def ar(self,name,cg):
          print("name: ",name)
          print("cg: ",cg)
          print("age: ",self.age)

s1 = arnob(80,90,100)
s1.ar("arnob",3.83)