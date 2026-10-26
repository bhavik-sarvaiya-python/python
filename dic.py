data = {
    "name":"Arjun",
    "age":25,
    "city":"vadodara"
}

print("data =",data)
print("name : ",data["name"])
print("age : ",data["age"])
print("city : ",data["city"])

print("using get mehtod -> ")
print(data.get("name"))
print(data.get("age"))
print(data.get("city"))

data["age"]= 23 #update
data["phno"]="3965328978" #add new data
del data["name"] #delete the key
print("data =",data)


for k,v in data.items():
    print(k," : ", v)


print(data.keys())
print(data.values())
print(data.items())


runs = {"Rohit":100,"virat":75,"Rahul":85,"Dhoni":150}
print(sorted(runs)) # using the sorted method 
                    # only short the key not dict record

print(runs)


# lambda arguments : expression
# lambda function

n = lambda x : x+30;

ans = n(10)
print(ans)

y = lambda x: "Zero" if x == 0 else "Even" if x % 2 == 0 else "Odd" 

print(y(10))
print(y(5))



