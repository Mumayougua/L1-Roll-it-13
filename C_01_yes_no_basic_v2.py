
def yes_no(question):
    while True:
        responce = input(question).lower()
        if responce == "yes" or responce == "y":
            return "yes"
        elif responce == "no" or responce == "n":
            return "no"
        else:
            print("please enter yes /no")
            continue

while True:
    want_instructions = yes_no("Do you want to see the instructions? ")
    print(f"you chose {want_instructions}")

print('we done')