########################################################################
#                                                                           
#                              Mastermind                                      
#                                                                           
#                             Mastermind.py                                      
#                                                                           
#                                MAIN                                      
#                                                                           
#                 Copyright (C) 1997 Ulrik Hoerlyk Hjort                   
#                                                                           
#  Mastermind is free software;  you can  redistribute it                          
#  and/or modify it under terms of the  GNU General Public License          
#  as published  by the Free Software  Foundation;  either version 2,       
#  or (at your option) any later version.                                   
#  Mastermind is distributed in the hope that it will be                           
#  useful, but WITHOUT ANY WARRANTY;  without even the  implied warranty    
#  of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.                  
#  See the GNU General Public License for  more details.                    
#  You should have  received  a copy of the GNU General                     
#  Public License  distributed with Yolk.  If not, write  to  the  Free     
#  Software Foundation,  51  Franklin  Street,  Fifth  Floor, Boston,       
#  MA 02110 - 1301, USA.                                                    
########################################################################                                                                          
import random
import sys




##################################################################
#
# Create an random code from list "pegs" of length "length"
#
##################################################################
def setCode(pegs,length):
   codeList = []
   for i in range (0,length):
      codeList.append(pegs[random.randrange(0, len(pegs))])  
   return codeList


##################################################################
#
# Compare the guess "guessIn" with the code "codeIn" and returns
# a list with information of correct pegs by a "W" and correct placed
# pegs by a "B" 
#
##################################################################
def testGuess(guessIn,codeIn):
   
   guess = guessIn[:]
   code = codeIn[:]
   status = []

   for i in range (0, len(code)):
     if guess[i] == code[i]:
        status.append("B")
        code[i] = 0
        guess[i] = -1

   for i in range (0, len(code)):
     if guess[i] in code:
        status.append("W")
        code[code.index(guess[i])] = 0
        guess[i] = -1
   return status

##################################################################
#
# Print out the code "code"
#
##################################################################
def printCode(code):
   for i in range (0, len(code)):
     print code[i],



##################################################################
#
# Returns true if the "status" list contains "B" on all places, 
# otherwise false
#
##################################################################
def chkStatus(status, length):

   for i in range (0,len(status)):
      if status[i] != "B":
         return False

   if len(status) == length:
      return True
   else:
      return False



##################################################################
#
# Solve a code by random guesses
#
##################################################################
def randomSolver():

   pegList = [1,2,3,4,5,6]
   codeLength = 4   

   code = setCode(pegList,codeLength)
   printCode(code)
   solved = False
   guessNumber = 1
   while solved == False:
     guess = setCode(pegList,codeLength)
     status = testGuess(guess,code)
     print guessNumber,code, guess,status
     solved = chkStatus(status,codeLength)
     guessNumber = guessNumber + 1




##################################################################
#
# Read a guess from stdin and return the guess as a list
#
##################################################################
def readGuess():
   guess = raw_input("Enter guess: ")
   list = guess.split(' ')
   numList = []
   for item in list:
    numList.append(int(item))
   return numList



##################################################################
#
# Start a game
#
##################################################################
def play(pegs, codeLength, numberOfGuesses):

   pegList = []
   
   for i in range (1,pegs+1):
     pegList.append(i) 

   code = setCode(pegList,codeLength)
   printCode(code)
   solved = False
   guessNumber = 1
   while (solved == False) and (guessNumber <= numberOfGuesses):
     guess = readGuess()
     status = testGuess(guess,code)
     print guessNumber,code, guess,status
     solved = chkStatus(status,codeLength)
     guessNumber = guessNumber + 1
   
   return solved

##################################################################
#
# Main
#
##################################################################
pegs       = int(raw_input("Enter number of pegs: "))
codeLength = int(raw_input("Enter code length: "))
guesses    = 10
solved = play(pegs,codeLength, guesses)
print "Solved: ", solved
