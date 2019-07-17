import random

chances = 3

random_number = random.randint(1, 10)

def choose():
    chosen_number = input("Enter A Number Between 1 and 10 ")
    chosen_number = int(chosen_number)
    return chosen_number
    
    print("Number Chosen")


def compare(chosen_number, random_number):
    
    if chosen_number == random_number:
        print ("You guessed right! The number is " + str(random_number))
        end_game()
        
    elif chosen_number < random_number:
        print ("Try again, the number is greater than " + str(chosen_number))
        reduce_chance()
    
    elif chosen_number > random_number:
        print ("Try again, the number is less that " + str(chosen_number))
        reduce_chance()

def reduce_chance():
    chances - 1
    
def end_game():
    chances = 0

while chances >= 1:
    chosen_number = choose()
    compare(chosen_number, random_number)


print("Game Over")