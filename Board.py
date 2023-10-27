from Ship import Ship
import random 
import time

board = []
compboard = []
new_board = []
new_comp_board = []
coordinates = []
hit_symbol = '|\U0001F4A5'
miss_symbol = '|\U0000274C'

#empty board with proper format created
def create_board(board):
    #print("Let's play Battleship!")
    empty_symbol = "  " 

    ascii_value = 65
    for x in range(6):
        board.append([f"|{empty_symbol}"] * 8)
        board[x][0] = chr(ascii_value)
        
        ascii_value+=1
    return board

#allows printing of a board in proper format
def print_board(board):
    print("   1  2  3  4  5  6")
    for row in board:
        print(("").join(row))
        print("---------------------")

#places ships depending on user input, appears on board, does proper checks on format of ships placed
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

#generates a random board for the computer using one of the three predetermined board
def create_comp_board():
    create_board(compboard)
    
    x = random.randint(0,2)
    if x == 0:
        compboard[1][2] = "|SB"
        compboard[1][3] = "|SB"
        compboard[1][4] = "|SB"
        compboard[2][5] = "|CS"
        compboard[3][5] = "|CS"
        compboard[2][1] = "|BS"
        compboard[3][1] = "|BS"
        compboard[4][1] = "|BS"
        compboard[5][1] = "|BS"
    elif x == 1:
        compboard[0][1] = "|SB"
        compboard[0][2] = "|SB"
        compboard[0][3] = "|SB"
        compboard[2][1] = "|CS"
        compboard[3][1] = "|CS"
        compboard[5][1] = "|BS"
        compboard[5][2] = "|BS"
        compboard[5][3] = "|BS"
        compboard[5][4] = "|BS"
    elif x == 2:
        compboard[0][6] = "|SB"
        compboard[1][6] = "|SB"
        compboard[2][6] = "|SB"
        compboard[5][5] = "|CS"
        compboard[5][4] = "|CS"
        compboard[1][1] = "|BS"
        compboard[2][1] = "|BS"
        compboard[3][1] = "|BS"
        compboard[4][1] = "|BS"
        
    return x

#allows game to start and user inputs which ship they would like to input, ship objects are created
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

#actual game sense is coded here, player one guesses, checks guess is correct format, tells if its a hit/miss and if a ship has sunk, then computer's turn, generate a random guess see if computer hits or miss and if a ship has sunk, repeat until all ships have been sunk for either computer or player  
def guess(rand_comp):
    player_hits = 0
    sub_hits = 0
    cruiser_hits = 0
    battle_hits = 0
    player_coord = [''.join(coordinates[i:i+2]) for i in range(0, len(coordinates), 2)]
    input_row = ""
    guess_col = 0
    comp_guess_row = 0
    comp_guess_col = 0
    comp_sub_hits = 0
    comp_cruiser_hits = 0
    comp_battle_hits = 0
    comp_hits = 0
    comp_guesses = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6']
    if rand_comp == 1:
        comp_coordinates = ['A1', 'A2', 'A3', 'C1', 'D1', 'F1', 'F2', 'F3', 'F4']
    elif rand_comp == 0:
        comp_coordinates = ['B2', 'B3', 'B4', 'C5', 'D5', 'C1', 'D1', 'E1', 'F1']
    elif rand_comp == 2:
        comp_coordinates = ['A6', 'B6', 'C6', 'B1', 'C1', 'D1', 'E1', 'F5', 'F4']
    
    
    print("\n"+"\n"+"\nPlayer 2: Time to guess Opponent's ships!")
    create_board(new_board)
    create_board(new_comp_board)
    print_board(new_comp_board)
    

    while comp_hits < len(player_coord) and player_hits < len(comp_coordinates):
        print("\nPLAYER TURN!")
        time.sleep(2)
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
                




        if new_comp_board[guess_row][guess_col] == miss_symbol or new_comp_board[guess_row][guess_col] == hit_symbol:
            print("You guessed that coordinate already. Try again.")
            continue
        if chr(guess_row+65) + str(guess_col) in comp_coordinates:
            print("!!!HIT! CONGRATULATIONS!!!")
            if compboard[guess_row][guess_col] == "|SB":
                sub_hits +=1
                if sub_hits == 3:
                    print("You sunk a submarine!")
            elif compboard[guess_row][guess_col] == "|CS":
                cruiser_hits +=1
                if cruiser_hits == 2:
                    print("You sunk a cruiser!")

            elif compboard[guess_row][guess_col] == "|BS":
                battle_hits +=1
                if battle_hits == 4:
                    print("You sunk a battleship!")
            new_comp_board[guess_row][guess_col] = hit_symbol
            time.sleep(2)
            print("\nOpponent's Board:")
            print_board(new_comp_board)
            player_hits +=1
        if compboard[guess_row][guess_col] == "|  ":
            time.sleep(1)
            print("You missed!")
            new_comp_board[guess_row][guess_col] = miss_symbol
            time.sleep(2)
            print("\nOpponent's Board:")
            print_board(new_comp_board)
            
        
        print("\nOPPONENT TURN!")
        time.sleep(2)
        print("Opponent thinking... please wait...")
        time.sleep(2)
        number = random.randint(0, len(comp_guesses)-1)
        comp_guess = comp_guesses.pop(number)
        
        if comp_guess == 'A1':
            comp_guess_row = 0
            comp_guess_col = 1
        if comp_guess == 'A2':
            comp_guess_row = 0
            comp_guess_col = 2
        if comp_guess == 'A3':
            comp_guess_row = 0
            comp_guess_col = 3
        if comp_guess == 'A4':
            comp_guess_row = 0
            comp_guess_col = 4
        if comp_guess == 'A5':
            comp_guess_row = 0
            comp_guess_col = 5
        if comp_guess == 'A6':
            comp_guess_row = 0
            comp_guess_col = 6
        if comp_guess == 'B1':
            comp_guess_row = 1
            comp_guess_col = 1
        if comp_guess == 'B2':
            comp_guess_row = 1
            comp_guess_col = 2
        if comp_guess == 'B3':
            comp_guess_row = 1
            comp_guess_col = 3
        if comp_guess == 'B4':
            comp_guess_row = 1
            comp_guess_col = 4
        if comp_guess == 'B5':
            comp_guess_row = 1
            comp_guess_col = 5
        if comp_guess == 'B6':
            comp_guess_row = 1
            comp_guess_col = 6
        if comp_guess == 'C1':
            comp_guess_row = 2
            comp_guess_col = 1
        if comp_guess == 'C2':
            comp_guess_row = 2
            comp_guess_col = 2
        if comp_guess == 'C3':
            comp_guess_row = 2
            comp_guess_col = 3
        if comp_guess == 'C4':
            comp_guess_row = 2
            comp_guess_col = 4
        if comp_guess == 'C5':
            comp_guess_row = 2
            comp_guess_col = 5
        if comp_guess == 'C6':
            comp_guess_row = 2
            comp_guess_col = 6
        if comp_guess == 'D1':
            comp_guess_row = 3
            comp_guess_col = 1
        if comp_guess == 'D2':
            comp_guess_row = 3
            comp_guess_col = 2
        if comp_guess == 'D3':
            comp_guess_row = 3
            comp_guess_col = 3
        if comp_guess == 'D4':
            comp_guess_row = 3
            comp_guess_col = 4
        if comp_guess == 'D5':
            comp_guess_row = 3
            comp_guess_col = 5
        if comp_guess == 'D6':
            comp_guess_row = 3
            comp_guess_col = 6
        if comp_guess == 'E1':
            comp_guess_row = 4
            comp_guess_col = 1
        if comp_guess == 'E2':
            comp_guess_row = 4
            comp_guess_col = 2
        if comp_guess == 'E3':
            comp_guess_row = 4
            comp_guess_col = 3
        if comp_guess == 'E4':
            comp_guess_row = 4
            comp_guess_col = 4
        if comp_guess == 'E5':
            comp_guess_row = 4
            comp_guess_col = 5
        if comp_guess == 'E6':
            comp_guess_row = 4
            comp_guess_col = 6
        if comp_guess == 'F1':
            comp_guess_row = 5
            comp_guess_col = 1
        if comp_guess == 'F2':
            comp_guess_row = 5
            comp_guess_col = 2
        if comp_guess == 'F3':
            comp_guess_row = 5
            comp_guess_col = 3
        if comp_guess == 'F4':
            comp_guess_row = 5
            comp_guess_col = 4
        if comp_guess == 'F5':
            comp_guess_row = 5
            comp_guess_col = 5
        if comp_guess == 'F6':
            comp_guess_row = 5
            comp_guess_col = 6
        
        
        if chr(comp_guess_row+65) + str(comp_guess_col) in player_coord:
            time.sleep(1)
            print("Oh no! You were hit!")
            if board[comp_guess_row][comp_guess_col] == "|SB":
                comp_sub_hits +=1
                if comp_sub_hits == 3:
                    time.sleep(1)
                    print("Your submarine was sunk!'")
            elif board[comp_guess_row][comp_guess_col] == "|CS":
                comp_cruiser_hits +=1
                if comp_cruiser_hits == 2:
                    time.sleep(1)
                    print("Your cruiser was sunk!")

            elif board[comp_guess_row][comp_guess_col] == "|BS":
                comp_battle_hits +=1
                if comp_battle_hits == 4:
                    time.sleep(1)
                    print("Your battleship was sunk!")
            new_board[comp_guess_row][comp_guess_col] = hit_symbol
            time.sleep(3)
            print("\nYour Board:")
            print_board(new_board)
            comp_hits +=1
        if board[comp_guess_row][comp_guess_col] == "|  ":
            time.sleep(1)
            print("Your opponent missed!")
            new_board[comp_guess_row][comp_guess_col] = miss_symbol
            time.sleep(2)
            print("\nYour Board:")
            print_board(new_board)
              
        
    time.sleep(2)
    if comp_hits >= len(player_coord):
        print("All your ships were sunk! You lost! Yikes... you just lost to a dumb computer... embarrassing ;-;")
    elif player_hits >= len(comp_coordinates):    
        print("You sunk all enemy battleships! You won! Whew close call... almost embarrassed yourself >_<")
    else:
        print("Tied! Still kinda embarrassing...")
        
#main function, everything added    
def main():
    rand_comp = create_comp_board()
    start_game()
    guess(rand_comp)
    
if __name__ == '__main__':
    main()












