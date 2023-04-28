'''
Write a txt file which has a word in each line like:
Hands
Legs
India
Crow
Rain
...

Write a python code to read the file and store the words in the list

Write a function to guess a word randomly from the list.

Now, write a function which asks user to guess the chosen word letter by letter.
Show "incorrect" message to the wrong guessed letter. 
Display  letters in the clue word that were guessed correctly. 

Let say word is EVAPORATE

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
You left with 5 chances to guess.

>>> Guess your letter: E
E _ _ _ _ _ _ _ E
...
And so on.


1)Only let the user guess 6 times, and tell the user how many guesses they have left.
Keep track of the letters the user guessed.
2) If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
3)When the player wins or loses, let them start a new game.
'''
import random

def play_hangman():
    file_path=r'C:\Users\Lenovo\Desktop\pace wisdom  Assignments\Assignments\python assignment\Assignment5\python8.2.txt'
    with open(file_path,'r') as text_file:
        lines=[line.lower().strip() for line in text_file.readlines()] 
        print(lines)
        
    def guess_word(lines):
        return random.choice(lines)
    got_word=guess_word(lines)


    def guess_letter(got_word):
        print('>>> Welcome to Hangman!')
        # print(got_word)
        clue=list(len(got_word)*'_')
        print('you Have 6 guess 😊')
        print(''.join(clue))
        attempt=0
        till=6
        while attempt<=6:
            user_inp=input('Guess your Letter: ').lower()
            if len(user_inp)!=1:
                print('please provide valid input')
                continue
            elif user_inp not in  got_word:
                if attempt!=6:
                    print(f'You have last {till-1-attempt} guess')
                    print(''.join(clue))
                attempt+=1
                if attempt==6:
                    print(f'You lost game😯 answer is {got_word}')
                    break
            else:
                for i in range(len(clue)):
                    if got_word[i]==user_inp:
                        clue[i]=got_word[i]
                        store=''.join(clue)
                        print(store)
                if store==got_word:
                    print(f'Congrats You won the game 🥳🥳 just with {attempt} guess ')
                    break
        play_again = input('Do you want to play again? 😁 (y/n) ')
        if play_again.lower() == 'y':
            play_hangman()


    guess_letter(got_word)


play_hangman()
            

