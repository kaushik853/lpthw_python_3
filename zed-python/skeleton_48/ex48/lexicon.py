
class Lexicon(object):
    def __init__(self):
        print('garbage')

Direction = ['north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back']
Verbs = ['go', 'stops', 'kill', 'eat', 'open']
Stops = ['the', 'from', 'in', 'of', 'at', 'it']
Nouns = ['door', 'bear', 'princess', 'cabinet']

def convert_numbers(user_integer):
    try:
        int(user_integer)
        return True
    except ValueError:
        return None


def scan(user_input):
    #self.user_input = user_input
    words = user_input.split()
    sentence = []
    for word in words:
        if word.lower() in Direction:
            sentence.append(('direction', word))
        elif word.lower() in Verbs:
            sentence.append(('verb', word))
        elif word.lower() in Stops:
            sentence.append(('stop', word))
        elif word.lower() in Nouns:
            sentence.append(('noun', word))
        elif convert_numbers(word):
            sentence.append(('number', int(word)))
        else:
            sentence.append(('error', word))
    return sentence
