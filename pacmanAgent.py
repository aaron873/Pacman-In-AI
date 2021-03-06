from random import randrange
from math import sqrt

#**********************************************************************************#
# Pacman Agent Class                                                               #
# This is the Pacman Agent class, representing the Pac-Man Agent that implements   #
# one of three movement algorithms to traverse the environment collecting Pac-Dots #
#**********************************************************************************#

class PacmanAgent:
    
    ###########################
    # Pacman Member Variables #
    ###########################
    
    # Pacman's current location in reference to the graphical window
    x = 40
    y = 40
    
    # Pacman's current location in reference to the 2D array in Location
    mapX = 1
    mapY = 1
    
    #Coordinates for the closest Pac-dot to Pac-Man
    closestPacDotX = 0
    closestPacDotY = 0
    hitDot = False
    endMovement = False
    
    # Referencing which direction to go
    right = 0
    down = 1
    left = 2
    up = 3
    
    # Used for GetSensors() Function
    actions = [[0.0], [1.0], [2.0], [3.0]]
    
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
    speed = 0.1
    
    # Reference to the Environment class to give our Pacman Agent vision of the Environment
    environment = None
    
  
    ###########################
    # Pacman Member Functions #
    ###########################
    
    
    # Pacman Class Constructor
    def __init__(self, input_environment):
        self.environment = input_environment  
        
        
        
    #################################################
    # Randomly Spawning Pacman on the board         #
    # This function is currently not used since     # 
    # we spawn Pacman in the same location each time#
    #################################################
    def randomSpawn(self):
        
        spawnLocations = [[1,1],[1,13],[13,1],[13,13]]
        
        randomIdx = randrange(0, 4, 1)
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
        
        
    '''    
    ####################################################################################################
    # Desc: This is a function to get a new randomized or breadth-first search movement direction.     #
    #       Currently not used since the program is implementing Q-Learning.                           # 
    # Inputs: Reference to self                                                                        #
    # Outputs: None                                                                                    #
    ####################################################################################################   
    def initializeMovement(self):
        
        
        ##############################################
        # Breadth-First Searching Algorithm Movement #
        ##############################################
        
        pacDotDistance = 100
        
        # Loop through all indexes in 2D environment array
        for loopY in range(self.environment.height):
            for loopX in range(self.environment.width):
                
                # If there is a pacDot at this index, check to see if its distance is 
                # closer than the previous minDistance
                if self.environment.environment[loopY][loopX] == 2:
                    tempDistance = sqrt( ((self.mapX - loopX) ** 2) + ((self.mapY - loopY) ** 2) )  
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
            self.direction = randrange(0, 4, 1)    
            self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
            self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
            
        #self.mapX = self.destinationX
        #self.mapY = self.destinationY    
        
        
        ''
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
            
        # Debug print statement    ''
        print("Moving", self.currentDirectionStr[self.direction])        
        '''

     
    ############################################################################
    # Desc: This function is called from on_loop to move pacman                #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def move(self, currDirection):
        
        self.direction = currDirection
        self.destinationX = self.effectOnXMovement[currDirection] + self.mapX
        self.destinationY = self.effectOnYMovement[currDirection] + self.mapY
        
        # Check if Pacman has reached its movement goal
        if(abs(self.x - self.destinationX * 40) <= 0.3 and abs(self.y - self.destinationY * 40) <= 0.3):
            self.mapX = self.destinationX
            self.mapY = self.destinationY
            
            # Check if Pacman ran over a PacDot
            if(self.environment.environment[self.mapY][self.mapX] == 2):
                self.environment.currPacDots -= 1
                self.environment.environment[self.destinationY][self.destinationX] = 0
            
                self.hitDot = True
                self.environment.directionPacmanMoved = self.actions[self.direction]
             
            self.endMovement = True
            
            # If there are no more remaining Pac-Dots
            if(self.environment.currPacDots == 0):
                print("Pac-man collected all the Pac-Dots!!!")
                    
        
        # If he has not reached his goal, keep moving in the right direction
        else:
            if(currDirection == self.right):
                self.movRight()
            if(currDirection == self.down):
                self.movDown()
            if(currDirection == self.left):
                self.movLeft()
            if(currDirection == self.up):
                self.movUp()
