#Code name: Maths quiz string checker
#By: Grayden Farrer
#Date: march 26, 2026
#Purpose: This code will ask the user if they would like
# to see the instructions
import random

#Variables

#Check that users have entered a valid option based on list
def string_checker(question, valid_ans = ( "yes","no")):
    error = f"Please enter a valid option from the following list: {valid_ans}"

    while True:

        # get user response and make sure its lowercase
        user_response = input(question).lower()

        for item in valid_ans:
            # check if the user response is a word on the list
            if item == user_response:
                return item

            # checks if the user response is the same as
            # the first letter of an item in the list
            elif user_response == item[0]:
                return item

        # print error if user does not enter valid answer
        print(error)
        print()

#gives the instructions
def instructions():
    """prints instructions"""
    print("""
    ******* instructions *******

        To begin, choose the number of questions. 
        Then, .
         """)

#Asks for the amount of questions
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more"

        to_check = input(question)

        # check for infinite mode
        if (to_check) == "":
            return "infinite"

        try:
            response = int(to_check)

            #checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            else:
                return response

        except ValueError:
            print(error)

#creates questions
def q_generator():
    num_one = random.randint(1, 20)
    num_two = random.randint(1, 20)

    q_generator = num_one + num_two
    print(f"{num_one} + {num_two} = {q_generator}")

#Main routine
want_instructions = string_checker("Do you want the instructions?")
#checks if user wants the instructions
if want_instructions == "yes":
    instructions()
#asks for number of questions
q_number = int_check("How many rounds would you like? Push <enter> for infinite mode  ")

if q_number == "infinte":
    mode = "infinite"
    q_number = 1
    
