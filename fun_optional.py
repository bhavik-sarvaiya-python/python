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



