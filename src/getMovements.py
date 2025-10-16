
from warnings import warn


class GetMovements:
    def __init__(self,board) -> None:
        self.board= board
        self.selected = False
        self.x =None;
        self.y =None;
        self.selected_piece = ""
    def isInGrid(self,x,y) ->bool:
        return (x >= 0 and x <= 640)and(y >= 0 and y <= 640)
    def selectPiece(self,x,y):
           if self.isInGrid(x,y) and self.selected == False:
               self.x = int(x/80)
               self.y = int(y/80)
               self.selected_piece= self.board.board[self.y][self.x]
               if self.selected_piece == "" or self.selected_piece == None:
                   return
               self.selected = True
           else:
               if self.isInGrid(x,y):
                  newPosX = int(x/80)
                  newPosY = int(y/80)
                  if self.isValidPositon(newPosX,newPosY):
                      self.board.updatePos(self.y,self.x,newPosY,newPosX) 
                  self.selected = False
                  self.x = None
                  self.y = None

    def clearPath(self,oldx,oldy,newx,newy):
        dx = newx - oldx
        dy = newy - oldy

        stepx = 0 if dx == 0 else int(dx/abs(dx))
        stepy = 0 if dy == 0 else int(dy/abs(dy))

        x,y = oldx + stepx,oldy + stepy
        while(x,y) != (newx,newy):
            if(self.board.board[y][x] is not None):
                return False
            x += stepx
            y += stepy
        return True


    def isValidPositon(self,x,y):
        piece = self.selected_piece

        oldx,oldy = self.x,self.y
        dx = x -oldx
        dy = y -oldy

        target = self.board.board[y][x]

        if target is not None and target.startswith('w_'):
            return False

        if piece == "w_pawn":
            if dx == 0 and dy == -1 and self.board.board[y][x] is None:
                return True

            if dx == 0 and dy == -2 and oldy == 6 and \
                    self.board.board[y][x] is None and \
                    self.board.board[oldy-1][oldx] is None:
                return True
            return False 

        if piece == "w_knight":
            if (abs(dx),abs(dy)) in [(1,2),(2,1)]:
                return True
            return False
        
        if piece == "w_rook":
            if dx == 0 or dy == 0:
                if self.clearPath(self.x,self.y,x,y):
                    return True;
            return False
            
        if piece == "w_king":
            if abs(dx) <= 1 and abs(dy) <=1:
                if self.clearPath(oldx,oldy,x,y):
                    return True
            return False
            
        if piece == "w_bishop":
            if abs(dx) == abs(dy):
                if self.clearPath(oldx,oldy,x,y):
                    return True
            return False

        if piece == "w_queen":
            if (dx == 0 or dy == 0) or (abs(dx) == abs(dy)):
                if self.clearPath(oldx,oldx,x,y):
                    return True
            return False


