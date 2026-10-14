"""
while condition :
    body

#while loop always frist check the condition.
#if condition is true then it's execute.
# otherwise exit loop.
# it's also call entry level loop.

"""
number = int(input("Enter the number base on that we create table:"))
var = 1

# +=,-=,*=,!=
while var<=10:
    print(number," * ",var," = ",(number*var))
    var +=1
print("-------------------------------------------")
x = [1,2,3,4,5,6,7,8,9,10]
for var in x:
    print(number," * ",var," = ",(number*var))  

"""
*
**
***
****
*****
-------------------
    *
  *   *
*   *   *
-------------------
++++++++++
 *******
  ++ ++
   * *
    +
"""    