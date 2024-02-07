number = 10

print("I'm thinking of a number...")

guess = input("What number am I thinking of? (q to quit) ")
while guess != str(number) and guess != 'q':
   try:
      guess = int(guess)
      if guess > number:
         print("Too high. Try again!")
      else:
         print("Too low. Try again!")
   except:
      print("Guess must be a number!")
   guess = input("What number am I thinking of? (q to quit) ")

if guess == str(number):
   print("Congratulations! You guessed the right number.")
else:
   print(f"Sorry! The number was {number}.")
