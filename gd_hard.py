import gd
import nltk
import os
import random


def segment_sentence(sentence):
    try:
        return nltk.word_tokenize(sentence)
    except LookupError:
        nltk.download('punkt')
        return nltk.word_tokenize(sentence)


def pick_word(sentence):
    wlist = segment_sentence(sentence)
    i = random.randint(0, len(wlist)-1)
    word = wlist[1]
    return word, sentence.replace(word, '___')


def interact(tip):
    return input('%s: ' % tip)


def trick(word, sentence, n):
    if n == 0:
        guess = interact('Last chance')
        if guess != word:
            print('\n%s\n' % sentence)
            print('%s\n' % 'LEARN THEN HIT IT NEXT TIME!')
            return
        print('\n%s\n' % 'YOU GOT IT!')
    if n > 0:
        guess = interact('Guess')
        if guess == word:
            print('\n%s\n' % 'YOU GOT IT!')
            return
        return trick(word, sentence, n-1)


def main(file):
    quote = gd.get_quote_from_local(file)[0]
    word, quote_guess = pick_word(quote)
    print('\n%s\n' % quote_guess)
    trick(word, quote, 2)


if __name__ == '__main__':
    main('%s/quotes.json' % os.path.dirname(os.path.abspath(__file__)))