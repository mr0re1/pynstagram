[![Build Status](https://travis-ci.org/mr0re1/pynstagram.svg?branch=master)](https://travis-ci.org/mr0re1/pynstagram)
[![PyPi](https://img.shields.io/pypi/v/pynstagram.svg)](https://pypi.python.org/pypi/pynstagram)

# Pynstagram

Pynstagram is small python module and CLI tool that allows you to upload photo to [Instagram](http://www.instagram.com).

## CLI tool

```sh
pynstagram -u username -f ~/kittens/31415.jpg -t '#meow'
```

## Module

```python
import pynstagram

with pynstagram.client('username', 'password') as client:
	client.upload('~/kittens/31415.jpg', '#meow')
```

## Installation

```sh
pip install pynstagram
```

### Usage tips

To use a line break in caption text you need to properly escape `\n` symbol. There are few options:

* Use `$' . . . '` escaping.

```sh
pynstagram -u username -f ~/kittens/31415.jpg -t $'line\nbreak'
```

* Use multiline argument.

```sh
pynstagram -u username -f ~/kittens/31415.jpg -t "line
> break"
```


___Disclaimer: 
Pynstagram uses private API of Instagram, there is no guaranty that this library will work in the future.
Instagram may not like that you use private API.___

Many kudos to [Lance G. Newman](http://lancenewman.me/) for his [article](http://lancenewman.me/posting-a-photo-to-instagram-without-a-phone/).
