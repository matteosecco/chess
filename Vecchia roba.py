class Pawn(Piece):
    def _move(self, x, y):
        if self.x != x:
            return False
        
        # ci sono tre casi (in verità 4 con en-passant)
        # 1° caso: doppio passo
        # 2° caso: take
        # 3° caso: normale
               
        # determines the color coefficient
        if self.w:
            color = 1
        else:
            color = -1
        
        # primo caso: mossa normale
        if self.x == x and y - self.y == color:
            self.y = y
            return True
        # secondo caso: mossa da due
        elif self.x == x and y - self.y == color * 2 and color * self.y in (2, -7)
            self.y = y
            return True
        # terzo caso: take
        elif abs(x - self.x) == 1 and y - self.y == color:
            if parent.get(x, y) != False:
                if parent.get(x, y).w != self.w:
                    # take
                    self.x = x
                    self.y = y
                    return True
        
        return False
        # bianco
        if self.w:
            if y - self.y == 1: # mossa normale
                self.y = y
                return True
            elif y - self.y == 2 and self.y == 2: # mossa iniziale
                self.y = y
                return True
            else:
                return False
        # nero
        else:
            if self.y - y == 1:
                self.y = y
                return True
            elif self.y - y == 2 and self.y == 7: # mossa doppia
                self.y = y
                return True
            else:
                return False
        
    def take(self, x, y):
        # è l'unica che riscrive la funzione take
        # check for validity
        if not (0 < x < 8 and 0 < y < 8):
            return False
        
        # check se c'è qualcuno
        
        # bianco        
        if self.w:
            if self.y - y == 1 and abs(self.x - x) == 1:
                self.y = y
                self. x = x
                return True
        # nero
        else:
            if y - self.y == 1 and abs(self.x - x) == 1:
                self.y = y
                self.x = x
                return True
        return False
    