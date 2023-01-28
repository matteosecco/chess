# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:29:21 2021

@author: Matte
"""

from tkinter import *
from PIL import Image, ImageTk


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

class Board:
    def __init__(self):
        """ Posiziona tutti i pezzi nella scacchiera """
        a = [Pawn(self, x + 1, 2, 1) for x in range(8)]
        b = [Pawn(self, x + 1, 7, -1) for x in range(8)]
        c = a + b
        c.append(Rook(self, 1, 1, 1))
        c.append(Rook(self, 8, 1, 1))
        c.append(Rook(self, 1, 8, -1))
        c.append(Rook(self, 8, 8, -1))
        c.append(Bishop(self, 3, 1, 1))
        c.append(Bishop(self, 6, 1, 1))
        c.append(Bishop(self, 3, 8, -1))
        c.append(Bishop(self, 6, 8, -1))
        c.append(Bishop(self, 6, 4, 1))
        c.append(Knight(self, 7, 1, 1))
        c.append(Knight(self, 2, 1, 1))
        c.append(Knight(self, 7, 8, -1))
        c.append(Knight(self, 2, 8, -1))
        c.append(Queen(self, 4, 1, 1))
        c.append(Queen(self, 4, 8, -1))
        c.append(King(self, 5, 1, 1))
        c.append(King(self, 5, 8, -1))
        
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

d.move(3,2,3,4)
print(d)

# grafica
root = Tk()

# board canvas where everything happens
board = Canvas(root, width=100*8, height=100*8, background="black")
board.pack()

board_png = ImageTk.PhotoImage(Image.open("img/board.png"))
board.create_image(400, 400, image=board_png)

# create every piece img
img_list = []  # needede to keep track of all the pngs
img_list2 = []  # needed to find images on click
for piece in d.pieces:
    png = ImageTk.PhotoImage(Image.open("img/" + piece.id + ".png"))
    img = board.create_image(piece.x * 100 - 50, piece.y * 100 - 50, image=png)
    img_list.append(png)
    img_list2.append(img)

# object under click
tobemoved = ()

def click(mouse):
    """ Find the object to be moved after the click """
    global tobemoved
    tobemoved = list(board.find_overlapping(mouse.x - 4, mouse.y + 4, mouse.x + 4, mouse.y + 4))
    tobemoved.remove(1)
    print(tobemoved)

def motion(mouse):
    """ Updates the position of the object each frame """
    global tobemoved
    c = board.coords(tobemoved)

    if len(tobemoved) > 1:
        return False
    board.move(tobemoved, mouse.x - c[0], mouse.y - c[1])

def release(mouse):
    """ Moves the object to the center of its square """
    global tobemoved

    # if there's none or the click is too close to both
    if tobemoved == [] or len(tobemoved) > 1:
        return False

    c = board.coords(tobemoved)
    real = [int(round(c[0] / 50) * 50), int(round(c[1] / 50) * 50)]
    if real[0] % 100 == 0 and c[0] % 50 <= 25:
        real[0] += 50
    elif real[0] % 100 == 0 and c[0] % 50 > 25:
        real[0] -= 50
    if real[1] % 100 == 0 and c[1] % 50 <= 25:
        real[1] += 50
    elif real[1] % 100 == 0 and c[1] % 50 > 25:
        real[1] -= 50

    diff = real[0] - c[0], real[1] - c[1]
    print(c, real, diff)
    board.move(tobemoved, diff[0], diff[1])

board.bind("<Button-1>", click)
board.bind("<B1-Motion>", motion)
board.bind("<ButtonRelease-1>", release)

root.mainloop()




