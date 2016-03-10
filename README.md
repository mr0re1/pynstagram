# Pynstagram

Pynstagram is small python module and CLI tool that allows you to upload photo to [Instagram](www.instagram.com).

## CLI tool

```sh
pynstagram -u username -p password -f ~/kittens/31415.jpg -t '#meow'
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


___Disclaimer: 
Pynstagram uses private API of Instagram, there is no guaranty that this library will work in the future.
Instagram may not like that you use private API.___

Many kudos to [Lance G. Newman](http://lancenewman.me/) for his [article](http://lancenewman.me/posting-a-photo-to-instagram-without-a-phone/).