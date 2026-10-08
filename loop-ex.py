"""
loop:
1) for -> fix no iteration
2) while -> first check the condtion than iteration (entry level loop)
3) do while -> 1) one statement always print.2) after that check the condtion
            -> exit level loop 
"""
#for -> fix no iteration
"""
1 to 5 alway use for loop
for (var) in (no of interation):
    body {print statement}
"""
for i in range(1,5):
    print(i)


print("*"*30)

var = [1,2,3,4,5,6]
for i in var:
    print(i,"==> ",var[i-1])    