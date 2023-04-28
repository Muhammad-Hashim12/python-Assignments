'''Create a program that will play the “cows and bulls” game with the user. The game works like this:

Randomly generate a 4-digit number. 
Ask the user to guess a 4-digit number(Digits should not be repeated). 
For every digit that the user guessed correctly in the correct place, they have a “cow”. 
For every digit the user guessed correctly in the wrong place is a “bull.” 
Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

Say the number generated by the computer is 1038. An example interaction could look like this:

  Welcome to the Cows and Bulls Game! 
  Enter a number: 
  >>> 1234
  2 cows, 0 bulls
  >>> 1250
  1 cow, 1 bull
  ...
Until the user guesses the number.
'''


import random

count_cow=0
count_bull=0

print('Welcome to the Cows and Bulls Game 🤪 ')

def check_random():
    while True:
        random_num=str(random.randint(1000, 9999))
        if len(set(random_num))==4:
            print(random_num)
            break
    return random_num

random_inp=check_random()

def user_input():    
    while True:
        user=input('enter the 4 digit number that must be unique: ')
        print(f'>>> {user}')
        if len(user)!=4 or len(set(user))!=4:
            print('Invalid input😒.. please provide valid input ')
            continue
        break
    return user
        
user_inp=user_input()

def counting(count_cow,count_bull):        
    for i in range(len(user_inp)):
        if user_inp[i]==random_inp[i]:
            count_cow+=1
        elif user_inp[i] in random_inp:
            count_bull+=1
    return count_cow,count_bull
    
total_count=counting(count_cow, count_bull)

def printing():
    if total_count[0]==1:
        print(f'{total_count[0]} cow,',end=' ')
    else:
        print(f'{total_count[0]} cows,',end=' ')
    if total_count[1]==1:
        print(f'{total_count[1]} bull')
    else:
        print(f'{total_count[1]} bulls')
    
printing()


