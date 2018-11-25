import pygame
import random
import math
from pybrain.rl.learners.valuebased import ActionValueTable
from pybrain.rl.learners import Q
from pybrain.rl.agents import LearningAgent


#************************************#
# Pacman Agent Class                 #
# Need Description Here              #
#************************************#

class Pacman:
    
    ###########################
    # Pacman Member Variables #
    ###########################
    
    # Pacman's current location in reference to the graphical window
    x = 40
    y = 120
    
    # Pacman's current location in reference to the 2D array in Location
    mapX = 1
    mapY = 3
    
    #Coordinates for the closest Pac-dot to Pac-Man
    closestPacDotX = 0
    closestPacDotY = 0
    
    # Referencing which direction to go
    right = 0
    down = 1
    left = 2
    up = 3
    
    # Direction's effect on movement. 
    # Example: if pacman is moving right, idx 0, his y change is 0 and x change is +1.  
    effectOnXMovement = [1, 0, -1, 0]
    effectOnYMovement = [0, 1, 0, -1]
    
    # Current movement direction and destination. Used when AI moves each frame
    direction = 0
    destinationX = 0
    destinationY = 0
    currentDirectionStr = ["Right", "Down", "Left", "Up"]
    
    # Pacman's speed
    speed = 0.05
    
    # Reference to the Environment class to give our Pacman Agent vision of the Environment
    environment = None
    
  
    ###########################
    # Pacman Member Functions #
    ###########################
    
    
    # Pacman Class Constructor
    def __init__(self, input_environment):
        self.environment = input_environment  
        self.randomSpawn()
        self.initializeMovement()
        
        
        
    #########################################
    # Randomly Spawning Pacman on the board #
    #########################################
    def randomSpawn(self):
        
        spawnLocations = [[1,1],[1,13],[13,1],[13,13]]
        
        randomIdx = random.randrange(0, 3, 1)
            
        self.mapX = spawnLocations[randomIdx][0]
        self.mapY = spawnLocations[randomIdx][1]
                
        self.x = self.mapX * 40
        self.y = self.mapY * 40
                
        print(self.mapX)
        print(self.mapY)
               
        self.environment.environment[self.mapY][self.mapX] = 0                                
                
                
    
    # Right movement
    def movRight(self):
        self.x = self.x + self.speed
    
    # Left movement    
    def movLeft(self):
        self.x = self.x - self.speed
    
    # Up movement    
    def movUp(self):
        self.y = self.y - self.speed
    
    # Down movement    
    def movDown(self):
        self.y = self.y + self.speed
        
        
        
    ############################################################################
    # Desc: This is a function to get a new randomized movement direction      #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def initializeMovement(self):
        
        
        ################################
        # Searching Algorithm Movement #
        ################################
        
        pacDotDistance = 100
        
        # Loop through all indexes in 2D environment array
        for loopY in range(self.environment.height):
            for loopX in range(self.environment.width):
                
                # If there is a pacDot at this index, check to see if its distance is 
                # closer than the previous minDistance
                if self.environment.environment[loopY][loopX] == 2:
                    tempDistance = math.sqrt( ((self.mapX - loopX) ** 2) + ((self.mapY - loopY) ** 2) )  
                    if (tempDistance < pacDotDistance):
                        pacDotDistance = tempDistance
                        self.closestPacDotX = loopX
                        self.closestPacDotY = loopY
        
        # Get the direction to the closest PacDot
        # If Pacman should move Right
        if (self.closestPacDotX > self.mapX):
            self.direction = 0
        # If Pacman should move Down
        elif (self.closestPacDotY > self.mapY):
            self.direction = 1
        # If Pacman should move Left
        elif (self.closestPacDotX < self.mapX):
            self.direction = 2
        # If Pacman should move Up
        else:
            self.direction = 3
            
            
        # Set destination vector in 2D array    
        self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
        self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
        
        # If there is a wall, randomly choose a new direction until there is no wall
        while (self.environment.environment[ self.destinationY ][ self.destinationX ] == 1 ):
            print("There is a wall to the", self.currentDirectionStr[self.direction])
            
            # Read comments above for description
            self.direction = random.randrange(0, 4, 1)    
            self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
            self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
            
        #self.mapX = self.destinationX
        #self.mapY = self.destinationY    
        
        
        '''
        #######################
        # RANDOMIZED MOVEMENT #
        #######################
        # Choose a random direction to move in, Right = 0, Down = 1, Left = 2, Up = 3
        self.direction = random.randrange(0, 4, 1)  

        # Store it in a variable so that the move() function called every frame can move in the correct direction
        self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
        self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
        
        # Keep looping until a direction without a wall is given
        while (self.environment.environment[ self.destinationY ][ self.destinationX ] == 1 ):
            print("There is a wall to the", self.currentDirectionStr[self.direction])
            
            # Read comments above for description
            self.direction = random.randrange(0, 4, 1)    
            self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
            self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
            
        # Debug print statement    '''
        print("Moving", self.currentDirectionStr[self.direction])        
     

     
    ############################################################################
    # Desc: This function is called from on_loop to move pacman                #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def move(self):
        
        # Check if Pacman has reached its movement goal
        if(abs(self.x - self.destinationX * 40) <= 0.25 and abs(self.y - self.destinationY * 40) <= 0.25):
            self.mapX = self.destinationX
            self.mapY = self.destinationY
            
            print("Pacman location:",self.mapX,self.mapY)
            
            # Check if Pacman ran over a PacDot
            if(self.environment.environment[self.destinationY][self.destinationX] == 2):
                self.environment.currPacDots -= 1
                self.environment.environment[self.destinationY][self.destinationX] = 0
                print(self.environment.currPacDots)
                
                if(self.environment.currPacDots == 0):
                    print("Pac-man collected all the Pac-Dots!!!")
                    stopGame()
                    
            
            # Initialize a new random movement
            self.initializeMovement()
        
        # If he has not reached his goal, keep moving in the right direction
        else:
            if(self.direction == self.right):
                self.movRight()
            if(self.direction == self.down):
                self.movDown()
            if(self.direction == self.left):
                self.movLeft()
            if(self.direction == self.up):
                self.movUp()



#************************************#
# Ghost Agent Class                  #
# Need Description Here              #
#************************************#

class Ghost:
    
    ###########################
    # Ghost Member Variables  #
    ###########################
    
    # Pacman's current location in reference to the graphical window
    x = 40
    y = 40
    
    # Pacman's current location in reference to the 2D array in Location
    mapX = 1
    mapY = 1
    
    # Coordinates for the closest Pac-dot to Pac-Man
    #closestPacDotX = 0
    #closestPacDotY = 0
    
    # Referencing which direction to go
    right = 0
    down = 1
    left = 2
    up = 3
    
    # Direction's effect on movement. 
    # Example: if pacman is moving right, idx 0, his y change is 0 and x change is +1.  
    effectOnXMovement = [1, 0, -1, 0]
    effectOnYMovement = [0, 1, 0, -1]
    
    # Current movement direction and destination. Used when AI moves each frame
    direction = random.randrange(0, 4, 1)
    destinationX = 0
    destinationY = 0
    currentDirectionStr = ["Right", "Down", "Left", "Up"]
    
    # Ghosts's speed
    speed = 0.05
    
    # Reference to the Environment class and Pacman to give our Ghost vision of the Environment
    environment = None
    pacman = None
    
  
    ###########################
    # Pacman Member Functions #
    ###########################
    
    
    # Pacman Class Constructor
    def __init__(self, input_environment, input_pacman, starting_mapX, starting_mapY):
        self.environment = input_environment  
        self.pacman = input_pacman
        
        self.mapX = starting_mapX
        self.x = self.mapX * 40
        
        self.mapY = starting_mapY
        self.y = self.mapY * 40
        
        self.direction = random.randrange(0, 4, 1)
        
        self.initializeMovement()               
                
                
    
    # Right movement
    def movRight(self):
        self.x = self.x + self.speed
    
    # Left movement    
    def movLeft(self):
        self.x = self.x - self.speed
    
    # Up movement    
    def movUp(self):
        self.y = self.y - self.speed
    
    # Down movement    
    def movDown(self):
        self.y = self.y + self.speed
        
        
        
    ############################################################################
    # Desc: This is a function to get a new randomized movement direction      #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def initializeMovement(self):    
            
        # Set destination vector in 2D array    
        self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
        self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
        print(self.destinationX, self.destinationY)
        
        # If there is a wall change direction
        while (self.environment.environment[ self.destinationY ][ self.destinationX ] == 1 ):
            #print("There is a wall to the", self.currentDirectionStr[self.direction])
            
            # Up and down movement for testing Q function
            '''if self.direction == 1:
                self.direction = 3
            else:
                self.direction = 1'''
            
            # Random movement
            self.direction = random.randrange(0, 4, 1)
                
            self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
            self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
            
        self.mapX = self.destinationX
        self.mapY = self.destinationY
     
    ############################################################################
    # Desc: This function is called from on_loop to move the ghost             #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def move(self):
        
        # Check if the Ghost has reached its movement goal
        if(abs(self.x - self.destinationX * 40) <= 0.25 and abs(self.y - self.destinationY * 40) <= 0.25):
            self.mapX = self.destinationX
            self.mapY = self.destinationY
            
            
            print("Ghost location:",self.mapX,self.mapY)
            # Check if Ghost ran over Pacman
            if(self.mapX == self.pacman.mapX and self.mapY == self.pacman.mapY):
                print("Ghost ran over Pacman!\nGame Over.")
                stopGame()
                    
            
            # Initialize a new random movement
            self.initializeMovement()
        
        # If he has not reached his goal, keep moving in the right direction
        else:
            if(self.direction == self.right):
                self.movRight()
            if(self.direction == self.down):
                self.movDown()
            if(self.direction == self.left):
                self.movLeft()
            if(self.direction == self.up):
                self.movUp()                

     

#***************************************************************#
# Environment Class                                                   #
# Holds information relating to where Pacman/Ghosts/PacDots are #
#***************************************************************#
class Environment:

    # Dimensions of 2D array
    width = 15
    height = 15
    
    # 2D array holding location of everything in the environment
    environment = [[]]
    
    # Current Pacdots
    currPacDots = 115
    
    # Environment Class Constructor
    def __init__(self):
        ''' Movement Test Environment
        self.environment =  [[1,1,1,1,1,1,1,1,1,1],
                            [1,2,2,2,2,2,2,2,2,1],
                            [1,2,2,2,2,2,2,2,2,1],
                            [1,2,2,1,2,2,1,2,2,1],
                            [1,2,2,1,2,2,1,2,2,1],
                            [1,2,2,1,2,2,1,2,2,1],
                            [1,2,2,1,2,2,1,2,2,1],
                            [1,2,2,2,2,2,2,2,2,1],
                            [1,2,2,2,2,2,2,2,2,1],
                            [1,1,1,1,1,1,1,1,1,1]]
        '''
        
        ''' Ghost Evasion Environment
        self.environment = [[1,1,1,1,1,1,1,1,1,1],
                           [1,0,0,0,0,0,0,0,0,1],
                           [1,0,0,0,0,0,0,0,0,1],
                           [1,0,0,0,0,0,0,0,2,1],
                           [1,0,0,0,0,0,0,0,0,1],
                           [1,0,0,0,0,0,0,0,0,1],
                           [1,1,1,1,1,1,1,1,1,1]]
        '''
        
        ''' Standard Pacman Environment '''
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], #12
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], #6
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], #10
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], #9
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], #10
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], #5
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], #12
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], #5
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], #10
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], #9
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], #10
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], #6
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], #12
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
                      
    ############################################################################
    # Desc: Draws background and walls                                         #
    # Inputs: Reference to self, something, something                          #
    # Outputs: None                                                            #
    ############################################################################
    def draw(self,display_surf, image_surf, image_dot):
        # Loop through the 2D array and place walls on the map where they should be.
        for y in range(self.height):
            for x in range(self.width):
                
                # If we need to draw a Wall
                if self.environment[y][x] == 1:
                    display_surf.blit(image_surf, (x * 40, y * 40))
                    
                 # If we need to draw a wall
                if self.environment[y][x] == 2:
                    display_surf.blit(image_dot, (x * 40, y * 40))
                    
                
                
            
 


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
    
    
    ###############################
    # RunPacman Class Constructor #
    ###############################
    def __init__(self):
        self.run = True
        self.display = None
        self.pacman_image = None
        self.ghost_image = None
        self.block_image = None
        self.dot_image = None
        
        # Environment (Environment) and Pacman
        self.environment = Environment()
        self.pacman = Pacman(self.environment)
        
        # Ghosts
        self.ghosts.append(Ghost(self.environment, self.pacman, 6, 6))
        self.ghosts.append(Ghost(self.environment, self.pacman, 6, 8))
        self.ghosts.append(Ghost(self.environment, self.pacman, 8, 8))
        self.ghosts.append(Ghost(self.environment, self.pacman, 8, 6))
       


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
        self.pacman_image = pygame.image.load("imgs\\player.png").convert()
        self.ghost_image = pygame.image.load("imgs\\ghost.png").convert()
        self.block_image = pygame.image.load("imgs\\block.png").convert()
        self.dot_image = pygame.image.load("imgs\\pacDot.png").convert()
        
        
    #############################################
    # Desc: Keeps each frame execution running  #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def on_loop(self):
        self.pacman.move()
        for ghost in self.ghosts:
            ghost.move()
            
            if self.pacman.mapX == ghost.mapX and self.pacman.mapY == ghost.mapY:
                endGame()
        

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
            
        self.display.blit(self.pacman_image, (self.pacman.x, self.pacman.y))
            
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
    def executeGame(self):
        if self.initGame() == False:
            self.run = False

        # Initialize Reinforcement Learning
        learner = Q()
        controller = ActionValueTable(70, 4)
        agent = LearningAgent(controller, learner)
            
        #########################################################################
        # This loop is called every frame. It is the main loop driving the game #
        #########################################################################
        while(self.run):
           
            ''' Player Controls for Pacman currently disabled        
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_RIGHT]):
                 self.pacman.movRight()
                 
            if (keys[pygame.K_LEFT]):
                self.pacman.movLeft()
                
            if (keys[pygame.K_UP]):
                self.pacman.movUp()
            
            if (keys[pygame.K_DOWN]):
                self.pacman.movDown()'''
                
            
            # Updates the window every frame showing new movements of the AI Agents 
            self.on_loop()
            self.render()
            
            # These are executed every frame to check if the user wants to quit the game 
            # Exits the Program if user clicks the x window button
            for even in pygame.event.get():
                if even.type == pygame.QUIT: 
                    self.stopGame()
            
            # Program will stop running once escape is pressed
            pygame.event.get()
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_ESCAPE]):
                self.run = False    
        
        
        # When the game finished running it calls the function to terminate the program
        self.stopGame()
        
        
        
###############################################################
# The main function that begins running our Pacman-In-AI game #
###############################################################
if __name__ == "__main__" :
    game = RunPacman()
    game.executeGame()
            
            
            
            
            
            
