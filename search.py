# search.py
# ---------
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


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    """

    start = problem.getStartState()
    reached, actions, actlst = [], [], []
    frontier, actionsRev = util.Stack(), util.Stack()
    frontier.push(start)

    node = frontier.pop()
    # depth-first search
    while not problem.isGoalState(node):
        if node not in reached:
            reached.append(node)
            for child in problem.getSuccessors(node):
                frontier.push(child[0])
                actionsRev.push(actions + [child[1]])

        actions = actionsRev.pop()  # traceback path
        node = frontier.pop()

    return actions

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    start = problem.getStartState()
    reached, actions = [], []
    frontier, actionsRev = util.Queue(), util.Queue()
    frontier.push(start)

    node = frontier.pop()
    # breadth-first search
    while not problem.isGoalState(node):
        if node not in reached:
            reached.append(node)
            for child in problem.getSuccessors(node):
                frontier.push(child[0])
                actionsRev.push(actions + [child[1]])

        actions = actionsRev.pop()  # traceback path
        node = frontier.pop()

    return actions

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    start = problem.getStartState()
    frontier, actionsRev = util.PriorityQueue(), util.PriorityQueue()
    reached, actions = [], []

    frontier.push(start, 0)
    node = frontier.pop()
    while not problem.isGoalState(node):
        if node not in reached:
            reached.append(node)
            for child in problem.getSuccessors(node):
                costOfActions = problem.getCostOfActions(actions + [child[1]])
                if child[0] not in reached:
                    frontier.push(child[0], costOfActions)
                    actionsRev.push(actions + [child[1]], costOfActions)

        actions = actionsRev.pop()
        node = frontier.pop()
    
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    start = problem.getStartState()
    frontier, actionsRev = util.PriorityQueue(), util.PriorityQueue()
    reached, actions = [], []

    frontier.push(start, 0)
    node = frontier.pop()
    while not problem.isGoalState(node):
        if node not in reached:
            reached.append(node)
            for child in problem.getSuccessors(node):
                costOfActions = problem.getCostOfActions(actions + [child[1]])
                costOfActions += heuristic(child[0], problem)
                if child[0] not in reached:
                    frontier.push(child[0], costOfActions)
                    actionsRev.push(actions + [child[1]], costOfActions)

        actions = actionsRev.pop()
        node = frontier.pop()
    
    return actions


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
