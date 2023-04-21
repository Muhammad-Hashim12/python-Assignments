'''Write a Python program to find smallest and largest word in a given string.'''


string='The Quick Brown Fox Jumps Over The Lazy Dog'

listt=string.split(' ')
smallest_word=listt[0]
largest_word=listt[0]

for word in listt:
    if len(word)<len(smallest_word):
        smallest_word=word

    if len(word)>len(largest_word):
        largest_word=word
print(f"Smallest word is '{smallest_word}' and Largest word is '{largest_word}'")
    