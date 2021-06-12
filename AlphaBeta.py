from board import Mancala_Board

def Alpha_Beta_Algorithm(board, depth, alpha, beta , playAgain,Stealing_Flag):
     if depth == 0 or board.IsGameOver():
         return board.Score(),-1
     if playAgain:
         bestvalue = -9999999
         move = -1
         for i in range(7,13,1):
             if board.Mancala_board[i]==0: continue
             Test_board = Mancala_Board(board.Mancala_board[:])
             playAgain = Test_board.Stones_Move(i,Stealing_Flag)
             New_Value,_ =  Alpha_Beta_Algorithm(Test_board, depth-1, alpha, beta, playAgain,Stealing_Flag)
             if bestvalue < New_Value:
                 move=i
                 bestvalue =New_Value
             alpha = max(alpha, bestvalue)
             if alpha >= beta :
                 break
         return bestvalue, move
     else:
         bestvalue = 9999999
         move = -1
         for i in range(0, 6, 1):
             if board.Mancala_board[i] == 0: continue
             Test_board = Mancala_Board(board.Mancala_board[:])
             playAgain = Test_board.Stones_Move(i,Stealing_Flag)
             New_Value,_ = Alpha_Beta_Algorithm(Test_board, depth - 1, alpha, beta, not  playAgain,Stealing_Flag)
             if bestvalue > New_Value:
                 move = i
                 bestvalue = New_Value
             beta = min(beta, bestvalue)
             if alpha >= beta:
                 break
         return bestvalue, move

########################################################################################################################
