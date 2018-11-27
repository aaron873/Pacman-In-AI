import pygame
import random
import math
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q
from pybrain.rl.agents import LearningAgent
from pybrain.rl.experiments import Experiment
from pybrain.rl.explorers import EpsilonGreedyExplorer

from pacmanTask import PacmanTask

from pacmanAgent import PacmanAgent
from ghost import Ghost
from pacmanEnvironment import Environment         
                
                

        
        
        
###############################################################
# The main function that begins running our Pacman-In-AI game #
###############################################################
if __name__ == "__main__" :
    #game = RunPacman()
    #game.executeGame()
    print("hello")
    
    controller = ActionValueTable(196, 4)
    controller.initialize(0.)
    
    # Initialize Reinforcement Learning
    learner = Q(0.5, 0.0)
    learner._setExplorer(EpsilonGreedyExplorer(0.0))
    agent = LearningAgent(controller, learner)
    
    environment = Environment()
    task = PacmanTask(environment)

    experiment = Experiment(task, agent)
    
    while True:
        experiment.doInteractions(1)
        agent.learn()
        agent.reset()
    
    
    
            
            
            
            
            
            
