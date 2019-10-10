##################################
Artificial Intelligence Algorithms
##################################

.. TODO:
    AI (Artificial Intelligence) Algorithms
    * Picks the move that results in the highest score, e.g. win, then cats game, then loss
    * If scores are equal, picks random spot of the equal spots (so game appears more random)
    * This algorithm is perfect, thus toning down the difficulty involves the AI
      randomly not looking at a path. The probability of not going down a path
      is based on the difficulty setting.

The AI algorithms are responsible for picking a position to place the AI player's mark. [#AIName]_
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

The dept search algorithm can see to the end of the game, thus it cannot be beat.
The best possible outcome is a cat's game. Therefore, to give human players a
chance to win, the algorithm sometimes fails to consider one of the outcomes.
The probability of making a mistake is configurable.


============
Example Code
============


..  code-block:: python
    :caption: searching the tree

    def ai_move(game, player_turn):
        if game.state.is_game_over():
            return game.state

        for square in game.board.free_squares():
            square.set_owner(player_turn)
            # TODO: switch who's turn it is
            # TODO: clone the game or the board.
            result = ai_move(game, player_turn)
            square.set_result(square)


..  rubric:: Footnotes

..  [#AIName] The name of the AI player is Robbert, or Bob for short.

..  [#FunAI] One of the challenges of creating AI for video games is the AI needs
        to be fun. An AI that picked the same square every time would not be fun!
        See [Buckland-2004]_ for a discussion on making game AI fun.
