product = [
    {"name":"bat","price":1200,"stock":5},
    {"name":"boll","price":2000,"stock":1},
    {"name":"pad","price":4000,"stock":3}]

list_filtr = list(filter(lambda p:p["stock"]>1,product))

for p in list_filtr:
    print(p['name']) 
    print(p['price'])

print([p['name'] for p in list_filtr])
print([p['price'] for p in list_filtr])
