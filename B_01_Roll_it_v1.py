
def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("please enter yes /no")
            continue

def instructions():
    print("""
***Instructions***
    
Roll the dice and try to win!
    """)

def int_check():

    error = 'Please enter an integer more than ? equal to 13'
    while True:
        try:
            response = int(input("What is the game goal?"))

            if response < 13:
                print(error)
            else:
                return response
        except ValueError:
            print(error)

want_instructions = yes_no("Do you want to see the instructions? ")

if want_instructions == 'yes':
    instructions()
print()
game_goal = int_check()
print(game_goal)