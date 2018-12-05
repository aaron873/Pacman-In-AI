import pygame
import random
import math
import numpy as np
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q
from pybrain.rl.agents import LearningAgent
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer

from pacmanTask import PacmanTask

from pacmanAgent import PacmanAgent
from runPacman import RunPacman
from ghost import Ghost
from pacmanEnvironment import Environment         
                
        
        
###############################################################
# The main function that begins running our Pacman-In-AI game #
###############################################################
if __name__ == "__main__" :
    
    # Initialize our Action-Environment-Reward Table
    controller = ActionValueTable(196, 4)
    controller.initialize(0.)
    
    # Initialize Reinforcement Learning
    learner = Q(0.5, 0.0)
    learner._setExplorer(EpsilonGreedyExplorer(0.0))
    agent = LearningAgent(controller, learner)
    
    # Setup the PyBrain and PyGame Environments
    environment = Environment()
    game = RunPacman(environment)
    
    # Create the Task for the Pac-Man Agent to Accomplish and initialize the first Action
    task = PacmanTask(environment, game)
    task.performAction(np.array([1]))
    
    # The Experiment is the PyBrain link between the task to be completed and the agent completing it
    experiment = Experiment(task, agent)
    currentGame = 1
    
    # Continue to loop program until the 'X' on the GUI is clicked
    while True:
        
        # Allow the agent to interaction with the environment (Move in a direction) then learn from it.
        experiment.doInteractions(1)
        agent.learn()
        
        # Check if current pacman game ended and needs to start a new one
        if game.wonGame == 1 or game.wonGame == -1:
            currentGame += 1
            
            # Store the information the agent has learned in long term memory,
            # Clear the short term memory to reduce any chance of overfitting,
            # Reset the Pac-Man game, and the environment for the next game test
            agent.reset()
            environment.resetMap()
            game.__init__(environment)
            
    
    
            
            
            
            
            
            
