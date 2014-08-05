wilde
===========

Sometimes citing the program committee members pays off !

installation
-----------

You need tor installed (be aware that this script queries *Google Scholar*, abusing it violates the eula).

```sudo apt-get install tor```

You also need the ```stem``` and ```socksipy``` python modules.

```sudo apt-get install python-stem python-socksipy```

usage
-----------

*wilde* uses the excellent [scholar.py](https://github.com/ckreibich/scholar.py), check its readme for the available options. The only difference is that you have to feed smart-cites with a list of names instead of a single one, the list filename must be the first argument, after that you can specify all the *scholar.py* options you want.

example
----------

In the folder examples you can find the names of the program committee of [NDSS15](http://www.internetsociety.org/events/ndss-symposium-2015/program-committee). An use case would be:

```
./wilde.py examples/ndss -c 3 -t -s "android mobile malware" > results.md
```

This will produce for every member, the 3 most cited articles (```-c 3```) containing in the title (```-t```) some (```-s```) of the words *android, mobile, malware*.

The output is stored in a Github Flavored Markdown formatted file (```> result.md```) for you to read. You can check the output [here](https://github.com/enricobacis/wilde/blob/master/examples/results.md).
