import random

print('Number guessing game!')
print('Guess a number between 1 and 9: ')

number = random.randint(1, 9)
chances = 0

while chances < 5:
  guess = int(input('Enter a guess:- '))

  if guess == number:
    print('Congratulations! YOU WON!!')
    break
  elif guess < number:
    print('Your guess was lower than the number, guess a number higher than: ', guess)
  else:
    print("Your guess was higher thna the number, guess a number lower than", guess)

  chances += 1

if not chances < 5:
  print("You're a LOSER!\nThe number was", number)
