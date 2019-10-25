############
Distribution
############
This section describes how the Tic Tac Toe library is shared with others.


.. index:: MIT license

===========
MIT License
===========
The library's code is released under the MIT license. [#mitlicense]_ The MIT
license is simple and allows for use with open source, commercial, or private projects.

The library's source code repository contains a ``LICENSE.txt`` file that includes
the text of the MIT license. Additionally, the ``README.md`` file mentions the
this license.


..  rubric:: Related Requirements

* :ref:`ref-permissive-license-story`


.. index:: crates.io

=======================
Publishing to crates.io
=======================
Crates.io is the Rust community's package registry. Uploading the Tic Tac Toe
package to cargo.io allows others to easily obtain the library using the Rust
package manager, Cargo.

See `Publishing on crates.io <https://doc.rust-lang.org/cargo/reference/publishing.html>`_
for a step by step guide on how to publish a package. This includes a list of mandatory
metadata that ``Cargo.toml`` must contain and how to upload the package.

The library's source code repository ``README.md`` file contains a link to the
crates.io for the library.


..  rubric:: Related Requirements

* :ref:`ref-available-on-crates-io-story`


.. index:: GitHub

=================
GitHub Repository
=================
The library's source code is available on GitHub so others can clone and modify
the code as they wish. The repository is named after the library. Additionally,
the ``repository`` value in the packages's ``Cargo.toml`` file points to this
repository.

GitHub also takes care of the library's bug tracker.


..  rubric:: Related Requirements

* :ref:`ref-source-available-on-github-story`


..  rubric:: Footnotes

..  [#mitlicense] For details on the MIT license see
        `Choose an open source license - MIT License <https://choosealicense.com/licenses/mit/>`_.
