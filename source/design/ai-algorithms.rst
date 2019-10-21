.. index:: depth first search, AI player

##################################
Artificial Intelligence Algorithms
##################################
The AI algorithms are responsible for picking a square to place the AI player's mark. [#AIName]_
It does this by doing a depth first search for all possible game outcomes based
on the current state of the game board. An example is shown in
:numref:`fig-ai-depth-first-search-example`.

..  _fig-ai-depth-first-search-example:
..  figure:: img/ai-depth-first-search-example.*
    :alt: AI search tree example.

    Example dept first search algorithm looking for possible Tic Tac Toe game
    outcomes. The AI player is playing as X and the opponent is playing as O.
    The possible outcomes of selecting a particular square are marked with W for
    win, L for loss, and C for cat's game.

The algorithm selects a free position then traverses the tree looking one of the
end game conditions: win, loss, or cat's game. Once the end of the game is found,
the result is propagated up the tree. The algorithm assumes the opponent will
play a perfect game. That is, if a specific position leads for both a win for the
opponent (a loss for the AI player) and a cat's game, the algorithm marks that
position as a loss.

Once all possibilities have been searched, the algorithm picks the position that
lead to the best outcome. Winning positions are picked over cat's games, and
cat's games are picked over losses. Additionally, if there are multiple positions
with the same outcome, one is picked at random to ensure the game appears more
natural to human players. [#FunAI]_

The depth search algorithm can see to the end of the game, thus it cannot be beat.
The best possible outcome is a cat's game. Therefore, to give human players a
chance to win, the algorithm sometimes fails to consider one of the outcomes.
The probability of making a mistake is configurable.


================
AI Logic Details
================
There are two main parts to the AI's logic. A high level part examines the
state of the game and picks the best move and a low level part that
evaluates the outcome of picking a specific position. The best way
to examine this logic is to look at some pseudo code.

The pseudo code in :numref:`code-ai-move` examines the overall state of the game
and returns the best position for the AI to place its mark.

..  _code-ai-move:
..  code-block:: python
    :caption: Pseudo code for examining game state and picking the best move.

    def ai_move(game, mistake_probability):
        # Determine which player the AI is playing as.
        ai_player = get_ai_player(game.state())

        # For each free square, evaluate the consequences of using
        # that square. The outcome for each position and the position
        # is recorded.
        outcomes = []
        for square in game.board().free_squares():
             outcomes = evaluate_position(
                square.position, game, ai_player, mistake_probability)
             outcomes.push((outcome, square.position))

        # Return the best position based on the outcomes.
        return best_position(outcomes)

There are several notable items in this pseudo code. The ``get_ai_player()``
function indicates which player the AI is playing as, X or O, based on the
current state of the game. [#aiplayernew]_ It panics if the game is over. The
resulting variant is passed to the lower level ``evaluate_game()`` function.

The ``best_position()`` function takes the collection of outcome and position
tuples and picks a position with the best outcome. The ordering of outcomes from
best to worst are: ``Win``, ``CatsGame``, ``Unknown``, ``Loss``. A cats game is
considered better than unknown as the AI rather have the game end in a draw than
risk a loss. If there are multiple positions with the same outcome, one of the
positions is picked at random.

The ``evaluate_position()`` function is responsible for evaluate a specific position.
:numref:`code-evaluate-position` shows the pseudo for this function.

..  _code-evaluate-position:
..  code-block:: python
    :caption: Pseudo code for evaluating a specific position.

    def evaluate_position(position, game, ai_player, mistake_probability):
        # Check to see if the AI should make a mistake given the
        # mistake probability. If so, don't consider this position.
        if should_make_mistake(mistake_probability):
            return Outcome.Unknown

        # Clone the game so this function can try out the move without
        # modifying the original game.
        game = game.clone()
        game.do_move(square.position)

        # Check to see if the game is over. If so, return the
        # outcome of the game from the AI's perspective,
        # e.g. win, loss, or cat's game.
        if game.state().is_game_over():
            return game_state_to_ai_outcome(game.state(), ai_player)

        # The game is not over, to evaluate each of the remaining
        # free squares. Note: the game automatically takes care of
        # switching between player X's and player O's turn.
        outcomes = []
        for square in game.board().free_squares():
            outcome = evaluate_position(
                square.position, game, ai_player, mistake_probability)
            outcomes.push(outcome)

        # The AI assumes the other player plays a perfect game,
        # so return the worst outcome that was found.
        return worst_outcome(outcomes)

The ``should_make_mistake()`` function takes the mistake probability and returns
``true`` if the algorithm should skip examining this branch of the tree. The
``Unknown`` outcome is used for parts of the tree that are skipped.

The ``game_state_to_ai_outcome()`` function is responsible for converting one of
the game over states into an AI outcome. That is: one of ``Win``, ``Loss``, or
``CatsGame``. It uses the ``ai_player`` to know what player the AI is playing as.

The ``worst_outcome()`` function takes the outcomes from all the positions and
returns the worst possible one for the AI player. The ordering of outcomes
returned are: ``Loss``, ``CatsGame``, ``Win``, ``Unknown``. Unknown is returned
only if other information was not obtained about the position.

..  Note::
    The ordering of outcomes used by ``worst_outcome()`` is different than
    different than ``best_position()``.


..  rubric:: Related Requirements

* :ref:`ref-ai-player-story`
* :ref:`ref-ai-difficulty-settings-story`


..  rubric:: Footnotes

..  [#AIName] The name of the AI player is Robbert, or Bob for short.

..  [#FunAI] One of the challenges of creating AI for video games is the AI needs
        to be fun. An AI that picked the same square every time would not be fun!
        See [Buckland-2004]_ for a discussion on making game AI fun.

..  [#aiplayernew] Rust enums support methods, so ``get_ai_player()`` could actually be
        implemented as ``fn new(state: GameState) -> AIPlayer`` for the
        ``AIPlayer`` enum.
