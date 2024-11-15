total_bill_amt = float(input("Enter total amount of bill Rs "))
tip_amt = float(input("what percentage of tip would you like to be? 10, 20, 25 : "))
person = float(input("how many people are there in total ? "))

total_bill = float((tip_amt/100) * total_bill_amt + total_bill_amt)
print("The bill amount after added tip ",total_bill)

total_bill_per_person = float(total_bill / person)
print("The bill split per person Rs.", total_bill_per_person)


