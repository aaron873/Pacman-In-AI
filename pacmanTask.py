from pybrain.rl.environments.task import Task
from runPacman import RunPacman
import pygame

#*****************************************************************#
# Pac-Man Task Class                                              #
# This is the Pac-Man Task Class, a child of PyBrain's Task Class #
# It holds the agent's actions, rewards, and interaction with the #
# environment.                                                    #     
#*****************************************************************#

class PacmanTask(Task):
    
    # This initializes the Task that the Pac-Man agent will be completing
    def __init__(self, environment, game):
        self.env = environment
        self.game = game
        
    # This calls to the environment to return the needed information into the PyBrain Q-Learning library   
    def getObservation(self):
        return self.env.getSensors()
        
    # This is called by PyBrain to give the Pac-Man a certain action to take in the environment
    # It represents a direction for the agent to move in the maze
    def performAction(self, action):        
        action = self.game.getValidMove(int(action.tolist()[0]))
        self.game.executeMove(action)
        
    # This function calls the game's function to give a reward to the agent based on its previous action    
    def getReward(self):
        return self.game.getReward()
        
