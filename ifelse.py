"""
#if statment
if (condtion) :
    body
#if...else statment
if (condtion) :
    body    
else :
    body

#if...elif..else statment (leader if ..else..)
if (condtion) :
    body
elif (condition):
    body        
else :
    body

"""
x = float(input("Enter you percentage : "))

if x<=35: 
    print("fail")
elif ((x>35) & (x<65)):
    print("first class")
elif ((x>65) & (x<=80)):
    print("Destiction class")        
else:
    print("Excelent")


