###############################
Interactions with Other Systems
###############################

The Tic Tac Toe library is intended to be used in other user facing applications.
This includes, but is not limited to, stand alone graphical applications, command
line applications, or even as a mini-game in a larger video game. The diagram in
:numref:`uml-interaction-diagram` shows how the library is used by other systems.

..  _uml-interaction-diagram:
..  uml::
    :caption: Diagram showing how the library is used by other applications.

    [TTT GUI] --> [open_ttt_lib]
    [TTT CLI] --> [open_ttt_lib]
    [TTT Mini Game] --> [open_ttt_lib]

The other applications link directly to ``open_ttt_lib``. The library does not
provide any ways of remote access, e.g. via a network interface and it does not
save any state the computer's persistent storage.
