contents = ["John And The Locals", "Monkey Temple", "Purna Rai and DajuBhaiHaru"]
filename = ["NewBand.txt", "OldBand.txt", "DharanBand.txt"]

for contents, filename in zip(contents,filename):
    file = open(f"files/{filename}", "w")
    file.write(contents)