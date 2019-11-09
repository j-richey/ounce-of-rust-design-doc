.. index:: Travis CI, travis.yml

######################
Continuous Integration
######################
The Tic Tac Toe library uses the `Travis CI <https://travis-ci.com/>`_
continuous integration system to build and test every commit on a variety of
platforms. [#multios]_ This ensures potential problems are found as soon as possible.

The continuous integration system also enforces additional rules such as requiring
the project have fully documented public APIs and contain no unused code.

A ``.travis.yml`` included in the library's source code repository tells Travis CI
how to build and test the code. The `Travis CI Tutorial <https://docs.travis-ci.com/user/tutorial/>`_
provides a starting point on how to create the ``.travis.yml`` file.

The library's source code repository ``README.md`` file contains a link to the
Travis CI build page and includes a badge that indicates if the build is passing
or failing.


..  rubric:: Related Requirements

* :ref:`ref-stable-library-api-story`
* :ref:`ref-cross-platform-support-story`


..  rubric:: Footnotes

..  [#multios] See `Testing Your Project on Multiple Operating Systems <https://docs.travis-ci.com/user/multi-os/>`_.
