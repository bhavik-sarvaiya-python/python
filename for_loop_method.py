car = ["BMW","TOYOTA","TATA","MG","KIA"]

for i in car:
    print(i)

for index, value in enumerate(car,start=0):
    print("[",index,"] = " , value)

bike = ["HONDA","BAJAJ","OLA","ATHAER"]

bycleck = ["HERO","HERCULAS","KTM","ABC"]
print("CAR"," | ","BIKE"," | ","BYCOCLE")
for var1,var2,var3 in zip(bike,car,bycleck):
    print(var1," | ",var2," | ",var3)


for i in range(1,4):
    print("===== value of i =",i)
    for j in range (5,8):
        print(f"{i}X{j}")
        print("===== value of j =",j)    
