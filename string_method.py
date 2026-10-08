email = "    ManishPatel@gmail.com   "

print ( " email :" ,email)
print ( " email :" ,email.strip())
print ( " email :" ,email.strip()[0])    #frist letter
print ( " email :" ,email.strip()[-1])   #last letter
print ( " email :" ,email.strip()[6:11]) #slice
print ( " email :" ,email.strip()[::-1]) #reverse
print ( " email :" ,email.strip().lower())
print ( " email :" ,email.strip().upper())

var = "java|python|c++|php|Ai".split("|")
print(var)
print(" & ".join(var).upper())
print(email.replace("gmail","outlook"))

name, marks = "Raju",90.5

print("student : {}, Percentage : {}".format(name,marks))
print(f"student = {name}, Precentage = {marks}")

dummy_string = "This is my best program."

print("xx" in dummy_string)
print("is" in dummy_string)
print("xx" not in dummy_string)
print("is" not in dummy_string)

print("#"*30)
print("banana"<"bee")
print("bee">"banana")
print("bee"=="bEe")




