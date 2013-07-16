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


Send a message:

    $ lplex hello world!
    
Send a message with a given token:

    $ lplex hello world! --token=$LOG_TOKEN --proc=lplex

Logplex output:

    2013-07-16T07:44:15+00:00 app[lplex]: hello world!

Configuration
-------------

By default, `lplex` requires that its distro (`lplex.zip`) is next to the executable. This is configurable with the `LPLEX_DISTRO_PATH` environment variable.

    $ export LPLEX_DISTRO_PATH=/tmp/lplex.zip

