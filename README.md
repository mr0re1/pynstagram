# Pynstagram

Pynstagram is small python library that allows you to upload photo to [Instagram](www.instagram.com).

```python
import pynstagram

with pynstagram.client('username', 'password') as client:
	client.upload('~/funny_kittens_photos/31415.jpg', 'mi-mi-mi')
```

___Disclaimer: 
Pynstagram uses private API of Instagram, there is no guaranty that this library will work in the future.
Instagram may not like that you use private API.___

Many kudos to [Lance G. Newman](http://lancenewman.me/) for his [article](http://lancenewman.me/posting-a-photo-to-instagram-without-a-phone/).