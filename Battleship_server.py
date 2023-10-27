### chap05/guess-server.py
from ShipTest import Ship
from socket32 import create_new_socket
from BoardTest import create_board, print_board, create_ship, start_game
import Battleship_client as rlib 


HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    empty_board = []
    hit_symbol = '|\U0001F4A5'
    miss_symbol = '|\U0000274C'
    total_hits = 0
    your_hits = 0

    with create_new_socket() as s:
        s.bind(HOST, PORT)
        s.listen()
        print("BATTLESHIP server started. Listening on", (HOST, PORT))

        conn, addr = s.accept()
        print('Connected by', addr)


        
        with conn:
            client_coords = conn.recv()
            print(client_coords)
            list_coord = client_coords.strip(']['"'").split("', '") #convert string coordinates sent from client into a list 
            server_coords = start_game() #server places ships
            conn.sendall(str(server_coords)) #server sends of the coordinates of their ships to the client 
            

            
            joined_client_coords = [''.join(list_coord[i:i+2]) for i in range(0, len(list_coord), 2)]
            joined_server_coords = [''.join(server_coords[i:i+2]) for i in range(0, len(server_coords), 2)] #join coordinates to follow 2 character structure ie. (A1, A2, etc)
        
            
            #print(joined_client_coords) <-- if you want client's coords 
            print("\n"+"\n"+"\nTime to guess Player 1's ships!")
            create_board(empty_board)
            print_board(empty_board)

            while True: #server receives client's guess and then makes their own guess 
                print("\nWaiting for client to respond....")
                client_row = conn.recv() 
                x = " " #<--- placeholder to recv() but don't know why it works 
                conn.sendall(x)
                client_col = conn.recv()
    
                if client_row + client_col in joined_server_coords:
                    print("\nThey hit your ship!")
                    total_hits +=1
                elif client_row + client_col not in joined_server_coords:
                    print("\nMiss!")
    
                guess_row, guess_column, server_result = rlib.guess(joined_client_coords, empty_board)
                conn.sendall(str(guess_row))
                conn.sendall(str(guess_column))
                
                if total_hits == len(joined_server_coords):
                    print("\nThey sunk your battleships! You lose!")
                    break
                if server_result == "Hit":
                    your_hits +=1
                    if your_hits == len(joined_client_coords):
                        print("\nYou sunk all of their battleships! You win!")
                        break

                
            
        
            print('Disconnected')

if __name__ == '__main__':
    main()
