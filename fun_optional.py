def bus_book_ticket(name ,seat="window",meal=False):
    print(f"name = {name}, seat = {seat}, meal = {meal}" )

bus_book_ticket("Arman"); 
bus_book_ticket("Arjun","Middle",True);
bus_book_ticket("Dharuv","Shofa");
bus_book_ticket("","Midele","Shofa");      


def all_employess_dtls(salaris):
    for i in range(len(salaris)):
       print(f"i ={i}", salaris[i])
       salaris[i] += 5000
    return salaris;

emp_salaris = [25000,35000,40000]
updated_salary= all_employess_dtls(emp_salaris)
print("new salary = ",updated_salary)


def full_name(firstName, LastName):
    return firstName+" "+LastName

list = ["Parth","Makwana"] #list
dic = {"firstName":"Dhruv","LastName":"Patel"} #dictonary

print(full_name(*list))
print(full_name(**dic))

def total_makrs(*marks):
    print("lists of marks :",marks)
    return sum(marks)

marks = [95,85,76,80]

print("Total marks =",total_makrs(*marks))
print("Total marks =",total_makrs(56,65,90))
print("Total marks =",total_makrs(56,65,90,78,86,98))

