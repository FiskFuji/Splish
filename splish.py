#==============================================================================#
#                                  "Splish"                                    #
#==============================================================================#
#                                                                              #
#   Title:      "Splish"                                                       #
#                                                                              #
#   Author:     Kirk Worley                                                    #
#                                                                              #
#   Dates:      ------------                                                   #
#               10.14.2016:     Started project.                               #
#               ---                                                            #
#               ---                                                            #
#                                                                              #
#   Abstract:   Minigame using Python 2.7.9 and PyGame 1.9.1, to become more   #
#               comfortable using PyGame classes and methods; as well as to    #
#               attempt to use OOP styles, as well as new and advanced         #
#               Python programming techniques.                                 #
#                                                                              #
#   GitHub:     www.github.com/KirkWorl                                        #
#                                                                              #
#:::::::::::::::#--------------------------------------------------------------#
version = 1.0   #   Versioning Purposes                                        #
#:::::::::::::::#--------------------------------------------------------------#
#==============================================================================#

#===BEGIN PROGRAM==============================================================#
#---Import Modules---------------------------------------------------------#
import random as rnd
import pygame as pgm
import sys

#------Splish Class------------------------------------------------------------#
#   This class is the game. It contains multiple other classes needed to       #
#   run the game.                                                              #
#---------Components:----------------------------------------------------------#
#
#
#
#
#
#------------------------------------------------------------------------------#
class Splish:

    #---Board Class------------------------------------------------------------#
    #   This class contains all the workings of the board that the game is     #
    #   played on.                                                             #
    #------Components:---------------------------------------------------------#
    # __init__ : 
    #
    #
    #--------------------------------------------------------------------------#
    class Board:

        #---Initialize Definition---#
        def __init__(self):
            self.field = []
            self.fieldPos = []
            self.ammo = 24
            self.boards = {
                1: [". . . . . . . .",
                    ". 2 . . . 3 . .",
                    ". 2 . . . 3 . .",
                    ". . . . . 3 . .",
                    ". . . . . . . .",
                    ". . . 4 4 4 4 .",
                    ". . . . . . . .",
                    ". . . . . . . ."],
  
                2: [". . . . . . . .",
                    ". . 2 2 . . . .",
                    ". . . . . . . .",
                    ". . . . . . . .",
                    ". 4 . . . . 3 .",
                    ". 4 . . . . 3 .",
                    ". 4 . . . . 3 .",
                    ". 4 . . . . . ."],

                3: [". . . . . . . .",
                    ". . . . . . . .",
                    ". 4 4 4 4 . . .",
                    ". . . . . . . .",
                    ". . . . . . . .",
                    ". . . . . 3 3 3",
                    ". . . . . . 2 .",
                    ". . . . . . 2 ."]
                }

            for i in range(0, 7):
                self.fieldPos.append([0, 0, 0, 0, 0, 0, 0, 0])
                    

        #---CreateBoard Definition---#
        def createBoard(self):
            self.field = self.boards[rnd.randint(1, len(self.boards))]
            self.col = 0
            self.row = 0
            
            for line in self.field:

                if not(isinstance(line, str)):
                    raise ValueError("The chosen board contained an element in which the row was not a string!")
                    break
                
                for char in line:

                    if(char == ' '):
                        continue

                    elif(char == '.'):
                        self.fieldPos[self.row][self.col] = 0
                        self.col += 1

                    elif(char in '2 3 4' and char != ' '):
                        self.fieldPos[self.row][self.col] = int(char)
                        self.col += 1

                self.row += 1




x = Splish.Board()
x.createBoard()

print x.fieldPos
print x.field
            



























    
    
