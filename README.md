# README


Unfortunately, python3 is not available in RHEL 6.x. So please use python2.x.

First export the PYTHONPATH env:

```
 $ export PYTHONPATH=.:$PYTHONPATH
```

Now, install the dependencies:

```
 $ sudo pip install -r requirements.txt
```

Finnaly, you are able to run any script inside `scripts`.

Now we have few scripts inside scripts directory.

```
 $ python scripts/topology.py
```
