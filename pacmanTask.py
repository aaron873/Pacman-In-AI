from pybrain.rl.environments.task import Task
from runPacman import RunPacman
import pygame

class PacmanTask(Task):
    
    def __init__(self, environment, game):
        self.env = environment
        self.game = game
        #self.gameReference = RunPacman(environment)
        #self.gameReference.executeGame()
        
    def getObservation(self):
        return self.env.getSensors()
        
    def performAction(self, action):
        #self.env.resetMap()
        print("PACMAN TAKE ACTION", action)
        
        #action = int(action.tolist()[0])
        action = self.game.getValidMove(int(action.tolist()[0]))
        print("MOVING: ",action)
        self.game.executeMove(action)
        
        #self.gameReference = RunPacman(self.env)
        #self.gameReference.executeGame()
        #print("")
        
    def getReward(self):
        return self.game.getReward()
        
