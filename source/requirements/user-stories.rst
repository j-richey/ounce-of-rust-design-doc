############
User Stories
############

..  Note: there is a user story template at the bottom of this file.

User stories are informal descriptions of the software system features. These
stories are written from the perspective of the users roles described in
:doc:`../overview/users`. The general format is:

  As a <user> I want <goal/desire> so that <benefit>.

This section contains the user stories identified for this project.


.. _ref-game-state-management-story:

=====================
Game State Management
=====================
| As a Rust application developer,
| I want the library to contain functionality for managing the state of the game,
| so I can focus on creating engaging user experiences.

.. rubric:: Acceptance Criteria

* The library exposes APIs for getting the current state and updating the state
  of the game. This includes functionality for checking the victory condition
  and determining the winner of the game, if any.

.. rubric:: Notes

The design details of the APIs are outside the scope of this requirements chapter.


.. _ref-know-victory-squares-story:

===============================================
Know Cells that Contributed to Player's Victory
===============================================
| As a Rust application developer,
| I want to know what cells contributed to the player's victory,
| so I can draw a line through them or mark them in a special color.

.. rubric:: Acceptance Criteria

* When a player has won the game there is a way to obtain the board's cells that
  contributed to the victory.


.. _ref-stable-library-api-story:

==================
Stable Library API
==================
| As a Rust application developer,
| I want the library to have a stable API,
| so that my application does not unexpectedly break if I use a different version of the library.

.. rubric:: Acceptance Criteria

* The library uses semantic versioning to clearly communicate when there are API
  changes. [#semver]_
* There are integration tests that help library developers detect if the
  library's API changes.


.. _ref-ai-player-story:

=========
AI Player
=========
| As a Tic Tac Toe player,
| I want to play against the computer,
| as I do not always have a friend to play with.

.. rubric:: Acceptance Criteria

* The library provides an AI player that Rust application developers can
  incorporate into their applications.


.. _ref-ai-difficulty-settings-story:

======================
AI Difficulty Settings
======================
| As a Tic Tac Toe player,
| I want different AI difficulty settings,
| so I can play a challenging yet winnable game of Tic Tac Toe.

.. rubric:: Acceptance Criteria

* The difficulty for AI players can be configured by the Rust application developer.

.. rubric:: Notes

The difficulty can be thought of as a probability of how likely the AI will make
a mistake.


.. _ref-players-take-turns-having-first-move-story:

========================================
Players Take Turns Having the First Move
========================================
| As a Tic Tac Toe player,
| I want to have the first move on the next game if I did not have the first move this game,
| so I have a better chance of winning the next game.

.. rubric:: Acceptance Criteria

* The game logic ensures the starting player alternates between games.

.. rubric:: Notes

The player who takes the first move has more wining possibilities than the
second player. [#WiningMoves]_


.. _ref-maximum-ai-update-time-story:

======================
Maximum AI Update Time
======================
| As a Rust application developer,
| I want the AI to block for less than one frame when picking its next move,
| so it does not block my rendering thread making my animations choppy.

.. rubric:: Acceptance Criteria

* There is a benchmark that measures the worst case time the AI blocks while
  picking the next move.
* How to run the benchmark is documented so developers can quickly evaluate this
  library to see if it meets their needs.

.. rubric:: Notes

Frame times can vary greatly depending on platform and application. For example,
an update time of one second might be just fine for a casual Tic Tac Toe game.
However, a Tick Tac Toe mini-game in a modern FPS is expected to take just a
fraction of the 1/144 second frame time. Therefore, providing the tools to allow
the Rust application developer to see if this library meets their needs is
sufficient to fulfill this requirement.


.. _ref-getting-started-example-story:

=======================
Getting Started Example
=======================
| As a Rust application developer,
| I want an example of getting started with the library,
| so I can quickly start integrating the library into my application.

.. rubric:: Acceptance Criteria

* There is a runnable example of using the library.
* The example is in a prominent location such as library's documentation.


.. _ref-detailed-library-documentation-story:

==============================
Detailed Library Documentation
==============================
| As a Rust application developer,
| I want detailed and thorough library documentation,
| so I can determine how to use the library from my specific needs.

.. rubric:: Acceptance Criteria

* All public modules and their members are documented using Rust's documentation
  comments.
* The documentation contains the typical sections such as **Panics** and **Errors**.
* The documentation is accessible from the internet, such as being hosted on
  `Docs.rs <https://docs.rs>`__.


.. _ref-idiomatic-rust-apis-story:

===================
Idiomatic Rust APIs
===================

| As a Rust application developer,
| I want the library to provide idiomatic Rust APIs,
| so the library works in natural and familiar way.

.. rubric:: Acceptance Criteria

* The Rust API Guidelines are consulted when designing the libraries API. [#RustAPIGuidelines]_
* An experienced Rust programmer code reviews and signs off on the library's API.

.. rubric:: Notes

This can be a subjective subject subject. However, providing an idiomatic Rust
API is important to fulfilling the :ref:`ref-learn-about-rust-objective` objective.


.. _ref-cross-platform-support-story:

======================
Cross Platform Support
======================
| As a Rust application developer,
| I want the library to work on a variety of platforms,
| so I can make Tic Tac Toe games for a wider use base.

.. rubric:: Acceptance Criteria

* The library is tested and verified on two different platforms such as
  Windows 10 and Linux.

.. rubric:: Notes

The use of platform specific code is minimized, however, the number of platforms
the library is tested on may be limited due to resource constraints.


.. _ref-available-on-crates-io-story:

======================
Available on crates.io
======================
| As a Rust application developer,
| I want the library to be on `crates.io <https://crates.io/>`__,
| so that I can easily incorporate it into my Rust based application with Cargo.

.. rubric:: Acceptance Criteria

* The library can be downloaded from crates.io.
* The library can be obtained by simply specifying it as a dependency in Cargo.toml.


.. _ref-source-available-on-github-story:

==========================
Source Available on GitHub
==========================
| As a Rust application developer,
| I want the library's source code to be available on `GitHub <https://github.com/>`__
| so I can view the source code to get a better understanding of how the library works.

.. rubric:: Acceptance Criteria

* The library's source code is hosted on a public GitHub repository.
* The library's tags match the releases on crates.io.


.. _ref-permissive-license-story:

==================
Permissive License
==================
| As a Rust application developer,
| I want the library to be licensed under a permissive open source license,
| so that I can incorporate the library into my application without worrying about legal issues.

.. rubric:: Acceptance Criteria

* The library is released under a permissive open source license. The MIT license
  fulfills this requirement.



..  rubric:: Footnotes

..  [#semver] See https://semver.org/ for details on semantic versioning.

..  [#WiningMoves] The player with the first move has about double the number of
        winning possibilities. For details see
        `Wikipedia's Tic-tac-toe page <https://en.wikipedia.org/wiki/Tic-tac-toe>`__.
..  [#RustAPIGuidelines] See the [Rust-API-Guidelines]_ for details.



..  User Story Template
    =====
    Title
    =====
    | As a <role>
    | I want <goal/desire>
    | so that <benefit>.

    .. rubric:: Acceptance Criteria

    * Item 1
    * Item 2

    .. rubric:: Notes

    Optional free form notes as necessary.
