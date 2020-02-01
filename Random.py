import random
import sys
sys.path.append("..")  #so other modules can be found in parent dir
from Player import *
from Constants import *
from Construction import CONSTR_STATS
from Ant import UNIT_STATS
from Move import Move
from GameState import *
from AIPlayerUtils import *


##
#AIPlayer
#Description: The responsbility of this class is to interact with the game by
#deciding a valid move based on a given game state. This class has methods that
#will be implemented by students in Dr. Nuxoll's AI course.
#
#Variables:
#   playerId - The id of the player.
##
class AIPlayer(Player):

    #__init__
    #Description: Creates a new Player
    #
    #Parameters:
    #   inputPlayerId - The id to give the new player (int)
    #   cpy           - whether the player is a copy (when playing itself)
    ##
    def __init__(self, inputPlayerId):
        super(AIPlayer,self).__init__(inputPlayerId, "Random")
    
    ##
    #getPlacement
    #
    #Description: called during setup phase for each Construction that
    #   must be placed by the player.  These items are: 1 Anthill on
    #   the player's side; 1 tunnel on player's side; 9 grass on the
    #   player's side; and 2 food on the enemy's side.
    #
    #Parameters:
    #   construction - the Construction to be placed.
    #   currentState - the state of the game at this point in time.
    #
    #Return: The coordinates of where the construction is to be placed
    ##
    def getPlacement(self, currentState):
        numToPlace = 0
        #implemented by students to return their next move
        if currentState.phase == SETUP_PHASE_1:    #stuff on my side
            numToPlace = 11
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    #Choose any x location
                    x = random.randint(0, 9)
                    #Choose any y location on your side of the board
                    y = random.randint(0, 3)
                    #Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        #Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        elif currentState.phase == SETUP_PHASE_2:   #stuff on foe's side
            numToPlace = 2
            moves = []
            for i in range(0, numToPlace):
                move = None
                while move == None:
                    #Choose any x location
                    x = random.randint(0, 9)
                    #Choose any y location on enemy side of the board
                    y = random.randint(6, 9)
                    #Set the move if this space is empty
                    if currentState.board[x][y].constr == None and (x, y) not in moves:
                        move = (x, y)
                        #Just need to make the space non-empty. So I threw whatever I felt like in there.
                        currentState.board[x][y].constr == True
                moves.append(move)
            return moves
        else:
            return [(0, 0)]
    
    ##
    #getMove
    #Description: Gets the next move from the Player.
    #
    #Parameters:
    #   currentState - The state of the current game waiting for the player's move (GameState)
    #
    #Return: The Move to be made
    ##
    def getMove(self, currentState):
        # Generate a list of all possible moves that could be made from the given GameState. AIPlayerUtils.py contains a method that will do this for you.
        all_legal_moves = listAllLegalMoves(currentState)
        
        list_len = len(all_legal_moves)

        # Generate a list of the GameState objects that will result from making each possible move.
        all_legal_move_gamestate_objects = []

        count = 0
        for moves in all_legal_moves:
            print(count, moves)
            count+=1
            all_legal_move_gamestate_objects.append(getNextState(currentState, moves))

        print("====================")

        # Depth will always be 1 for part A
        depth = 1

        node_list = []

        for index in range(list_len):
            node = self.createNode(all_legal_moves[index], all_legal_move_gamestate_objects[index], depth, currentState)
            node_list.append(node)



        for node in node_list:
            print(node)

        print("====================")



        moves = listAllLegalMoves(currentState)
        selectedMove = moves[random.randint(0,len(moves) - 1)];

        #don't do a build move if there are already 3+ ants
        numAnts = len(currentState.inventories[currentState.whoseTurn].ants)
        while (selectedMove.moveType == BUILD and numAnts >= 3):
            selectedMove = moves[random.randint(0,len(moves) - 1)];
            
        return selectedMove


        # Generate a list of the GameState objects that will result from making each possible move. You will probably find the getNextState() method in
        #AIPlayerUtils.py helpful for this part. (Do not use getNextStateAdversarial().)
        
        #Use each move and GameState to create a node (see above). Then, put all these nodes in a list. 
        #Currently, creating this list may feel like a waste of cycles. Do it anyway as you’ll need this list in Part B.
        
        #Return the move associated with the node that has the highest evaluation.
    
    ##
    #getAttack
    #Description: Gets the attack to be made from the Player
    #
    #Parameters:
    #   currentState - A clone of the current state (GameState)
    #   attackingAnt - The ant currently making the attack (Ant)
    #   enemyLocation - The Locations of the Enemies that can be attacked (Location[])
    ##
    def getAttack(self, currentState, attackingAnt, enemyLocations):
        #Attack a random enemy.
        return enemyLocations[random.randint(0, len(enemyLocations) - 1)]

    ##
    #registerWin
    #
    # This agent doens't learn
    #
    def registerWin(self, hasWon):
        #method templaste, not implemented
        pass


    ##
    #
    #heuristicStepsToGoal
    #
    #
    def heuristicStepsToGoal(self, currentState):
        return 1


    ##
    #
    #bestMove
    #
    #search a given list of nodes to find the one with 
    #the best evaluation and return it to the caller
    #
    def bestMove(self, currentState):
        return ""


    ##
    #
    #createNode
    #
    # creates a node based on 
    #
    def createNode(self, move_taken, move_taken_gamestate, depth, parent_state):
        
        return {
                "move":move_taken,
                "move_taken_state":move_taken_gamestate,
                "depth":depth,
                "evaluation": self.heuristicStepsToGoal(move_taken_gamestate),
                "parent_state":parent_state
                }


