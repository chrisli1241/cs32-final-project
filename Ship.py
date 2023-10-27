import math
#class ship created
class Ship: 
    def __init__(self, name, size, row, col, row2, col2):
        self.name = name 
        self.size = size 
        self.row = row 
        self.col = col
        self.row2 = row2
        self.col2 = col2



    #allows individual to enter coordinates in which they would like to place ship while having all necessary checks in place to ensure final input is in correct format
    def place_ship(self):

        while True:
            while True:
                self.row = input("Which row would you like to place your starting point? (A-F)")
                if len(self.row) > 1:
                    print("Invalid Input: Please only input one character")
                else:
                    if ord(self.row) not in range(65,71,1):
                        print("Invalid input: Please enter a letter from A-F")
                    elif ord(self.row) in range(65,71,1):
                        break
            
            while True:
                    try:
                        self.col = int(input("Which col would you like to place your starting point? (1-6)"))
                        if int(self.col) not in range(7):
                            print("Invalid Input: Please enter a number from 1 and 6")
                           
                        elif int(self.col) in range(7):
                            break
                    except ValueError:
                        print("Invalid Input: Not A Real Column")
                    
                                
                #ending point checks
            while True:
                self.row2 = input("Which row would you like to place your ending point? (A-F)")
                if len(self.row2) > 1:
                    print("Invalid Input: Please only input one character")
                else:
                    if ord(self.row2) not in range(65,71,1):
                        print("Invalid input: Please enter a letter from A-F")
                    elif ord(self.row2) in range(65,71,1):
                        break
            
                                    #checks ending row is two up or down  
            while True:
                    try:
                        self.col2 = int(input("Which col would you like to place your ending point? (1-6)"))
                        if int(self.col2) not in range(7):
                            print("Invalid Input: Please enter a number from 1 and 6")
                           
                        elif int(self.col2) in range(7):
                            break
                    except ValueError:
                        print("Invalid Input: Not A Real Column")

            dist1 = (math.dist([ord(self.row)], [ord(self.row2)]) + 1)
            dist2 = (math.dist([int(self.col)],[int(self.col2)]) + 1)
            
            if (self.row != self.row2) and (self.col != self.col2):
                print("Invalid input: Ships not aligned. Please make sure that either the row or column is the same value")
                continue
                    
                    
                    
                #checks that ship is correct size
            if dist1 != float(self.size) and dist2 != float(self.size):
                print("Input Invalid: Incorrect size of ship please get better at math")
                    
                continue
                    
            else:
                ship_loc = Ship(self.name,self.size,self.row,self.col,self.row2,self.col2)
                
                return ship_loc
                break
            
            
        
                #if ship input = sumbarine then x = submarine
    
















    
