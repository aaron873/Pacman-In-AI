from random import randrange

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
    direction = randrange(0, 4, 1)
    destinationX = 0
    destinationY = 0
    currentDirectionStr = ["Right", "Down", "Left", "Up"]
    
    # Ghosts's speed
    speed = 0.05
    
    # Reference to the Environment class and Pacman to give our Ghost vision of the Environment
    environment = None
    pacman = None
    
  
    ###########################
    # Ghost  Member Functions #
    ###########################
    
    
    # Pacman Class Constructor
    def __init__(self, input_environment, input_pacman, starting_mapX, starting_mapY):
        self.environment = input_environment  
        self.pacman = input_pacman
        
        self.mapX = starting_mapX
        self.x = self.mapX * 40
        
        self.mapY = starting_mapY
        self.y = self.mapY * 40
        
        self.direction = randrange(0, 4, 1)
        
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
        #print(self.destinationX, self.destinationY)
        
        # If there is a wall change direction
        while (self.environment.environment[ self.destinationY ][ self.destinationX ] == 1 ):
            #print("There is a wall to the", self.currentDirectionStr[self.direction])
            
            # Up and down movement for testing Q function
            '''if self.direction == 1:
                self.direction = 3
            else:
                self.direction = 1'''
            
            # Random movement
            self.direction = randrange(0, 4, 1)
                
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
            
            
            #print("Ghost location:",self.mapX,self.mapY)
            # Check if Ghost ran over Pacman
            #if(self.mapX == self.pacman.mapX and self.mapY == self.pacman.mapY):
                #print("Ghost ran over Pacman!\nGame Over.")
                #stopGame()
                    
            
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
