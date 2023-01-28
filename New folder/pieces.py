
class Piece:
    def __init__(self, parent, x, y, w):
        self.parent = parent
        self.x = int(x)  # 12345678 che sta a abcdefgh
        self.y = int(y)  # 12345678
        self.w = int(w) # black or white (-1 or +1)
        
    def __str__(self):
        return "%s(%s, %s, %s)" % (str(self.__class__).split(".")[-1][:-2], str(self.x), str(self.y), str(self.w))
    
    def move(self, x, y):
        # check the validity of the arguments
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
    def __init__(self, parent, x, y, w):
        super(Pawn, self).__init__(parent, x, y, w)
        self.id = "pawn" + str(self.w)

    def _movelist(self):
        pos_list = []

        # primo caso: normale
        if self.parent.get(self.x, self.y + self.w) is False: 
            pos_list.append((self.x, self.y + self.w))
        
        # second caso: mossa da due
        if self.parent.get(self.x, self.y + 2*self.w) is False and self.parent.get(self.x, self.y + self.w) is False:
            if self.y == 2 or self.y == 7:
                pos_list.append((self.x, self.y + 2*self.w))

        # terzo caso: take
        destra = self.parent.get(self.x + 1, self.y + self.w)
        if destra != False and destra.w != self.w:
            pos_list.append((self.x + 1, self.y + self.w))
        sinistra = self.parent.get(self.x - 1, self.y + self.w)
        if sinistra != False and sinistra.w != self.w:
            pos_list.append((self.x - 1, self.y + self.w))
            
        # quarto caso: en passant

        return pos_list
        
    def _move(self, x, y):
        # check se la mossa è in lista
        if (x, y) in self._movelist():
            self.parent.kill(self.parent.get(x, y))
            self.y = y
            self.x = x
            return True
        
        return False
    
class Knight(Piece):
    def __init__(self, parent, x, y, w):
        super(Knight, self).__init__(parent, x, y, w)
        self.id = "knight" + str(self.w)
    
    def _movelist():
        pass
    
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

class Bishop(Piece):
    def __init__(self, parent, x, y, w):
        super(Bishop, self).__init__(parent, x, y, w)
        self.id = "bishop" + str(self.w)
    
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

class Queen(Piece):
    def __init__(self, parent, x, y, w):
        super(Queen, self).__init__(parent, x, y, w)
        self.id = "queen" + str(self.w)
    
    def _move(self, x, y):
        if (self.x == x or self.y == y) or abs(self.x - x) == abs(self.y - y):
            self.x = x
            self.y = y
            return True
        return False

class King(Piece):
    def __init__(self, parent, x, y, w):
        super(King, self).__init__(parent, x, y, w)
        self.id = "king" + str(self.w)
    
    def _move(self, x, y):        
        if abs(self.x - x) < 2 and abs(self.y - y) < 2:
            # check se viene messo sotto scacco
            self.y = y
            self.x = x
            return True
        return False
    
class Rook(Piece):
    def __init__(self, parent, x, y, w):
        super(Rook, self).__init__(parent, x, y, w)
        self.id = "rook" + str(self.w)
    
    def _move(self, x, y):        
        if self.x == x or self.y == y:
            # check se la strada è libera
            
            
            self.y = y
            self.x = x
            return True
        
        return False
