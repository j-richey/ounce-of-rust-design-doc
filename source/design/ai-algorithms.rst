##################################
Artificial Intelligence Algorithms
##################################

.. TODO:
    AI (Artificial Intelligence) Algorithms
    * Depth first search tree
    * Checks the state of the board: looks for end games: win, tie (cats game), loss
    * Picks the move that results in the highest score, e.g. win, then cats game, then loss
    * If scores are equal, picks random spot of the equal spots (so game appears more random)
    * This algorithm is perfect, thus toning down the difficulty involves the AI
      randomly not looking at a path. The probability of not going down a path
      is based on the difficulty setting.


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

