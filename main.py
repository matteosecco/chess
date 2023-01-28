# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:29:21 2021

@author: Matte
"""

from pieces import *

class Board:
    def __init__(self):
        """ Posiziona tutti i pezzi nella scacchiera """
        a = [Pawn(self, x + 1, 2) for x in range(8)]
        b = [Pawn(self, x + 1, 7, w=False) for x in range(8)]
        c = a + b
        c.append(Rook(self, 1, 1))
        c.append(Rook(self, 8, 1))
        c.append(Rook(self, 1, 8, w=False))
        c.append(Rook(self, 8, 8, w=False))
        c.append(Bishop(self, 3, 1))
        c.append(Bishop(self, 6, 1))
        c.append(Bishop(self, 3, 8, w=False))
        c.append(Bishop(self, 6, 8, w=False))
        c.append(Bishop(self, 6, 4))
        c.append(Knight(self, 7, 1))
        c.append(Knight(self, 2, 1))
        c.append(Knight(self, 7, 8, w=False))
        c.append(Knight(self, 2, 8, w=False))
        c.append(Queen(self, 4, 1))
        c.append(Queen(self, 4, 8, w=False))
        c.append(King(self, 5, 1))
        c.append(King(self, 5, 8, w=False))
        
        self.pieces = c
    
    def __str__(self):
        """ Ritorna output di print(Board)"""
        
        l = ["-"] * 64
        for piece in self.pieces:
            try:
                l[piece.x + (piece.y - 1) * 8 - 1] = str(piece)[0]
            except:
                return str((piece.x, piece.y))
        a = ""
        for i in range(64):
            if i % 8 == 0:
                a += "\n"
            a += l[i]

        return a
 
    def get(self, x, y):
        """ Ritorna quale pezzo c'è nella posizione richiesta """
        for p in self.pieces:
            if (x, y) == (p.x, p.y):
                return p
        return False
    
    def kill(self, piece):

        
        if piece in self.pieces:
            self.pieces.remove(piece)
            return True
        return False
    def move(self, x, y, x1, y1):
        piece = self.get(x, y)
        if piece != False:
            return piece.move(x1, y1)
        print("non Trovato")
        return False


d = Board()
print(d)
