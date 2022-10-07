# Conditional
# Method evaluate data
# if then else

from cgitb import grey
import random

high_range = 100
middle_number = int(high_range/2)
my_guess = middle_number
number_guesses = 0
highOrlow = "lower"
output = "{} is {} than {}"

my_random_number = random.randint(1, high_range)

print(my_random_number)
print(my_guess)


#evaluate the random number and compare it to the middle number
if my_guess < my_random_number :
    highOrlow = "lower"

if my_guess > my_random_number :
    highOrlow = "higher"

if my_guess == my_random_number:
    highOrlow = "equal"

print(output.format(my_guess, highOrlow, my_random_number))