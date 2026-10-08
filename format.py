name =  "Raju"
marks = 90.5
#String .formate method for formate the string
print("name = {} ,marks= {}".format(name,marks))

#after python 3.0.0 upper version we can use(f-string)
name1 ,marks1=  "Kaju", 92.5
print(f"name: {name1} ,marks: {marks1}")


#old style % method formateing
name2 ,marks2=  "Saju", 93.5
print("name: %s ,marks: %.10f "%(name2,marks2))



"""
#if..else..
if condition :
    body
else:
    body   

#if...elif....elif ....else (leader.. if else)
if condition :
    body
elif condition :
    body     
else:
    body      
"""

x = input("Enter the clour :")

if x == "red":
    print("read")
elif x == "green":
    print("green")
elif x == "yellow":
    print("yellow")
else:
    print("new clour :", x)             