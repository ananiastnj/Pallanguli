class Pallanguli:
    total_muthu = 70
    #board = [5 for i in range(14)]
    #print(board)
    player1_side_board = 35
    player2_side_board = 35
    player1_start = 0
    player2_start = 0
    #game_start(player1_side_board,player2_side_board,player1_start,player2_start,player1,player2,board)
    player1_kuli = 0
    player2_kuli = 0
    total_kuli = 0
    def index_check(self, start_value):
        if (start_value == 13):
            start_value = -1
        return start_value
    
    def board_generation(self, player1, player2, board):
        player1_kuli = player1 // 5
        #board = []
        if(player1_kuli < 7 ):
            board = [5 for i in range(player1_kuli)]
            player1 -= (player1_kuli*5)
        elif(player1_kuli >= 7):
            board = [5 for i in range(7)]
            player1 -= (7 * 5)
        player2_kuli = player2 // 5
        if (player2_kuli < 7):
            board.extend([5 for i in range(player2_kuli)])
            player2 -= (player2_kuli * 5)
        elif (player2_kuli >= 7):
            board.extend([5 for i in range(7)])
            player2 -= (7 * 5)
        return (board,player1,player2)

p = Pallanguli()
player1 = 35
player2 = 35
board = []  
board_gen = list(p.board_generation(player1, player2, board))
print("***** Board *****\n",board_gen[0])
print("Player1 : ",board_gen[1])
print("Player2 : ",board_gen[2])


'''
print(board)
print(player1)
print(player2)
print(player1_kuli)
print(player2_kuli)
print(total_kuli)
'''
#round_calculation(player1_side_board,player2_side_board,player1,player2,board)

