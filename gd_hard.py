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


def guess(sentence, time=2):
    word, sentence_guess = pick_word(sentence)
    print('\n%s\n' % sentence_guess)
    guess = interact('Guess')
    n = 0
    while n < time:
        if guess == word:
            print('\n%s\n' % 'YOU GOT IT!')
            return
        n += 1
        interact('Try again')
        if n == time:
            interact('Last chance')
    print('\n%s\n' % sentence)
    print('%s\n' % 'LEARN THEN HIT IT NEXT TIME!')


def main(file):
    quote = gd.get_quote_from_local(file)[0]
    guess(quote)


if __name__ == '__main__':
    main('%s/quotes.json' % os.path.dirname(os.path.abspath(__file__)))