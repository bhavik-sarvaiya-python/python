"""
for <name_of_var> in <length or range of array> :
    body
# No of iteration you know(5,10,15)   
"""
var = 1;
list = [200,50,100,80,65,23]
for var in list:
    if var <= 23:
        print(" >= ",var)
        break;
    if var >= 50:
        print(" >= ",var)
        continue;
print("===========not show 50 and 23 number==============")
for var in list:
    if (var != 50) & (var != 23)  :
        print(var)
        continue
print("===========not show 5 and 9 number==============")
no = [1,2,3,4,5,6,7,8,9]

"""
no[0]=1
no[1]=2
no[2]=3.......no[8]=9
"""
for var in no:
    if (var != 5) & (var != 9)  :
        print(var)
        continue;
    