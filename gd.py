#coding:utf-8

import json
import os
import random


def get_quote_from_local(file):
    with open(file) as f:
        quotes = json.load(f)
    i = random.randint(0, len(quotes)-1)
    quote = quotes[i]['quote']['text']
    author = quotes[i]['author']['name']
    return quote, author


def save_quote(file, quote, author):
    with open(file) as f:
        quotes = json.load(f)
    qlist = []
    for q in quotes:
        qlist.append(q['quote']['text'])
    if quote not in qlist:
        new_quote = {
            'author': {
                'name': author
            },
            'quote': {
                'text': quote
            }
        }
        quotes.append(new_quote)
        with open(file, 'w') as output:
            json.dump(quotes, output)


def get_quote_from_remote(file, url):

    from lxml import html
    import requests

    raw = requests.get(url)
    tree = html.fromstring(raw.content)
    raw_quote = tree.xpath('//*[@id="content"]/div/div[1]/div/ul/li[1]/div/p/a/text()')
    raw_author = tree.xpath('//*[@id="content"]/div/div[1]/div/ul/li[1]/div/div[1]/a/text()')
    quote = raw_quote[0]
    author = raw_author[0]
    save_quote(file, quote, author)


def get_quote(file, url):
    try:
        get_quote_from_remote(file, url)
    except:
        pass
    return get_quote_from_local(file)


def empty_file(file='/etc/motd'):
    if os.path.isfile(file):
        open(file, 'w').close()


def write_file(content, file='/etc/motd'):
    empty_file(file)
    with open(file, 'w') as f:
        f.write(content)


def main(file, url):
    quote, author = get_quote(file, url)
    write_file('\n"%s"\n- %s\n\n' % (quote, author))


if __name__ == '__main__':
    main('%s/quotes.json' % os.path.dirname(os.path.abspath(__file__)), 'https://www.azquotes.com/quote_of_the_day.html')