from pybrain.rl.environments.task import Task
from runPacman import RunPacman
import pygame

class PacmanTask(Task):
    
    def __init__(self, environment):
        self.env = environment
        self.gameReference = RunPacman(environment)
        self.gameReference.executeGame()
        
    def getObservation(self):
        return self.env.getSensors()
        
    def performAction(self, action):
        #self.env.performAction(action)
        print("")
        
    def getReward(self):
        return self.gameReference.getReward()
        
