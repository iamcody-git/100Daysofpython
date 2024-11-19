try:
    width = float(input("Enter a width of rectangle: "))
    height = float(input("Enter a height of rectangle: "))
    
    if width == height:
        exit("Its look like square")

    area = width * height
    print(f"Area of rectangle is : {area}")
    
except ValueError:
    print("Inputs must be in number")