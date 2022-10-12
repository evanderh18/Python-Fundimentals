# Conditional
# Method evaluate data
# if then else

import random

#ask the suer to select the upper bound
#ask the user to guess
upper_bound = input("What is the upper bound? ")
upper_bound = int(upper_bound)

# generate a random interger starting at 1 and going to upper_bound
random_number = random.randint(1, upper_bound)
print(random_number)

user_guess = None

while user_guess != random_number:

    user_guess = input("Enter guess between 1 and " + str(upper_bound) + ": ")

    #check if user guess is equal to random number

    if int(user_guess) == random_number:
        print("You win")
    else:
        print("Mission failed, we'll get them next time")
print("Game Over")
# high_range = 100
# middle_number = int(high_range/2)
# my_guess = middle_number
# number_guesses = 0
# highOrlow = "lower"
# output = "{} is {} than {}"

# my_random_number = random.randint(1, high_range)

# print(my_random_number)
# print(my_guess)


# #evaluate the random number and compare it to the middle number
# if my_guess < my_random_number :
#     highOrlow = "lower"

# if my_guess > my_random_number :
#     highOrlow = "higher"

# if my_guess == my_random_number:
#     highOrlow = "equal"

# print(output.format(my_guess, highOrlow, my_random_number))