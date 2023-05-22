def show():
    for row in game_board:
        for cell in row:
            print(cell, end="")
        print()


def chek_game(win):
        
        for i in range(3):
            if game_board[i][0] == game_board[i][1] == game_board[i][2] == "x":
                win = "x"
                return win
            
            elif game_board[i][0] == game_board[i][1] == game_board[i][2] == "o":
                win = "o" 
                return win 
                      
            if game_board[0][i] == game_board[1][i] == game_board[2][i] == "x":
                win = "x"
                return win
            elif game_board[0][i] == game_board[1][i] == game_board[2][i] == "o":
                win = "o" 
                return win 

            if game_board[0][0] == game_board[1][1] == game_board[2][2] == "x":
                win = "x"
                return win
            elif game_board[0][0] == game_board[1][1] == game_board[2][2] == "o":
                win = "o" 
                return win 
            
            if game_board[0][2] == game_board[1][1] == game_board[2][0] == "x":
                win = "x"
                return win
            
            elif game_board[0][2] == game_board[1][1] == game_board[2][0] == "o":
                win = "o" 
                return win 
        return 1


            






                

    


game_board = [["-","-","-"],
              ["-","-","-"],
              ["-","-","-"]]

show()

while True:
    print("player1")
    while True:
        row = int(input("enter row:"))
        col = int(input("enter col:"))
        if 0<= row <=2 and  0<= col <=2:
            if (game_board[row][col]=="-"):
                game_board[row][col]="x"
                break
            else:
                print("select another cell!!!")
        else:
            print("select in 0 , 2")
    show()
    winner = chek_game(0)
    if winner == "x":
        print("player1 win !!")
        break
    

    print("player2")
    while True:
        row = int(input("enter row:"))
        col = int(input("enter col:"))
        if 0<= row <=2 and  0<= col <=2:
            if (game_board[row][col]=="-"):
                game_board[row][col]="o"
                break
            else:
                print("select another cell!!!")
        else:
            print("select in 0 , 2")
    show() 
    winner = chek_game(0)
    if winner == "o":
        print("player2 win !!")
        break
    
