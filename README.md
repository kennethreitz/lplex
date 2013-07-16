lplex
=====

This is a simple CLI for sending messages to logplex.

You should be able to just stick it in a directory and go:

    $ git clone https://github.com/kennethreitz/lplex.git && cd lplex
    $ make
    $ ./lplex

You can then move `lplex` and `lplex.zip` wherever you like.


Usage
-----

Configure logplex with the disired prefix and token:

    $ lplex init TOKEN

Send a message:

    $ lplex test

Logplex output of all above:

    2013-07-16T07:44:15+00:00 app[python-logplex]: test

Configuration
-------------

By default, `lplex` requires that its distro (`lplex.zip`) is next to the executable. This is configurable with the `LPLEX_DISTRO_PATH` environment variable.

    $ export LPLEX_DISTRO_PATH=/tmp/bpwatch.zip

