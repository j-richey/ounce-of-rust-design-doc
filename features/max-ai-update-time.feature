Feature: Maximum AI Update Time

  | As a Rust application developer,
  | I want the AI to block for less than one frame when picking a square,
  | so it does not block my rendering thread making my animations choppy.

  Frame times can vary greatly depending on platform and application. For example,
  an update time of one second might be just fine for a casual Tic Tac Toe game.
  However, a Tick Tac Toe mini-game in a modern FPS is expected to take just a
  fraction of the 1/144 second frame time. Therefore, providing the tools to allow
  the Rust application developer to see if this library meets their needs is
  sufficient to fulfill this requirement.

