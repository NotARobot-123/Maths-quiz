import random
while True:
    score = 0
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