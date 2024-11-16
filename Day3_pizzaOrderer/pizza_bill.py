print("lets order a pizza")
print("Your bill: ")

size = (input("What size of pizza do you want? S, M AND L : "))
pepperoni = (input("Do you want pepperoni? Y OR N : "))
extra_cheese = (input("Do you want extra cheese? Y OR N : "))

bill =0 
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 30
else:
    print("we dont serve that kind of pizza")
    

if pepperoni == "Y":
    if size == "S":
        bill += 3
else:
    bill += 5
    

if extra_cheese == "Y":
    bill +=1

print(f"Your order bill is ${bill}.")
print("Visit us again. Thank you!!")
print("goog ggoo")
    
