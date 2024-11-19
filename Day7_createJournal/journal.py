Date = input("Enter a today data: ")
Mood = input("How was your mood rate in scale of 1 - 10 ? ")
Explain_day = input("Let describe my day: " + "\n")

with open(f"Journal/{Date}.txt", "w") as file:
    file.write(Mood + 2 * "\n")
    file.write(Explain_day)
print("Yours journal have been saved.")