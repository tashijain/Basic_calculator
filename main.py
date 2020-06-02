import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")
# hold result of previously calculated equation
previous = 0

run = True


def perform_math():
    global run
    global previous
    choice = ""
    if previous == 0:
        choice = input("Enter equation:")
    else:
        choice = input(str(previous))

    if choice == 'quit':
        print("Goodbye, human")
        run = False
    else:
        # making sure that eval function is handed only numbers - using regEx for that
        choice = re.sub('[a-zA-Z,.:()" "]', '', choice)

        if previous == 0:
            previous = eval(choice)
        else:
            previous = eval(str(previous)+choice)


while run:
    perform_math()






