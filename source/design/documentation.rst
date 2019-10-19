#############
Documentation
#############
The Tic Tac Toe crate provides API documentation to help developers use the
functionality provided by the crate. This section describes how the documentation
is put together and published.


======================
Documentation Comments
======================
Rust supports storing the crate's documentation along side the source code using
documentation comments. [#usefuldocs]_ Each public item provided by the crate
has corresponding documentation that describes why the item should be used.

Common sections include **examples**, **panics**, and **errors**. In particular,
Rust encourages every public type to have a corresponding example. Additionally
examples are exercised as part of the library's tests which help developers detect
if a public API has changed.


..  rubric:: Related Requirements

* :ref:`ref-stable-library-api-story`
* :ref:`ref-detailed-library-documentation-story`
* :ref:`ref-getting-started-example-story`


==========
Change Log
==========
The library's source code repository includes a ``CHANGELOG.md`` file that describes
user visible changes to the library. For each release a new entry is added to
the change log that describes changes users might care about. [#changelog]_
The change log also mentions how the library follows semantic visioning. [#rfc1105]_


..  rubric:: Related Requirements

* :ref:`ref-stable-library-api-story`


=======
Hosting
=======
The crate's ``Cargo.toml`` uses the default ``documentation`` value which means
when the crate is uploaded to crates.io, https://docs.rs automatically builds
and hosts the crate's documentation.

..  rubric:: Related Requirements

* :ref:`ref-detailed-library-documentation-story`


..  rubric:: Footnotes

..  [#usefuldocs]  See the
    `Making Useful Documentation Comments <https://doc.rust-lang.org/book/ch14-02-publishing-to-crates-io.html#making-useful-documentation-comments>`_
    section in the Rust Book which is part of [Rust-Docs]_. Additionally, there
    is a `Documentation <https://rust-lang-nursery.github.io/api-guidelines/documentation.html>`_
    section in the [Rust-API-Guidelines]_.

..  [#changelog] See https://keepachangelog.com/ for the format of the `CHANGELOG.md`
        file and additional details / motivation for keeping a change log.

..  [#rfc1105] `Rust RFC 1105 API Evolution <https://github.com/rust-lang/rfcs/blob/master/text/1105-api-evolution.md>`_
        describes semantic visioning as understood by Rust.
