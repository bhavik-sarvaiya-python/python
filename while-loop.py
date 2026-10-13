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
for var in range(1,11):
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