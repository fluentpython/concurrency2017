# concurrency
Example code for the workshop Modern Concurrency in Python

## Ideas

* Review speakerdeck talks

* Update vaurien tutorial

* Load UnicodeData into PostgreSQL to demo [aiopg](http://aiopg.readthedocs.io/en/stable/)

* [PEP-492: Coroutines with async and await syntax](https://docs.python.org/3/whatsnew/3.5.html#whatsnew-pep-492)

* [PEP-525: Asynchronous Generators](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep525)

* [PEP 530: Asynchronous Comprehensions](https://docs.python.org/3/whatsnew/3.6.html#pep-530-asynchronous-comprehensions)

### Benchmarking

#### ab: Apache Bench

https://www.petefreitag.com/item/689.cfm

https://serverfault.com/questions/274252/apache-ab-please-explain-the-output

http://infoheap.com/ab-apache-bench-load-testing/ (graphic output)

concurrency * timetaken * 1000 / done
              timetaken * 1000 / done


### Configuration notes

#### nginx

On Luciano's, Mac, these are the notes output by `brew install nginx`:

```
Docroot is: /usr/local/var/www

The default port has been set in /usr/local/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.

nginx will load all files in /usr/local/etc/nginx/servers/.

To have launchd start nginx now and restart at login:
  brew services start nginx
Or, if you don't want/need a background service you can just run:
  nginx
```

## References

https://speakerdeck.com/pycon2017/miguel-grinberg-asynchronous-python-for-the-complete-beginner

https://speakerdeck.com/1st1/await-and-asyncio-in-python-3-dot-6-and-beyond

https://glyph.twistedmatrix.com/2014/02/unyielding.html
