.. index:: API, application programming interface

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

    package open_ttt_lib {
        enum Owner
        enum State

        Game *-- Board
        Game *-- State

        Board "1..*" *-- Position
        Board "1..*" *-- Owner
        Game <. AIOpponent
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
:numref:`uml-game-management` shows the Game structure and other types related
to management of Tic Tac Toe games.

..  _uml-game-management:
..  uml::
    :caption: The Game structure contains a State and a Board.

    hide empty fields
    hide empty methods

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

    Game *-- Board
    Game *-- State
    FreePositions --[hidden] InvalidMoveError


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
    Gets an iterator over the free positions that do not have an owner and thus
    can be provided to ``do_move()``. When the game is over there are no free
    positions.

can_move()
    Indicates if the square at the indicated position can be marked as owned.
    That is, if ``can_move()`` returns ``true`` for a given position then
    ``do_move()`` is guaranteed to be successful.

do_move()
    Marks the indicated square as being owned by the current player. The state
    of the game is updated as a side effect of ``do_move()`` and the new state
    of the game is returned. An error is returned if the position is already
    owned or if the game is over.

start_next_game()
    Starts the next game by resetting the state machine ensuring the player who
    went second last game goes first next game. This can be called at any time
    even if the current game is not over. The new state of the game is returned.


..  rubric:: Trait Implementations

* Clone [#clonecopy]_


..  rubric:: Related Requirements

* :doc:`../requirements/ttt-rules`
* :ref:`ref-game-state-management-story`
* :ref:`ref-players-take-turns-having-first-move-story`


.. index:: Sate enum

---------
Enum Sate
---------
The game state enumeration contains a variant for each possible game state
described in :numref:`uml-game-state-diagram` along with some additional helper
methods.

PlayerXMove
    Player X's turn to mark a free position.

PlayerOMove
    Player O's turn to mark a free position.

PlayerXWin[HashSet<position>]
    Player X has won the game. The set of positions that contributed to the win
    are provided as the enum value.

PlayerOWin[HashSet<position>]
    Player O has won the game. The set of positions that contributed to the win
    are provided as the enum value.

CatsGame
    The game has ended in a draw where there are no winners.

is_game_over()
    Indicates if the state represents one of the game over states. That is,
    if either player has won or it is a cat's game then ``true`` is returned;
    otherwise, ``false`` is returned.

The set of positions provided to ``PlayerXWin`` and  ``PlayerOWin`` contain all
the positions that contributed to the victory. Usually, there will be three items
in this set representing a row, column, or diagonal. However, there are some
situations as :numref:`fig-example-wining-games` where more than three squares
can contribute to a victory.

..  rubric:: Trait Implementations

* Clone
* Debug
* Eq


..  rubric:: Related Requirements

* :ref:`ref-know-victory-squares-story`


.. index:: FreePositions struct

---------------------
Struct Free Positions
---------------------
An iterator over free positions that do not have an owner. [#iterators]_

next()
    Gets the next free position in the board, or None once all the free positions
    have been returned.


..  rubric:: Trait Implementations

* Iterator


.. index:: InvalidMoveError struct

-------------------------
Struct Invalid Move Error
-------------------------
Used to indicate moving to the indicated position is invalid. This could be due
to the position being owned or the game being over.

..  rubric:: Trait Implementations

* Error


.. index:: Board struct

==========
Board Data
==========
The board structure models a Tic Tac Toe game board. It maps the individual
positions to owners of the position. It provides functions to access and iterate
over each position. The board and square structures along with supporting types
are shown in :numref:`uml-struct-board`.


..  _uml-struct-board:
..  uml::
    :caption: The Board structure and supporting types.

    hide empty fields
    hide empty methods

    class Board {
        +new(Size)
        +size() -> Size
        +contains(Position) -> bool
        +get(Position) -> Option<Owner>
        +get_mut(Position) -> Option<mut Owner>
        +iter() -> Iter
    }

    class Iter << Iterator >> {
        +Item: (Position, Owner)
        +next() -> Option<Item>
    }

    class Position {
        +row: i32
        +column: i32
    }

    enum Owner {
        PlayerX
        PlayerO
        None
    }

    class Size {
        +rows: i32
        +columns: i32
    }

    Board "1..*" *-- Position
    Board "1..*" *-- Owner
    Board *-- Size


------------
Struct Board
------------
Data structure representing the Tic Tac Toe board. Provides multiple ways to
access individual squares.

new()
    Constructs a new board based on the given size. Panics if the size is less
    than one row and one column.

size()
    Gets the size of board, that is the number of rows and columns.

get()
    Gets the owner of the provided position. None is returned if requested
    position is outside the size of the board.

get_mut()
    Gets a mutable reference ot the owner at the indicated position. This allows
    the owner of the position to be changed. None is returned if requested
    position is outside the size of the board.

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


.. index:: Iter struct

-----------
Struct Iter
-----------
Implements the iterator trait for iterating over all the positions and owner
pairs of the board.

next()
    Gets a tuple containing the next position and owner of that position. None
    is returned if the end of the board has been reached.


.. index:: Size struct

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


.. index:: Position struct

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
The owner enumeration indicates which player owns a position, if any.

PlayerX
    Player X owns the position.

PlayerO
    Player O owns the position.

None
    No player owns the position.


..  rubric:: Trait Implementations

* Default
* Debug
* Copy
* Clone
* Eq
* Hash


.. index:: AIOpponent struct

===========
AI Opponent
===========
The AI opponent structure represents a computer controlled AI player. The AI
opponent structure is shown in :numref:`uml-struct-ai-opponent`.

..  _uml-struct-ai-opponent:
..  uml::
    :caption: AI Opponent structure.

    hide empty fields

    class AIOpponent {
        +new(mistake_probability)
        +get_move(Game) -> Option<Position>
    }


See :doc:`ai-algorithms` for details on how the AI selects a position.

..  rubric:: Member Details

new()
    Constructs a new AI opponent. The mistake probability indicates how likely
    the AI will fail to consider various situations. A value of 0.0 makes the
    AI play a perfect game. A value of 1.0 causes the AI to always pick a random
    position. Values less than 0.0 are set to 0.0 and values greater than
    1.0 are set to 1.0.

get_move()
    Gets the position the AI opponent wishes to move based on the provided game.
    None is returned if the game is over. The AI opponent never tries to select
    an invalid position, that is a position that is not free.


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
