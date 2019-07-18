import random


random_number = random.randint(1, 15)
chosen_number = int(input("Enter a number between 0 and 15 "))


if chosen_number == random_number:
    print ("Congrats! You guessed right!")
else:
    if chosen_number > random_number:
        chosen_number = int(input("Try again, random number is less than " + str(chosen_number) + " "))
        
        if chosen_number == random_number:
            print ("Congrats! You guessed right!")
        else:
            print ("Sorry, Game Over!")
            
    elif random_number > chosen_number:
        chosen_number = int(input("Try again, random number is greater than " + str(chosen_number) + " "))
        
        if chosen_number == random_number:
            print ("Congrats! You guessed right!")
        else:
            print ("Sorry, Game Over!")

#print(random_number, chosen_number)