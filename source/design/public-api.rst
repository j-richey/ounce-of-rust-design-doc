##########
Public API
##########
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

    ' Hidden links are used to help with the diagram's layout.
    Module -[hidden] Trait
    Trait -[hidden] Struct
    Struct -[hidden] Enum

An overview of the major public types is shown in :numref:`uml-public-api-overview`.

..  _uml-public-api-overview:
..  uml::
    :caption: Major public modules, structures, and other types. Note: the
        module contains additional supporting types that are not shown here.

    hide members

    package tic_tac_toe {
        enum Owner
        enum State

        Game o-- Board
        Game *- State

        Board "1" *-- "n" Position
        Position o- Owner
        AIOpponent .> Game
    }

The library contains a single public module that holds the public types. The
naming conventions used in this library follow those described in the Rust API
Guidelines [#RustAPIGuidelines]_ per the :ref:`ref-idiomatic-rust-apis-story`
user story.

Each of the major and supporting types are described below.


.. index:: Game struct

===============
Game Management
===============
Game management is handled by the Game structure. This structure is one of the
central types provided by the library. It contains the state machine logic,
holds the underlying game board, and enforces the rules of Tic Tac Toe.
:numref:`uml-game-management` shows the Game structure along with the State
enumeration.

..  _uml-game-management:
..  uml::
    :caption: The Game structure and GameState enumeration.

    hide empty fields

    class Game {
        +new()
        +board() -> Board
        +state() -> State
        +free_positions() -> FreePositions
        +can_move(Position) -> bool
        +do_move(Position) -> Result<State, InvalidMoveError>
        +start_next_game() -> State
    }

    enum State {
        PlayerXMove
        PlayerOMove
        PlayerXWin[HashSet<Position>]
        PlayerOWin[HashSet<Position>]
        CatsGame

        +is_game_over() -> bool
    }

    class FreePositions << Iterator >> {
        +Item: Position
        +next() -> Option<Item>
    }


    class InvalidMoveError << Error >> {

    }

A state machine is used determine which player has the next move or when the game
is over. The state diagram is shown in :numref:`uml-game-state-diagram`.

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

When a new game starts either player X or player O takes the first turn.
The players alternate making their moves until one of the end game conditions is
encountered. The player that did not have the first turn last game takes the
first turn next game.

-----------
Struct Game
-----------
Members of the Game structure are as follows:

new()
    Creates a new Tic Tac Toe game structure. Note: use ``start_next_game()`` for
    playing consecutive games to ensure each player gets to start the game.

board()
    Gets the board associated with the game.

state()
    Gets the current state of the game.

free_positions()
    Gets an iterator that iterates the free positions that do not have an owner
    and thus can be provided to ``do_move()``. When the game is over there are no
    free positions.

can_move()
    Indicates if the square at the indicated position can be marked as owned.
    That is, if ``can_move()`` returns ``true`` then ``do_move()`` is guaranteed
    to not panic.

do_move()
    Marks the indicated square as being owned by the current player. The state
    of the game is updated as a side effect of ``do_move()``.
    Panics if the indicated position is already owned or if the game is over.

start_next_game()
    Starts the next game by resetting the state machine ensuring the player who
    went second last game goes first next game.


..  rubric:: Trait Implementations

* Clone [#clonecopy]_


..  rubric:: Related Requirements

* :doc:`../requirements/ttt-rules`
* :ref:`ref-game-state-management-story`
* :ref:`ref-players-take-turns-having-first-move-story`


---------------------
Struct Free Positions
---------------------


..  rubric:: Trait Implementations

* Iterator


-------------------------
Struct Invalid Move Error
-------------------------


..  rubric:: Trait Implementations

* Error



.. index:: Sate enum

---------
Enum Sate
---------
The game state enumeration contains a variant for each possible game state
described in :numref:`uml-game-state-diagram` along with some additional helper
methods.

PlayerXMove
    Player X's turn to mark an empty square.

PlayerOMove
    Player O's turn to mark an empty square.

PlayerXWin[HashSet<position>]
    Player X has won the game. The victory sets that contributed to the win are
    provided as the enum value.

PlayerOWin[HashSet<position>]
    Player O has won the game. The victory sets that contributed to the win are
    provided as the enum value.

CatsGame
    The game has ended in a draw where there are no winners.

is_game_over()
    Indicates if the state represents one of the game over states. That is,
    if either player has won or it is a cat's game then ``true`` is returned;
    otherwise, ``false`` is returned.


..  rubric:: Trait Implementations

* Clone
* Debug
* Eq


..  rubric:: Related Requirements

* :ref:`ref-know-victory-squares-story`


.. index:: Board struct

==========
Board Data
==========
The board structure models a Tic Tac Toe game board. It holds the individual
squares of the board and provides functions to access and iterate over the
squares. The board and square structures along with supporting types are shown
in :numref:`uml-struct-board`.


..  _uml-struct-board:
..  uml::
    :caption: The Board structure and supporting types.

    hide empty fields
    hide empty methods

    class Board {
        +new(Size)
        +size() -> Size
        +contains(Position) -> bool
        +get(Position) -> Option<&Owner>
        +get_mut(Position) -> Option<&mut Owner>
        +iter() -> Iter
    }

    class Iter << Iterator >> {
        +Item: (Position, Owner)
        +next() -> Option<Item>
    }

    class Size {
        +rows: usize
        +columns: usize
    }

    class Position {
        +row: usize
        +column: usize
    }

    enum Owner {
        PlayerX
        PlayerO
        None
    }

    ' Hidden links are used to help with the diagram's layout.
    Board -[hidden]- Size
    Size -[hidden] Position
    Position -[hidden] Owner

------------
Struct Board
------------
Data structure representing the Tic Tac Toe board. Provides multiple ways to
access individual squares.

new()
    Constructs a new board.

size()
    Gets the size of board, that is the number of rows and columns.
    Note: boards are always square.

get()
    Gets the square at the indicated position. Panics if requested position is
    outside the size of the board.

get_mut()
    Gets a mutable square at the indicated position. Panics under the same
    situations as get().

iter()
    Gets an iterator that iterates over all the squares in the board.


The board structure also implements the Display trait. This provides a formatted
output of the board and is suitable for use in simple console applications or
debugging purposes. An example of the boards display is shown in
:numref:`code-example-board-display`.

..  _code-example-board-display:
..  code-block:: text
    :caption: Example board display output.

    +---+---+---+
    | X | O | O |
    +---+---+---+
    | O | X |   |
    +---+---+---+
    | X |   | X |
    +---+---+---+


..  rubric:: Trait Implementations

* Display
* Clone

-----------
Struct Iter
-----------
Implements the iterator trait for iterating over all the positions of the board.

next()
    Gets the next position in the board, or None if the end of the board has been
    reached.

.. TODO: Remove the following paragraph:

The board structure provides several ways to iterate over board's squares. [#iterators]_
Helper types that implement the Iterator trait are used to provide this support.




-----------
Struct Size
-----------
The size structure represents the size of the board in number of rows and columns.

rows
    The number of rows in the board.

columns
    The number of column in the board.


..  rubric:: Trait Implementations

* Debug
* Copy
* Clone
* From<(usize, usize)>
* Eq
* Hash


---------------
Struct Position
---------------
The position structure represents a specific board position denoted by row and
column.

row
    The row associated with the position.

column
    The column associated with the position.


..  rubric:: Trait Implementations

* Debug
* Copy
* Clone
* From<(usize, usize)>
* Eq
* Hash


.. index:: Owner enum

----------
Enum Owner
----------
The owner enumeration indicates which player owns a square, if any.

PlayerX
    Player X owns the square.

PlayerO
    Player O owns the square.

None
    No player owns the square.


..  rubric:: Trait Implementations

* Default
* Debug
* Copy
* Clone
* Eq
* Hash


..  TODO:
    * Remove FreeSquares and VictorySets from this
    * Make a WinSquares structure thing.
      * It contains all the winning squares -> can somehow get an iterator to these
      * Why not just a vector?
    * This is part of the game state, so must be cloned and equality comparable.
    * Clean up AI pesudo code.


.. index:: AIOpponent struct

===========
AI Opponent
===========
The AI opponent structure represents a move by an AI player. The AI move structure is
shown in :numref:`uml-struct-ai-move`.

..  _uml-struct-ai-move:
..  uml::
    :caption: AI Opponent structure.

    hide empty fields

    class AIOpponent {
        +new(mistake_probability)
        +get_move(Game) -> Position
    }


See :doc:`ai-algorithms` for details on how the AI selects a position.

..  rubric:: Member Details

new()
    Constructs a new AI move using the provided game and a given probability of
    making a mistake. Panics if the game is over.

position()
    Gets the position selected by the AI player based on the previously provided
    game.


..  rubric:: Trait Implementations

* Debug


..  rubric:: Related Requirements

* :ref:`ref-ai-player-story`
* :ref:`ref-ai-difficulty-settings-story`



..  rubric:: Footnotes

..  [#RustAPIGuidelines] See the [Rust-API-Guidelines]_ for details.

..  [#clonecopy] Rust's clone and copy traits both serve to duplicate an object but
        each goes about duplication in a different manner. Copy performs an operation
        similar to ``memcpy`` where it just copies the bits of the object. Alternately,
        Clone explicitly duplicates the object giving the programmer control over
        what parts are cloned. For details see the discussion in
        `Trait std::clone::Clone <https://doc.rust-lang.org/std/clone/trait.Clone.html>`_.

..  [#iterators] Rust's standard library documentation states "Iterators are
        heavily used in idiomatic Rust code, so it's worth becoming familiar
        with them." For details see [Rust-Crate-std]_.
