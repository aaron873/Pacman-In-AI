from pacmanAgent import PacmanAgent
from ghost import Ghost
from random import randrange
from math import sqrt
import pygame

#************************************************#
# RunPacman Class                                #
# Handles the execution of the Pacman In AI Game #
#************************************************#
class RunPacman:
    
    
    ##############################
    # RunPacman Member Variables #
    ##############################
    
    # Minimum width and height of the window
    winWidth = 600
    winHeight = 600
    
    # Pacman object
    pacman = None   
    
    # List of Ghosts
    ghosts = []

    # Reference to the Environment
    environment = None
    
    wonGame = 0
    reachedGoal = False
    
    
    ###############################
    # RunPacman Class Constructor #
    ###############################
    def __init__(self, environment):
        self.run = True
        self.display = None
        self.pacmanImgs = None
        self.pacmanRight_image = None
        self.pacmanDown_image = None
        self.pacmanLeft_image = None
        self.pacmanUp_image = None
        self.ghost_image = None
        self.block_image = None
        self.dot_image = None
        
        # Environment (Environment) and Pacman
        self.environment = environment
        self.pacman = PacmanAgent(self.environment)
        self.wonGame = 0
        
        self.ghosts = []
        
        # Ghosts
        self.ghosts.append(Ghost(self.environment, self.pacman, 6, 6))
        self.ghosts.append(Ghost(self.environment, self.pacman, 6, 8))
        self.ghosts.append(Ghost(self.environment, self.pacman, 8, 8))
        self.ghosts.append(Ghost(self.environment, self.pacman, 8, 6))
       
        self.initGame()


    ############################################################################
    # Desc: Initializes the program. Draws walls and pacman location           #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################
    def initGame(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.winWidth, self.winHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Pac-man AI")
        self.run = True
        self.pacmanRight_image = pygame.image.load("imgs\\playerRight.png").convert()
        self.pacmanDown_image = pygame.image.load("imgs\\playerDown.png").convert()
        self.pacmanLeft_image = pygame.image.load("imgs\\playerLeft.png").convert()
        self.pacmanUp_image = pygame.image.load("imgs\\playerUp.png").convert()
        self.pacmanImgs = [self.pacmanRight_image, self.pacmanDown_image, self.pacmanLeft_image, self.pacmanUp_image]
        self.ghost_image = pygame.image.load("imgs\\ghost.png").convert()
        self.block_image = pygame.image.load("imgs\\block.png").convert()
        self.dot_image = pygame.image.load("imgs\\pacDot.png").convert()
        
        
    #############################################
    # Desc: Keeps each frame execution running  #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def on_loop(self, action):
        
        direction = action
        self.pacman.move(direction)
        
        # If pacman has reached his goal
        if self.pacman.endMovement == True:
                
                self.reachedGoal = True
                
                # If pacman has ran over a dot
                if self.pacman.hitDot == True:
                    self.currReward = 1
            
                self.pacman.endMovement = False
                self.pacman.hitDot = False
        
        for ghost in self.ghosts:
            ghost.move()
            
            # If a ghost runs over pacman
            if self.pacman.mapX == ghost.mapX and self.pacman.mapY == ghost.mapY:
                
                self.run = False
                self.currReward = -1
                self.stopGame()
                self.wonGame = -1
        
                
        

    #############################################
    # Desc: Updates the Progam graphical window #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def render(self):
        self.display.fill((0,0,0))
        self.environment.draw(self.display, self.block_image, self.dot_image)
        
        for ghost in self.ghosts:
            self.display.blit(self.ghost_image, (ghost.x, ghost.y))
            
        self.display.blit(self.pacmanImgs[self.pacman.direction], (self.pacman.x, self.pacman.y))
            
        pygame.display.flip()
  

  
    ################################
    # Desc: Terminates the program #
    # Inputs: Reference to self    #
    # Outputs: None                #
    ################################
    def stopGame(self):
        pygame.quit()
        
        
        
    #####################################################
    # Desc: Begins and handles execution of the Program #
    # Inputs: Reference to self                         #
    # Outputs: None                                     #
    #####################################################
    def executeMove(self, action):
        
        self.reachedGoal = False
        self.currReward = 0
            
        #########################################################################
        # This loop is called every frame. It is the main loop driving the game #
        #########################################################################
        while(not self.reachedGoal and self.run):                
            
            # Updates the window every frame showing new movements of the AI Agents 
            self.on_loop(action)
            if self.run:
                self.render()
            
            # These are executed every frame to check if the user wants to quit the game 
            # Exits the Program if user clicks the x window button
                for even in pygame.event.get():
                    if even.type == pygame.QUIT: 
                        self.stopGame()
                        exit()
            
            # Check if all dots have been collected
            if(self.environment.currPacDots == 0):
                print("Pac-man collected all the Pac-Dots!!!")
                self.run = False
                self.wonGame = 1
                self.stopGame()
        
        
    ######################################################
    # Desc: Makes sure Pac-Man does not walk into a wall #
    # Inputs: Reference to self                          #
    # Outputs: None                                      #
    ######################################################     
    def getValidMove(self,direction):
        
        # Store it in a variable so that the move() function called every frame can move in the correct direction
        tempX = self.pacman.effectOnXMovement[direction] + self.pacman.mapX
        tempY = self.pacman.effectOnYMovement[direction] + self.pacman.mapY
        
        # Keep looping until a direction without a wall is given
        while (self.environment.environment[ tempY ][ tempX ] == 1 ):
            #print("There is a wall to the ", self.pacman.currentDirectionStr[direction])
            self.currReward = -1
            
            # Read comments above for description
            direction = randrange(0, 4, 1)    
            tempX = self.pacman.effectOnXMovement[direction] + self.pacman.mapX
            tempY = self.pacman.effectOnYMovement[direction] + self.pacman.mapY
    
        return direction
    
 

    ###############################################################
    # Desc: Returns the reward received by Pac-man for its action #
    #       Calculated based on closest dot and closest ghost.    #
    # Inputs: Reference to self                                   #
    # Outputs: None                                               #
    ###############################################################
    def getReward(self):
    
        # If Pacman hit a ghost or wall
        if self.currReward == -1:
            return -100
        
        # If pacman hits a pacdot
        elif self.currReward == 1:
           
            # Calculate a reward based on distance to closest ghost
            distanceToClosestGhost = 1000000
            
            for ghost in self.ghosts:
                tempDistance = sqrt( ((self.pacman.destinationX - ghost.destinationX) ** 2) + ((self.pacman.destinationY - ghost.destinationY) ** 2) )
                if tempDistance < distanceToClosestGhost:
                    distanceToClosestGhost = tempDistance
            
            
            if distanceToClosestGhost > 3:
                self.currReward = 1

            else:
                self.currReward = -0.7 + (distanceToClosestGhost/10)
            
            return self.currReward
        
        # If pacman did not hit anything
        else:
            
            # Calculate a reward based on distance to closest ghost and closest dot
            distanceToClosestGhost = 1000
            distanceToClosestDot = 1000 
            
            # find distance to closest ghost
            for ghost in self.ghosts:
                tempDistance = sqrt( ((self.pacman.destinationX - ghost.destinationX) ** 2) + ((self.pacman.destinationY - ghost.destinationY) ** 2) )
                if tempDistance < distanceToClosestGhost:
                    distanceToClosestGhost = tempDistance
                    
             # Loop through all indexes in 2D environment array
            for loopY in range(self.environment.height):
                for loopX in range(self.environment.width):
                
                    # If there is a pacDot at this index, check to see if its distance is 
                    # closer than the previous minDistance
                    if self.environment.environment[loopY][loopX] == 2:
                        tempDistance = sqrt( ((self.pacman.destinationX - loopX) ** 2) + ((self.pacman.destinationY - loopY) ** 2) )  
                        if (tempDistance < distanceToClosestDot):
                            distanceToClosestDot = tempDistance
            
            if distanceToClosestGhost > 3:
                
                # Make sure no division by zero
                if distanceToClosestDot != 0:
                    self.currReward = 1/distanceToClosestDot - 0.75 
                
                else:
                    self.currReward = 0
            else:
                self.currReward = ((distanceToClosestDot/50) - (1 - (distanceToClosestGhost/10)))

            return self.currReward
