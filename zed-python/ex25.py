def break_word(stuff):
    """ This function will break words for us"""
    words = stuff.split(' ')
    return words
def sort_word(words):
    """ Sorts the words"""
    return sorted(words)
def print_first_word(words):
    """ Prints the first word after popping it out """
    word = words.pop(0)
    print(word)
def print_last_word(words):
    """ Prints the last word after popping it out """
    word = words.pop(-1)
    print(word)
def sort_sentence(sentence):
    """ Take in the full sentence and return sorted words"""
    words = break_word(sentence)
    return sort_word(words)
def print_first_and_last(sentence):
    """ Prints the first and last word of the sentence """
    words = break_word(sentence)
    print_first_word(words)
    print_last_word(words)
def print_first_and_last_sorted(sentence):
    """ Sorts the word and then print the first and last one """
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)
