# cs32-final-project
CS32 Project with Chris Li and Andrew Chen 


For our project we hope to create a battleship game using a server and a client that constructs a game board using ASCII characters and simulates the game Battleship in the python shell. Each player is able to view their own game board during every turn to see their own ships and where they have missed or hit their opponent's ships. 


** FP Design ** 

**Game Board** 
- Board created using ASCII and lists
- Coordinates written out on sides (X-Axis - Numbers, Y-Axis - Letters)
- 10x10 board
- Empty board has O's as place holders for each coordinate
- Hit represented by explosion emoji
- Miss represented by X

**Game Mechanics** 
- Players place pieces 
- Data stored on p1 board and p2 board
 - Class ships
 - Each coordinate entered is stored in a list for specific ship
- Display empty and personal board for both players

While win = False
- P1 guess 
  - Mark guess on p1 empty board, mark on p2 personal board
  - Check if guess exists in one of the ship locations
    - If yes then counter +1 for that ship
  - If hit, p1 guess again (repeat step)
  - If not, p2 turn
  - If a ship has sunk display info
- P2 guess
  - Mark guess on p2 empty board, mark on p1 personal board
  - If hit, p2 guess again (repeat step)
  - If not, p1 turn
- If all p1/p2 pieces are hit (counters added up equal total) win = True (exit loop)
  - Display win/lose 

**Network** 
- Divided into dumb client and smart server
- Connection from two player from different computers
