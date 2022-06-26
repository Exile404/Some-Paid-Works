class ControlGame:
    c=0
    def __init__(self,turns):
        # This initializes the game with an empty board, the current
        # player set to 'Red' and the number of turns
        # specified by the user (defaults to 64).  turnsToPlay must
        # be an even number in the range [2..64].
        self.turnstpPlay=8
        self.lst=[["." for i in range(8)] for j in range(8)]
        self.red=0
        self.blue=0

    def __str__(self):
        # Permit displaying the header "Current board is:" following by the 
        # board.
        s=' '
        for i in range(self.turnstpPlay):
            if i==0:
                for j in range(self.turnstpPlay):
                    s+=str(j)+" "
                s+='\n'

            for j in range(self.turnstpPlay):
                if j==0:
                    s+=(str(i)+" "+self.lst[i][j]+" ")
                else:
                    s += (self.lst[i][j] + " ")
            s+='\n'
        return s

    def swapCurrentPlayer(self):
        # If the current player is 'Red', set it to 'Blue', and
        # vice versa.
        if ControlGame.c % 2 == 0:
            ControlGame.c += 1
            return "Red"
        else:
            ControlGame.c += 1
            return "Blue"

    def getCurrentPlayer(self):
        # Return the current player, 'Red' or 'Blue'
        if ControlGame.c % 2 == 0:
            return "Red"
        else:
            return "Blue"

    def takeTurn(self, row, col):
        # This attempts to add the current player's token to cell
        # (row, col).  Check whether the cell is legal and is not
        # occupied.  If the checks pass add the current player's
        # token to that cell.  Finally, return a Boolean value 
        # indicating whether or not the turn occurred.
        if row>7 or col>7:
            print("Invalid turn. Location is out of bounds.")
            return False
        if self.lst[row][col]!='.':
            print("Invalid turn. Cannot place piece on occupied cell.")
            return False


        if self.getCurrentPlayer()=="Red":
            check=False
            for i in range(self.turnstpPlay):
                if self.lst[row][i]=="B" or self.lst[i][col]=="B":
                    self.red+=1
                    self.blue-=1
                    check=True
                    break
            if check==False:
                heck = False
                for i in range(self.turnstpPlay):
                    if self.lst[row][i] == "R" or self.lst[i][col] == "R":
                        self.red += 1
                        heck = True
                        break
                if heck==False:
                    self.red+=2
        else:
            check = False
            for i in range(self.turnstpPlay):
                if self.lst[row][i] == "R" or self.lst[i][col] == "R":
                    self.red -= 1
                    self.blue += 1
                    check = True
                    break
            if check == False:
                heck = False
                for i in range(self.turnstpPlay):
                    if self.lst[row][i] == "B" or self.lst[i][col] == "B":
                        self.blue += 1
                        heck = True
                        break
                if heck == False:
                    self.blue += 2
        if self.getCurrentPlayer()=="Red":
            self.lst[row][col]="R"
        else:
            self.lst[row][col]="B"
        self.swapCurrentPlayer()
        return True


    def getScore(self):
        # Calculate the sum of rows, columns, and cells controlled by
        # Red and Blue.  Return this as a pair (red, blue).  This is
        # the most complicated method, so it's probably a good idea 
        # to write subsidiary functions for this.
        return self.red,self.blue