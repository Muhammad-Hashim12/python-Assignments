''' Write a Python function that takes a list of words and returns the length of the longest one. '''

def longest_word(listt):
    max_len=0
    store_val=0
    for word in listt:
        if len(word)>max_len:
            max_len=len(word)
            store_val=listt.index(word)
    return listt[store_val]

print(longest_word(['the','fox','jumped','over','the','lazy','dog']))