### chap05/guess-client.py
from ShipTest import Ship
from socket32 import create_new_socket
from BoardTest import create_board, print_board, create_ship, start_game


HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server
empty_board = []

def guess(coords,empty_board): #input row and col guesses and checks if guess is hit or miss 
    hit_symbol = '|\U0001F4A5'
    miss_symbol = '|\U0000274C'
    input_row = ""
    guess_col = 0
    result = ""
    while True:
        while True: #check for invalid inputs 
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

        if empty_board[guess_row][int(guess_col)] == miss_symbol or empty_board[guess_row][int(guess_col)] == hit_symbol: #check for already-chosen guess
            print("\nInvalid input: Coordinate already chosen")
            continue
        if input_row + str(guess_col) in coords:
            print("\nHit!")
            empty_board[guess_row][int(guess_col)] = hit_symbol
            print_board(empty_board)
            result = "Hit"
        elif input_row + str(guess_col) not in coords:
            print("\nMiss!")
            empty_board[guess_row][int(guess_col)] = miss_symbol
            print_board(empty_board)
        

        break

    return input_row, str(guess_col), result #returns the guess as well as the result of the guess if it is a hit 




def main():
    hit_symbol = '|\U0001F4A5'
    miss_symbol = '|\U0000274C'
    print('## Welcome to BATTLESHIP! ##')
    total_hits = 0
    your_hit_counter = 0
    with create_new_socket() as s:
        s.connect(HOST, PORT)
        
        
        client_coords = start_game() #client places ships 
        s.sendall(str(client_coords)) #client sends the coordinates of their ships to the server 
        coordinates = s.recv()
        list_coord = coordinates.strip(']['"'").split("', '") #convert string coordinates sent from server into a list 

        
        joined_server_coords = [''.join(list_coord[i:i+2]) for i in range(0, len(list_coord), 2)]
        joined_client_coords = [''.join(client_coords[i:i+2]) for i in range(0, len(client_coords), 2)] #join coordinates to follow 2 character structure ie. (A1, A2, etc)
        
        
    
        
        #print(joined_server_coords) <--- if you want server's coords
        print("\n"+"\n"+"\nTime to guess Player 2's ships!")
        create_board(empty_board)
        print_board(empty_board)

        while True: #client guesses and receives server's guess 
            guess_row, guess_column, client_result = guess(joined_server_coords, empty_board)
            s.sendall(str(guess_row))
            s.recv()
            s.sendall(str(guess_column))
            print("\nWaiting for server to respond....")
            
    
            server_row = s.recv()
            server_col = s.recv()
    
            if server_row + server_col in joined_client_coords:
                print("\nThey hit your ship!")
                total_hits +=1
            elif server_row + server_col not in joined_client_coords:
                print("Miss!")
                
            if total_hits == len(joined_client_coords):
                print("\nThey sunk your battleships! You lose!")
                break
            if client_result == "Hit":
                your_hit_counter +=1
                if your_hit_counter == len(joined_server_coords):
                    print("\nYou sunk all of their battleships! You win!")
                    break
        

        
        
        
            
            

if __name__ == '__main__':
    main()
