import glob


# to imports multiple .txt files using python code
myfiles = glob.glob("files/*.txt")

for filepath in myfiles:
    with open(filepath,"r") as file:
        print(file.read())