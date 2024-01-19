# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent
from pacman import GameState

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState: GameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState: GameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py) 


        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newFood = successorGameState.getFood()
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***" 
        if currentGameState.isWin() or currentGameState.isLose():
            return currentGameState.getScore()
        ghostDistance = 0
        for ghost in newGhostStates: 
            ghostPosition = ghost.getPosition
            dist = manhattanDistance(newPos, ghost.getPosition())
            if dist < ghost.scaredTimer: ghostDistance = 999999
            elif dist < 2: 
                ghostDistance = -999999
                break
        food_Distance = 999999 
        food_list = newFood.asList()
        for food in food_list : 
            Distance_from_food = manhattanDistance(newPos, food)
            if Distance_from_food < food_Distance: food_Distance = Distance_from_food        
        return successorGameState.getScore() + ghostDistance + (1.0 / food_Distance) 

def scoreEvaluationFunction(currentGameState: GameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState: GameState):
        def minimax(state, agentIndex, depth):
            if agentIndex == 0:
                depth -= 1
            if depth < 0 or state.isWin() or state.isLose():
                return (self.evaluationFunction(state), None)
            bestValue = float('-inf') if agentIndex == 0 else float('inf')
            bestAction = None
            actions = state.getLegalActions(agentIndex)
            for action in actions:
                successor, _ = minimax(state.generateSuccessor(agentIndex, action), (agentIndex + 1) % state.getNumAgents(), depth)
                nextValue = successor
                if agentIndex == 0:
                    if bestValue < nextValue:
                        bestValue = nextValue
                        bestAction = action
                else:
                    if bestValue > nextValue:
                        bestValue = nextValue
                        bestAction = action

            return (bestValue, bestAction)

        return minimax(gameState, self.index, self.depth)[1]



class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState: GameState):
        def alpha_beta_search(state, current_agent, remaining_depth, alpha, beta):
            if current_agent == 0:
                remaining_depth -= 1
            if remaining_depth < 0 or state.isWin() or state.isLose():
                return (self.evaluationFunction(state), None)
            best_value = float('-inf') if current_agent == 0 else float('inf')
            best_action = None
            for action in state.getLegalActions(current_agent):
                next_state = state.generateSuccessor(current_agent, action)
                successor_value, _ = alpha_beta_search(next_state, (current_agent + 1) % state.getNumAgents(), remaining_depth, alpha, beta)
                if current_agent == 0:
                    if successor_value > best_value:
                        best_value = successor_value
                        best_action = action
                    if best_value > beta:
                        return (best_value, best_action)
                    alpha = max(alpha, best_value)
                else:
                    if successor_value < best_value:
                        best_value = successor_value
                        best_action = action
                    if best_value < alpha:
                        return (best_value, best_action)
                    beta = min(beta, best_value)
            return (best_value, best_action)

        _, best_action = alpha_beta_search(gameState, self.index, self.depth, float('-inf'), float('inf'))
        return best_action






class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState: GameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def minimax(state, current_agent, remaining_depth):
            if current_agent == 0:
                remaining_depth -= 1
            if remaining_depth < 0 or state.isWin() or state.isLose():
                return (self.evaluationFunction(state), None)

            if current_agent == 0:
                # max-value
                best_value, best_action = float('-inf'), None
                for action in state.getLegalActions():
                    next_value, _ = minimax(state.generateSuccessor(current_agent, action), (current_agent + 1) % state.getNumAgents(), remaining_depth)
                    if next_value > best_value:
                        best_value, best_action = next_value, action
                return (best_value, best_action)

            # exp-value
            total_value = 0
            total_value += sum(minimax(state.generateSuccessor(current_agent, action), (current_agent + 1) % state.getNumAgents(), remaining_depth)[0] for action in state.getLegalActions(current_agent))


            return (total_value / len(state.getLegalActions(current_agent)), None)

        return minimax(gameState, self.index, self.depth)[1]

def betterEvaluationFunction(currentGameState: GameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pacman_pos = currentGameState.getPacmanPosition()
    food_distances = [util.manhattanDistance(pacman_pos, food) for food in currentGameState.getFood().asList()]
    closest_food_distance = min(food_distances) if food_distances else 0
    ghost_states = currentGameState.getGhostStates()
    ghost_distances = [manhattanDistance(pacman_pos, ghost.getPosition()) for ghost in ghost_states]
    score = currentGameState.getScore()
    
    if len(food_distances)==0:
        score += 10
    else:
        score += 10 / closest_food_distance 
    
    for i, dist in enumerate(ghost_distances):
        if dist > 0:
            if ghost_states[i].scaredTimer > 0:
                score += 55
            else:
                score -= 7 / dist
        else:
            return -99999999
    
    return score

# Abbreviation
better = betterEvaluationFunction

