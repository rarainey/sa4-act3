number = 10
num_guesses = 10

print("I'm thinking of a number...")

print(f"You have {num_guesses} guesses to find it!")
guess = input("What number am I thinking of? (q to quit) ")
num_guesses -= 1
while guess != str(number) and guess != 'q' and num_guesses != 0:
   print(f"Sorry! Wrong number. Try again. You have {num_guesses} guess(es) left.")
   guess = input("What number am I thinking of? (q to quit) ")
   num_guesses -= 1


if guess == str(number):
   print("Congratulations! You guessed the right number.")
elif guess == 'q':
   print(f"Sorry! The number was {number}.")
elif num_guesses == 0:
   print(f"Sorry! You ran out of guesses! The number was {number}")