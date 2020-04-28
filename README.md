# gooday 

gooday (abbr. of 'good day') is a tool to decorate your terminal login banner with quotes.

## Setup
```
$ git clone https://github.com/vjyq/gooday.git
$ cd gooday
$ bash install.sh
```

## More quotes?
I try to get quotes from [remote](https://www.azquotes.com/quote_of_the_day.html). My setup steps:
- in `install.sh`, comment `echo 'python '${PWD}'/gd.py' >> $HOME/.bash_profile` and uncomment `echo 'pyenv activate gooday...>> $HOME/.bash_profile`
- then, 
```
$ (init a virtualenv -- using pyenv here. I call it 'gooday'.)
$ git clone https://github.com/vjyq/gooday.git
$ pip install -r requirement.txt
$ bash install.sh
```
You could also append your fav quotes to `quotes.json`.

## Author
yuqing.ji@outlook.com