##############
Current System
##############

Tic Tac Toe is a game where two players, X and O, take turns placing their mark
in a gird. The first player to get three marks in a row, column, or diagonal
wins the game. The game can also end in a draw, known as a "cat's game".
An example of a Tic Tac Toe game is shown in :numref:`fig-tic-tac-toe-example-game`.

..  _fig-tic-tac-toe-example-game:
..  figure:: img/tic-tac-toe-example-game.*
    :alt: An example Tic Tac Toe game

    An example game of Tic Tac Toe where player X is victorious.

================
Pencil and Paper
================
Traditionally Tic Tac Toe is played by two players using pencil and paper.
This is a quick and convenient way to play with a friend. However, this does not
allow for single player games. For people stuck on an airplane this can lead to
extreme boredom!


==============
Computer Games
==============
Tic Tac Toe computer games allow for single player versions of the game. There
are many versions of the game created over the years.
:numref:`fig-ttt-screen-shot` shows a screen shot from one of the classic
Tic Tac Toe games.

..  _fig-ttt-screen-shot:
..  figure:: img/ttt-screen-shot.*
    :alt: Screen shot of a Tic Tac Toe computer game.

    Screen shot of `Tic Tac Toe <https://www.imaginaryphase.com/ttt.html>`__
    developed by James Richey.

These games can be developed as stand alone applications or can be created with
the help of supporting libraries.


====================
Supporting Libraries
====================
To support the creation of Tic Tac Toe games many libraries have been developed
to provide common functionality. Searching Rust's package registry,
`<https://crates.io/>`__, reveals several such libraries including ``ultimate-ttt``,
``zero_sum``, and ``minimax``.

With the wide variety of libraries available, for both Rust and other languages,
there is likely one that meets the needs of Tic Tac Toe application developers.
However, due to the :ref:`ref-learn-about-rust-objective` objective, is worth
going through the effort to create another Tic Tac Toe library.
