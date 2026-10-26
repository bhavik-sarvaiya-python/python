marks= [23,33,34,25,30,45,65,70,75,95,99]

# [ <expression> for <var> in <list,tuple,dec.,set> if <condition> ]
passed = [m for m in marks if m>=35]
print("new list ",passed)

result = ['p' if m>=35 else 'f' for m in marks]
print("result list ", result)

grace = [m + 5 for m in marks if m<=35]
print("grace list",grace)

qube = [n*n*n for n in range(1,10)]
print("qube list",qube)