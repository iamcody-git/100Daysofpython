password = input("Enter a password: ")

# dictionary{} : like a list but provides us the key and value pair 
result = {}

if len(password) >= 8:
    result["length"] = True
else:
    result["length"] = False
    
digit = False
for i in password:
    if i.isdigit():
        digit = True

result["digits"] = digit

uppercase = False
for u in password:
    if u.isupper():
        uppercase = True
result["uppercase"] = uppercase

print(result)

if all(result.values()):
    print("strong password")
else:
    print("weak password")    
    