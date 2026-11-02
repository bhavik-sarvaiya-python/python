"""
# def is keyword
def <funaction_name> (<argument>):
return <value>
""" 
def test():
    print("This is without argument funaction")

#calculate the table
def cal_table(number):
    for i in range(1,11):
        print(number," * ",i ," = ", (number*i))

#calculate redius
def redius(d):
    """
    This is redius caculation function.
    please eneter the daimeter and return the redius.
    """
    return d/2;        

#take input number for the user
no = int(input("enter the value of table."))

#call funaction or method
cal_table(no)
test()        

val = float(input("enter the daimeter ="))
r = redius(val)

print("redius = ",r)
print(redius.__doc__)

# max,min,len,print,sorted,filter this all  pre define function