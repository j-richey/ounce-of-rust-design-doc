# Change Log
Significant changes to the Ounce of Rust project manual are described here.


## Rev B - 2019-11-27

### Requirements

* **Changed:** Know Squares that Contributed to Player’s Victory requirement to 
  clarify that in the event the player won by having more than one row, column, 
  or diagonal all the squares are provided.

#### Design

* **Added:** Size struct to represent board sizes.
* **Removed:**  Square struct as this data is redundant.
* **Changed:** Game struct so it provides access to free squares instead of the
  Board struct. 
* **Changed:** Victory sets are represented by the Rust HashSet instead of having
  a custom type.
* **Changed:** AIMove struct is renamed to AIOpponent. The AIOpponent struct
  is not intended to be recreated every move like the old AIMove was.
* **Changed:** Public APIs now prefer to return an Error Result or None Option 
  type instead of panicking.  
* **Changed:** The continuous integration system enforces documentation for 
  public APIs instead of making the Rust compiler do this check.


## Rev A - 2019-10-27
Initial release
