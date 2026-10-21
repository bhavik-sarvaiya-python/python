a = [1,5,8,15,10,3] #list
b = {1,15,9,8,10} #set
c = (1,5,6,8,10) #tuple
d = {'a':10,'b':10} #dic

print("list before sorting= ",a)
a.sort()
print("list after sorting = ",a)
a.append(20)
print("list ",a)
a.insert(0,3)
print("list change index value 5 t0 3 ",a)
a.remove(15)
print("remove value of 15 in list",a)
print(a.count(3))
print(a)