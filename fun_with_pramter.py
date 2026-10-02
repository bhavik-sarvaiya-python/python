b_year = int(input("enter your brith year : "))
c_year = int(input("enter your curret year : "))

def display():
    print ("this is function with no patameter")

# it'c calculate the age
# it's a parameterize function
def calculate_age(birth_year,current_year):
    return current_year-birth_year

#call function
age = calculate_age(b_year,c_year) 

print (f"my age is {age}")

def min_max_avg(number):
    l_min = min(number)
    l_max = max(number)
    l_sum= sum(number) 

    return l_min,l_max,l_sum

val = [1,2,3,4,5]
lo,lv,av = min_max_avg(val)

print("min",lo)
print("max",lv)
print("sum",av)

print(f"min :{lo}, max :{lv}, sum :{av}")



 