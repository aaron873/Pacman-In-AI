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
    
    controller = ActionValueTable(196, 4)
    controller.initialize(0.)
    
    # Initialize Reinforcement Learning
    learner = Q(0.5, 0.0)
    learner._setExplorer(EpsilonGreedyExplorer(0.0))
    agent = LearningAgent(controller, learner)
    
    environment = Environment()
    
    game = RunPacman(environment)
    #game.executeMove(np.ndarray([1]))
    
    task = PacmanTask(environment, game)
    task.performAction(np.array([1]))
    
    experiment = Experiment(task, agent)
    
    while True:
        
        experiment.doInteractions(1)
        agent.learn()
        
        # Check if current pacman game ended and needs to start a new one
        if game.wonGame == 1 or game.wonGame == -1:
            agent.reset()
            environment.resetMap()
            game = RunPacman(environment)
            
            task = PacmanTask(environment, game)
            task.performAction(np.array([1]))
    
            experiment = Experiment(task, agent)
            
    
    
            
            
            
            
            
            
