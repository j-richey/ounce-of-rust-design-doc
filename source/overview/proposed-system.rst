###############
Proposed System
###############
This project creates a Rust library that application developers can use to create
Tic Tac Toe games. The library contains common Tic Tac Toe functionality such as
game state management and single player artificial intelligence. The library
exposes this functionality through a well defined and documented public API.
The library is open source and is available in Rust's package repository
`<https://crates.io/>`__.

By using this library application developers can focus on making flashy graphics
or other unique Tic Tac Toe experience without worrying about the underlying game
logic and management.


===============================
Game State and Board Management
===============================
A common task of Tic Tac Toe games is managing the state of the game. This
includes knowing which player's turn it is, ensuring players cannot mark a
previously marked square, and checking for victory or draw conditions.


==========
AI Players
==========
The library allows single player Tic Tac Toe games to be created by providing
AI players. These players use artificial intelligence algorithms that pick a
square to place the AI player's mark. The application developer has control over
how difficult to win over the AI player.


======================
Available on crates.io
======================
The library is available on `<https://crates.io/>`__, the source code released
under a permissive open source license, and the API documentation is hosted
on a publicly accessible website.


============
Deliverables
============
The project deliverables are:

* ``open_ttt_lib`` crate. [#A]_
* API documentation. [#B]_
* Public source code repository with a tagged release.


..  rubric:: Footnotes

..  [#A] Future projects built around ``open_ttt_lib`` may use ``open_ttt`` as
         part of their crate name.

..  [#B] Popular places to host Rust API documentation include `<https://docs.rs/>`__
         and `<https://pages.github.com/>`__.
