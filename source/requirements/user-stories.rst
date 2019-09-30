############
User Stories
############

..  Note: there is a user story template at the bottom of this file.

User stories are informal descriptions of the software system features. These
stories are written from the perspective of the users roles described in
:doc:`../overview/users`. The general format is:

  As a <user> I want <goal/desire> so that <benefit>.

This section contains the user stories identified for this project.


======================
AI Difficulty Settings
======================
| As a Tic Tac Toe player,
| I want different AI difficulty settings,
| so I can play a challenging yet winnable game of Tic Tac Toe.

.. rubric:: Acceptance Criteria

* The difficulty for AI players can be configured by the Rust application developer.


======================
Maximum AI Update Time
======================
| As a Rust application developer,
| I want the AI to block for less than 1/300 a second when picking its next move,
| so it does not block my rendering thread making my animations choppy.

.. rubric:: Acceptance Criteria

* There is a benchmark that measures the worst case time the AI blocks while
  picking the next move.
* The benchmark is run on the lowest supported hardware.

.. rubric:: Notes

* It is OK for the AI to spread the update over multiple iterations if necessary
  to meet this requirement.
* Limited resources may prevent testing on a verity of platforms. Therefore,
  meeting this requirement on any one platform is considered successful.
* 1/300 a second is ten times faster than what is considered the minimum
  acceptable frame rate for an interactive game and twice as fast as the 144Hz
  refresh rate of some modern monitors.


=======================
Getting Started Example
=======================
| As a Rust application developer,
| I want an example of getting started with the library,
| so I can quickly start integrating the library into my application.

.. rubric:: Acceptance Criteria

* There is a runnable example of using the library.
* The example is in a prominent location such as library's documentation.


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


===================
Idiomatic Rust APIs
===================

| As a Rust application developer,
| I want the library to provide idiomatic Rust APIs,
| so the library works in natural and familiar way.

.. rubric:: Acceptance Criteria

* An experienced Rust programmer code reviews and signs off on the library's API.

.. rubric:: Notes

This can be a subjective subject subject. However, providing an idiomatic Rust
API is important to fulfilling the :ref:`ref-learn-about-rust-objective` objective.


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


======================
Available on crates.io
======================
| As a Rust application developer,
| I want the library to be on `crates.io <https://crates.io/>`__,
| so that I can easily incorporate it into my Rust based application with Cargo.

.. rubric:: Acceptance Criteria

* The library can be downloaded from `crates.io <https://crates.io/>`__.
* The library can be obtained by simply specifying it as a dependency in Cargo.toml.


==========================
Source Available on GitHub
==========================
| As a Rust application developer,
| I want the library's source code to be available on `GitHub <https://github.com/>`__
| so I can view the source code to get a better understanding of how the library works.

.. rubric:: Acceptance Criteria

* The library's source code is hosted on a public GitHub repository.
* The library's tags match the releases on crates.io.


==================
Permissive License
==================
| As a Rust application developer,
| I want the library to be licensed under a permissive open source license,
| so that I can incorporate the library into my application without worrying about legal issues.

.. rubric:: Acceptance Criteria

* The library is released under a permissive open source license. The MIT license
  fulfills this requirement.



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
