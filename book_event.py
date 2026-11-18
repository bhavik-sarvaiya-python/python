
"""
 import <module_name>
 import <module_name> as <alice_name>
"""
#import math 
import math as m
import event as e

#print(math.sqrt(4));
print(m.sqrt(4));

print(e.bus_book_ticket("Dharuv"))
print(e.bus_book_ticket("Arman","middle"))
print(e.bus_book_ticket("Radhika","regular",True))

redius = float(input("Please enter the are of redius"))
print(e.area(redius))