import random

def get_determiner(grammatical_number):

    if grammatical_number == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    deter = random.choice(words)
    return deter

def get_noun(grammatical_number):
    if grammatical_number == 1:
        words = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        words = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]
    """ Parameter
        grammatical_number: an integer that determines
            if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    noun = random.choice(words)
    return noun

def get_verb(grammatical_number, tense):
    words = []
    
    if tense == "past":
        words =  ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present" and grammatical_number == 1:
        words = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    elif tense == "present" and grammatical_number != 1:
        words = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    elif tense == 'future':
        words = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    
    verb = random.choice(words)
    return verb

def get_preposition():

    words = ['about', 'above', 'across', 'after', 'along', 'around', 'at', 'before', 'behind', 'below', 'beyond', 'by', 
    'despite', 'except', 'for', 'from', 'in', 'into', 'near', 'of', 'off', 'on', 'onto'
    ,'out', 'over', 'past', 'to', 'under', 'with', 'without']
    preposition = random.choice(words)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.


    Parameter
        quantity: an integer that determines if the
            determiner and nouns are singular or plural.
    Return: a prepositional phrase.
    """
    quantity = random.choice(quantity)
    return get_prepositional_phrase
def main():
    '''grammatical_number = int(input("Please enter grammatical number: "))
    tense = int(input("Is the tense past(1), present(2), or future(3) tense (the numbers next to the tenses represent the input)? "))
    deter = get_determiner(grammatical_number)  
    noun = get_noun(grammatical_number)
    verb = get_verb(grammatical_number, tense)
    print(f"{deter.capitalize()} {noun} {verb}.")'''

    print(get_determiner(1), get_noun(1), get_verb(1, "past")) #, get_preposition(), get_prepositional_phrase())
    print(get_determiner(2), get_noun(2), get_verb(2, 'past'))
    print(get_determiner(1),get_noun(1), get_verb(1, 'present'))
    print(get_determiner(2),get_noun(2), get_verb(2, 'present'))
    print(get_determiner(1),get_noun(1), get_verb(1, 'future'))
    print(get_determiner(2),get_noun(2), get_verb(2, 'future'))
main()