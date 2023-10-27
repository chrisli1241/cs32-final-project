from ShipTest import Ship

board = []
new_board = []
coordinates = []
hit_symbol = '|\U0001F4A5'
miss_symbol = '|\U0000274C'

def create_board(board):
    #print("Let's play Battleship!")
    empty_symbol = "  " 

    ascii_value = 65
    for x in range(6):
        board.append([f"|{empty_symbol}"] * 8)
        board[x][0] = chr(ascii_value)
        
        ascii_value+=1
    return board
    
def print_board(board):
    print("   1  2  3  4  5  6")
    for row in board:
        print(("").join(row))
        print("---------------------")


            
    #print("Input the starting coordinate")
    #print("Input the end coordinate (must be same row or column)")
    #return board 




def create_ship(self):
    self = Ship(self.name, self.size, None, None, None, None)
    
    while True:
        
        while True:
            self.place_ship()
            
            letter_row = ord(self.row)-65
            letter_row2 = ord(self.row2)-65
    
            #print(self.name,self.size,self.row,self.col,self.row2,self.col2)
            if(self.row == self.row2):
                if int(self.col) > int(self.col2): 
                    for horiz in range(int(self.col),int(self.col2)-1,-1):
                        exit_condition = True
                        if board[letter_row][horiz] == "|  ":
                            board[letter_row][horiz] = self.name
                            coordinates.extend([self.row,str(horiz)])
                        else:
                            print("A ship has already been placed here. Please try again.")
                            
                            break
                        
                for horiz in range(int(self.col),int(self.col2)+1,1):
                    exit_condition = True
                    if board[letter_row][horiz] == "|  ":
                        board[letter_row][horiz] = self.name
                        coordinates.extend([self.row,str(horiz)])
                    else:
                        print("A ship has already been placed here. Please try again.")
                        
                        break

                    
        
            if(self.col == self.col2):
                if letter_row > letter_row2: 
                    for vert in range(letter_row,letter_row2-1,-1):
                        exit_condition = True
                        if board[vert][int(self.col)] == "|  ":
                            board[vert][int(self.col)] = self.name
                            coordinates.extend([chr(vert+65),str(self.col)])
                        else:
                            print("A ship has already been placed here. Please try again.")
                            
                            break
                for vert in range(letter_row,letter_row2+1,1):
                    exit_condition = True
                    if board[vert][int(self.col)] == "|  ":
                        board[vert][int(self.col)] = self.name
                        coordinates.extend([chr(vert+65),str(self.col)])
                    else:
                        print("A ship has already been placed here. Please try again.")
                        
                        break
            break
        if exit_condition == True:
            break
        else:
            continue   

    #return coordinates

        
            #board[letter_row2][int(submarine.col2)] = submarine.name

        
   
    
    
    
def start_game():
    
    print("Let's play battleship!"+"\nPlayer 1: Time to place your ships!")
    create_board(board)
    print_board(board)
    ships = []
    
    while len(ships) < 3:
        ship_input = input("\nInput the ship type (submarine, cruiser, battleship):")
        while True:
    
            if ship_input.lower() == "submarine":
                if ship_input in ships:
                    print("This ship has already been placed. Try again")
                    break
                else:
                    ships.append("submarine")
                    
                    submarine = Ship("|SB", 3, None, None, None, None)
                    print("You selected submarine (3 spaces)!")
                    create_ship(submarine)
                    print_board(board)
                print(ships)
    
            elif ship_input.lower() == "cruiser":
                if ship_input in ships:
                    print("This ship has already been placed. Try again")
                    break
                else:
                    ships.append("cruiser")
                   
                    cruiser = Ship("|CS", 2, None, None, None, None)
                    print("You selected cruiser (2 spaces)!")
                    create_ship(cruiser)
                    print_board(board)
                print(ships)

            
            elif ship_input.lower() == "battleship":
                if ship_input in ships:
                    print("This ship has already been placed. Try again")
                    break
                else:
                    ships.append("battleship") 
                    
                    battleship = Ship("|BS", 4, None, None, None, None)
                    print("You selected battleship (4 spaces)!")
                    create_ship(battleship)
                    print_board(board)
                    
                print(ships)
            else:
                print("Invalid input.")
                break
        
            break

    
    return coordinates
            
def guess():
    total_hits = 0
    sub_hits = 0
    cruiser_hits = 0
    battle_hits = 0
    joined_coord = [''.join(coordinates[i:i+2]) for i in range(0, len(coordinates), 2)]
    input_row = ""
    guess_col = 0

    
    print(joined_coord)
    print("\n"+"\n"+"\nPlayer 2: Time to guess Player 1's ships!")
    create_board(new_board)
    print_board(new_board)
    

    while total_hits < len(joined_coord):
        while True:
            input_row = input("Please input the row of your guess:")
            if len(input_row) > 1:
                print("Invalid Input: Please only input one character")
            else:
                if ord(input_row) not in range(65,71,1):
                    print("Invalid input: Please enter a letter from A-F")
                elif ord(input_row) in range(65,71,1):
                    break

        while True:
            try:
                guess_col = int(input("Please input the column of your guess:"))
                if guess_col not in range(7):
                    print("Invalid input: Please enter a number from 1-6")
                elif guess_col in range(7):
                    break
                
            except ValueError:
                print("invalid input: Please enter a number from 1-6")

        guess_row = ord(input_row)-65
                




        if new_board[guess_row][guess_col] == miss_symbol or new_board[guess_row][guess_col] == hit_symbol:
            print("You guessed that coordinate already. Try again.")
            continue
        if chr(guess_row+65) + str(guess_col) in joined_coord:
            print("Hit! Congratulations!")
            if board[guess_row][guess_col] == "|SB":
                sub_hits +=1
                if sub_hits == 3:
                    print("You sunk a submarine!")
            elif board[guess_row][guess_col] == "|CS":
                cruiser_hits +=1
                if cruiser_hits == 2:
                    print("You sunk a cruiser!")

            elif board[guess_row][guess_col] == "|BS":
                battle_hits +=1
                if battle_hits == 4:
                    print("You sunk a battleship!")
            new_board[guess_row][guess_col] = hit_symbol
            print_board(new_board)
            total_hits +=1
        if board[guess_row][guess_col] == "|  ":
            print("Miss! Try again.")
            new_board[guess_row][guess_col] = miss_symbol
            print_board(new_board)
        

    print("You sunk all the battleships!")
        
    
    
def main():
    start_game()
    guess()
    
    

if __name__ == '__main__':
    main()












