"""
* * * * * * * * * *
* * * *     * * * *
* * *         * * *
* *             * *
*                 *
"""
n = int(input("enter the pattern No:"))
for i in range(n,0,-1):
    
    for j in range(n-i):
        print(" ",end="")
    for k in range(i):
        print("* ",end="")  
    print()



for i in range(n):
    for j in range(n - i):
        print("*", end=" ")

    for j in range(2 * i):
        print(" ", end=" ")

    for j in range(n - i):
        print("*", end=" ")

    print()
