import csv

with open("csvfiles/weather.csv", "r") as file:
    data = list(csv.reader(file))
    
city = input('enter a city : ')

for row in data:
    if row[0] == city:
        print(row[1])