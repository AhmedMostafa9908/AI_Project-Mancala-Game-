class Mancala_Board:

    def __init__(self, Mancala_board):
        if Mancala_board!=None:
            self.Mancala_board = Mancala_board[:]
        else:
          self.Mancala_board=[4,4,4,4,4,4,0,4,4,4,4,4,4,0]

    def IsGameOver(self):
        Player1_sum = 0
        Player2_sum = 0
        for i in range(0, 6, 1):
            Player1_sum += self.Mancala_board[i]

        for i in range(7, 13, 1):
            Player2_sum += self.Mancala_board[i]

        if Player1_sum == 0:
            for i in range(7, 13, 1):
                self.Mancala_board[13] += self.Mancala_board[i]
            for i in range(14):
                if (i != 13 and i != 6):
                    self.Mancala_board[i] = 0
            return True

        elif Player2_sum == 0:
            for i in range(0, 6, 1):
                self.Mancala_board[6] += self.Mancala_board[i]
            for i in range(14):
                if (i != 13 and i != 6):
                    self.Mancala_board[i] = 0
            return True

        return False

########################################################################################################################
    def Stones_Move(self, index, Stealing_Flag):
        StonesNumber=self.Mancala_board[index]
        self.Mancala_board[index] = 0
        Playagain=False
        if index>6:
            while(StonesNumber>0):
                index+=1
                index=index % 14
                if index==6: continue
                else:
                    self.Mancala_board[index%14]+=1
                StonesNumber-=1

            # Enable Stealing
            if Stealing_Flag:
                if index > 6 and self.Mancala_board[index] == 1 and index != 13 and self.Mancala_board[5 - (index - 7)] != 0:
                    self.Mancala_board[13] += 1 + self.Mancala_board[5 - (index - 7)]
                    self.Mancala_board[index] = 0
                    self.Mancala_board[5 - (index - 7)] = 0
            if index==13:
                Playagain = True
        else:
            while (StonesNumber > 0):
                index += 1
                index = index % 14
                if index == 13:
                    continue
                else:
                    self.Mancala_board[index%14] += 1
                StonesNumber -= 1
            # Enable Stealing
            if Stealing_Flag:
                if index < 6 and self.Mancala_board[index] == 1 and Mancala_Board != 6 and self.Mancala_board[-index + 12] != 0:
                    self.Mancala_board[6] += 1 + self.Mancala_board[-index + 12]
                    self.Mancala_board[index] = 0
                    self.Mancala_board[-index + 12] = 0
            if index == 6:
                Playagain = True
        return Playagain

########################################################################################################################

########################################################################################################################
    def Score(self):
        if self.IsGameOver():
            # Ai win
            if self.Mancala_board[13]>self.Mancala_board[6]:
                return 30
            # Human win
            elif self.Mancala_board[13]<self.Mancala_board[6]:
                return -30
            # Draw
            else :
                 return 0
        else:
            return self.Mancala_board[13] - self.Mancala_board[6]

########################################################################################################################