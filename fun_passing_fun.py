def apply_descount(price,rule):
    return rule(price)

def festival(p):
    return p * 0.50

def special(p):
    f_amt = festival(p)
    dscount_amt = membership(f_amt)
    return dscount_amt

def membership(p):
    return p - 200

name = input("Enter the name : ")
price = float(input("enter the price :"))
qty   = int(input("enter the quantity :"))
amount = price * qty

final_festival_ds_amount = apply_descount(amount,festival)
final_member_ds_amount = apply_descount(amount,membership)
final_special_ds_amount = apply_descount(amount,special)

print("Name:",name)
print("=======================")
print(f"price * qty : {price} X {qty} = {amount}")
print("=======================")
print("festival discount price :", final_festival_ds_amount)
print("member discount price :",final_member_ds_amount)
print("member special price :",final_special_ds_amount)

# map()
"""
 map(function,iterable(list))
"""

celsius = [0,25,35,55,65,100]

def c_to_f(val):
    f = (val*(9/5)+32)
    return f

convert = list( map(c_to_f,celsius))
print("celsius to f list =",convert)

