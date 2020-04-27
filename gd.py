#coding:utf-8

import json
import os
import random


def get_quotes_from_local(file):
    with open(file) as f:
        return json.load(f)


def get_quotes_from_remote():
    pass


def get_quotes(file):
    return get_quotes_from_local(file)


def empty_file(file='/etc/motd'):
    if os.path.isfile(file):
        open(file, 'w').close()


def write_file(content, file='/etc/motd'):
    empty_file(file)
    with open(file, 'w') as f:
        f.write(content)


def main(file):
    quotes = get_quotes(file)
    i = random.randint(0, len(quotes)-1)
    quote = quotes[i]['quote']['text']
    author = quotes[i]['author']['name']
    write_file('\n"%s"\n- %s\n\n' % (quote, author))


if __name__ == '__main__':
    main('%s/quotes.json' % os.path.dirname(os.path.abspath(__file__)))