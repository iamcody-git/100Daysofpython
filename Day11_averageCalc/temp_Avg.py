
def get_average():
    with open("files/data.txt", "r") as file:
        data = file.readlines()
        
    values = data[1:]
    values = [float(i) for i in values]
    avg_value = sum(values) / len(values)
    return(f"The avg value of temp is : {avg_value}")
        
        
average = get_average()
print(average)
    