# %%
import random
print('what is your name ?')
name = input().capitalize()
print('Hello ' + str(name) + ' choose a number between 1 to 10 ')
numberToGuess = random.randint(1, 10)
for chances in range(1, 7):
  try: 
    if chances == 6:
      print('You lose !!!')
      break
    number = int(input())
    if number > numberToGuess:
      print('No ' + str(name) + ' is too high, try again :' )
    elif number < numberToGuess:
      print('No ' + str(name) + ' is too low, try again :' )
    else:
      print('Congrats ' + str(name) + " You WIN !!! in " + str(chances) + " times" )
      break
  except ValueError:
    print('Only number are accepted')