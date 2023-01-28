class Piece:
    def __init__(self, parent, x, y, w=True):
        """
        Each piece has only its coordinate and the reference to its parent (Board).
        """
        self.parent = parent
        self.x = int(x)  # 12345678 che sta a abcdefgh
        self.y = int(y)  # 12345678
        self.w = bool(w) # black or white
        
    def __str__(self):
        return "%s(%s, %s, %s)" % (str(self.__class__).split(".")[-1][:-2], str(self.x), str(self.y), str(self.w))
    
    def move(self, x, y):
        """
        Function called to move the piece. The function is the same for all pieces for the part in which it checks
        the validity of the arguments, the it calls a piece-specific function _move()
        """
        if 0 < x < 9 and 0 < y < 9 and not (self.x == x and self.y == y):
            return self._move(x, y)
        print("Errore: dati incorretti")
        return False
    
    def _move(self, x, y):
        """ overwritten by the subclasses """
        pass
    
    def take(self, x, y):
        # rimuove il morto
        self.move(x, y)

class Pawn(Piece):
    def _move(self, x, y):
        # gets whos' there
        piece = self.parent.get(x, y)
        
        # determines the color coefficient
        if self.w:
            color = 1
        else:
            color = -1

        
        # primo caso: mossa normale
        if self.x == x and y - self.y == color:
            if piece is False:    
                self.y = y
                return True
        
        # secondo caso: mossa da due
        elif self.x == x and y - self.y == color * 2 and color * self.y in (2, -7):
            if piece is False and self.parent.get(x, y - 1) is False:    
                self.y = y
                return True
            
        # terzo caso: take
        elif abs(x - self.x) == 1 and y - self.y == color:
            if piece != False:
                if piece.w != self.w:
                    print("Taken")
                    self.parent.kill(piece)
                    self.x = x
                    self.y = y
                    return True
        # quarto caso: en-passant
        
        return False


class Bishop(Piece):
    def _move(self, x, y):
        # check se la mossa è valida
        if abs(self.x - x) == abs(self.y - y):
            # check se la strada è libera    

            # primo quadrante +x +y
            if (self.x - x) < 0 and (self.y - y) < 0:
                for i in range(1, x - self.x):
                    if self.parent.get(self.x+i, self.y+i) != False:
                        print("Errore: trovato qualcuno in mezzo")
                        return False

            # secondo +x -y
            elif (self.x - x) < 0 and (self.y - y) > 0:
                print("seconfo")

            # terzo -x -y
            elif (self.x - x) > 0 and (self.y - y) > 0:
                for i in range(1, self.x - x):
                    if self.parent.get(self.x-i, self.y-i) != False:
                        print("Errore: trovato qualcuno in mezzo")
                        return False

            # quarto -x +y
            else:
                print("quanrto")
            
            # viene eseguito quando la strada è libera
            self.x = x
            self.y = y
            return True
        return False

class Knight(Piece):
    def _move(self, x, y):
        # gets whos' there
        piece = self.parent.get(x, y)
        
        if abs(self.x - x) + abs(self.y - y) == 3 and self.x != x and self.y != y:
            if piece != False:
                self.parent.kill(piece)
                print("Taken")
            self.x = x
            self.y = y
            return True
        return False

class Rook(Piece):
    def _move(self, x, y):        
        if self.x == x or self.y == y:
            # check se la strada è libera
            
            
            self.y = y
            self.x = x
            return True
        
        return False

class Queen(Piece):
    def _move(self, x, y):
        if (self.x == x or self.y == y) or abs(self.x - x) == abs(self.y - y):
            self.x = x
            self.y = y
            return True
        return False

class King(Piece):
    def _move(self, x, y):        
        if abs(self.x - x) < 2 and abs(self.y - y) < 2:
            # check se viene messo sotto scacco
            self.y = y
            self.x = x
            return True
        return False