##########
Public API
##########

..  TODO: describe the public API here
    Include public structures, modules, traits, etc
    Include an example of how these could be used for a simple TTT game

This section describes the public API of the library. The provided types and
functions are used by other applications to create Tic Tac Toe games. The legend
shown in :numref:`uml-public-api-diagram-legend` is used for the type diagrams
in this section.

..  _uml-public-api-diagram-legend:
..  uml::
    :caption: Legend used for the type diagrams in this section.

    hide members

    package Module {

    }
    interface Trait
    class Struct {
        +field
        +method()
    }

    enum Enum {
        EnumVariant
    }

    show Struct members
    show Enum fields


An overview of the public types is shown in :numref:`uml-public-api-overview`.

..  _uml-public-api-overview:
..  uml::
    :caption: Public modules, structures, and other types.

    hide members

    package tic_tac_toe {
        class Game
        enum GameState
        class Board
        class Square
        enum SquareOwner
        class AIMove
    }

The library contains a single public module that holds the public types.


===========
Struct Game
===========
The Game structure is one of the central types provided by the crate. It contains
the state machine logic and the underlying game board. :numref:`uml-struct-game`
show the Game structure.

..  _uml-struct-game:
..  uml::
    :caption: The Game structure.

    hide empty fields

    class Game {
        +new()
        +board() -> Board
        +state() -> GameState
        +can_move(position) -> bool
        +do_move(position)
        +start_next_game()
    }

The Game structure uses a state machine to determine which player has the next
move or when the game is over. The state diagram is shown in
:numref:`uml-game-state-diagram`.

..  _uml-game-state-diagram:
..  uml::
    :caption: State diagram of a Tic Tac Toe game.

    hide empty description

    [*] --> PlayerXMove
    [*] --> PlayerOMove

    PlayerXMove --> PlayerOMove
    PlayerXMove --> PlayerXWin
    PlayerXMove --> CatsGame

    PlayerOMove --> PlayerXMove
    PlayerOMove --> PlayerOWin
    PlayerOMove --> CatsGame

When a new Game starts either player X or player O takes the first turn.
The players alternate making their moves until one of the end game conditions is
encountered. The player that did not have the first turn last game takes the
first turn next game.


..  rubric:: Member Details

new
    Creates a new Tic Tac Toe game.

board
    Gets the board associated with the game.

state
    Gets the current state of the game.

can_move
    Indicates if the square at the indicated position can be marked as owned.
    That is, if ``can_move()`` returns ``true`` then ``do_move()`` is guaranteed
    to not panic.

do_move
    Marks the indicated square as being owned by the current player. The state
    of the game is updated as a side effect of ``do_move()``.
    Panics if the indicated position is already owned if the game is over.

start_next_game
    Starts

..  rubric:: Trait Implementations

* Debug
* Clone (or Copy?)

..  TODO: which one does game implement?

..  rubric:: Related Requirements

* :doc:`../requirements/ttt-rules`
* :ref:`ref-game-state-management-story`
* :ref:`ref-players-take-turns-having-first-move-story`


==============
Enum Game Sate
==============
The game state enumeration

..  _uml-enum-game-sate:
..  uml::
    :caption: GameState enum

    hide empty methods

    enum GameState {
        PlayerXMove
        PlayerOMove
        PlayerXWin
        PlayerOWin
        CatsGame

        +is_game_over() -> bool
    }

..  TODO: is_game_over returns True for any of the Win or Cats Game values.


============
Struct Board
============

..  _uml-struct-board:
..  uml::
    :caption: The Board structure.

    hide empty fields

    class Board {
        +new(num_rows, num_columns)
        +get(row, column) -> Square
        +get_mut(row, column) -> Square
        +num_rows() -> i32
        +num_columns() -> i32
    }



=============
Struct Square
=============

..  _uml-struct-square:
..  uml::
    :caption: The Square structure.

    hide empty fields

    class Square {
        +owner() -> SquareOwner
        +set_owner(owner: SquareOwner)
    }


=================
Enum Square Owner
=================

..  uml::
    :caption: Enumeration for indicating a square's owner.

    hide empty methods

    enum SquareOwner {
        PlayerX
        PlayerO
        None
    }



==============
Struct AI Move
==============

See :doc:`ai-algorithms` for details on the algorithms.


..  uml::
    :caption: AIMove structure.

    hide empty fields

    class AIMove {
        +new(game, mistake_probability)
        +position() -> tuple
    }


..  rubric:: Related Requirements

* :ref:`ref-ai-player-story`
* :ref:`ref-ai-difficulty-settings-story`
