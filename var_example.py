v9 = {
    "emp":[{
        "name":"manish",
        "age":25,
        "ph_no":"1234567895"
    },{
        "name":"dhruv",
        "age":27,
        "ph_no":"9856235689"
    },{
        "name":"parth",
        "age":28,
        "ph_no":"8956235689"
    }]
}

print("v9",v9)
print("===============================")
print("name = ",v9["emp"][0]["name"])
print("ph_no = ",v9["emp"][0]["ph_no"])
print("===============================")
print("name = ",v9["emp"][1]["name"])
print("ph_no = ",v9["emp"][1]["ph_no"])
print("===============================")
print("name = ",v9["emp"][2]["name"])
print("ph_no = ",v9["emp"][2]["ph_no"])

#print("name = ",v9["emp"]["name"])
#print("age = ",v9["emp"]["age"])
#print("phone number = ",v9["emp"]["ph_no"])

print(type(v9))