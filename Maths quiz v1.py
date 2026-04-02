# Code name: Maths quiz string checker
# By: Grayden Farrer
# Date: march 26, 2026
# Purpose: This code will ask the user if they would like
# to see the instructions
import random


# Variables

# Check that users have entered a valid option based on list
def string_checker(question, valid_ans=( "yes", "no" )):
    error = f"Please enter a valid option from the following list: yes, no"

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


# gives the instructions
def instructions():
    """prints instructions"""
    print("""
    ******* instructions *******

        To begin, choose the number of questions. 
        Then, answer the questions. 
        Once you have finished the questions, you may choose to see you game history.
         """)


# Asks for the amount of questions
def int_check(question):
    while True:
        error = "Please enter an integer that is 1 or more and less than 20"

        to_check = input(question)

        try:
            response = int(to_check)

            # checks that the number is more than / equal to 1
            if response < 1:
                print(error)
            elif response > 20:
                print(error)
            else:
                return response

        except ValueError:
            print(error)




# Main routine
mode = "regular"
rounds_played = 0
score = 0

game_history = []

name = input("what is your name?: ")
print(f" Welcome to math quiz {name}!")

want_instructions = string_checker("Do you want the instructions? ")

# checks if user wants the instructions
if want_instructions == "yes":
    instructions()

# ask user for number of rounds
num_rounds = int_check("how many rounds? please choose a number between 1 and 20: ")



# game loop starts here
while rounds_played < num_rounds:

    rounds_played += 1


    # rounds headings
    if mode == "regular":
        rounds_heading = f"\n ()()() Round {rounds_played} of {num_rounds} ()()()"

        print(rounds_heading)
        print()

    try:

        num_one = random.randint(1, 20)
        num_two = random.randint(1, 20)
        q_generator = num_one + num_two
        print(f"{num_one} + {num_two} =")
        user_input = int(input(""))
        if user_input == q_generator:
            print("correct")
            score +=1
        else:
            print("wrong")

        round_feedback = f" you chose: {user_input} answer: {q_generator}"
        history_item = f"Round: {rounds_played} - {round_feedback} - score: {score}"



        print(round_feedback)
        game_history.append(history_item)


        if rounds_played > 0:
            #claculate statistics

            rounds_lost = rounds_played - score
            percent_won = score / rounds_played * 100
            percent_lost = rounds_lost / rounds_played * 100


            # output game stats
            print(" game statistics")
            print(f" Won: {percent_won:.2f}%")
            print(f" Lost: {percent_lost:.2f}%")

    except ValueError:
        print("please enter value as a number")

#this code asks the user if they would like to see
see_history = string_checker("\nDo you want to see your game history? ")
if see_history == "yes":
    for item in game_history:
        print(item)


