#****************************************************************#
# Environment Class                                              #
# Holds information relating to where Pacman/Ghosts/PacDots are. #
#****************************************************************#
class Environment:

    # Dimensions of 2D array
    width = 15
    height = 15
    
    # 2D array holding location of everything in the environment
    environment = [[]]
    
    # Current Pacdots
    currPacDots = 115
    
    # Used for getting Sensor()
    directionPacmanMoved = None
    
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
        
        ''' Small Standard Pacman Environment 
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1],
                            [1,2,2,2,2,2,1,2,2,2,2,2,1],
                            [1,2,1,1,1,2,1,2,2,2,2,2,1],
                            [1,2,1,2,2,2,2,2,2,2,2,2,1],
                            [1,2,2,2,1,2,1,2,1,2,2,2,1],
                            [1,2,1,1,1,2,2,2,1,1,1,2,1],
                            [1,2,2,2,2,2,1,2,2,2,2,2,1],
                            [1,2,1,1,1,2,1,2,2,2,2,2,1],
                            [1,2,2,2,2,2,2,2,2,2,2,2,1],
                            [1,1,1,1,1,1,1,1,1,1,1,1,1]]
        
        '''
        
        ''' Large Standard Pacman Environment ''' 
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
                            [1,0,2,2,2,2,2,1,2,2,2,2,2,2,1], 
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], 
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], 
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], 
                            [1,2,2,2,2,2,2,2,2,2,2,2,2,2,1], 
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
        
        
                      
    ############################################################################
    # Desc: Draws background and walls                                         #
    # Inputs: Reference to self, something, something                          #
    # Outputs: None                                                            #
    ############################################################################
    def draw(self,display_surf, image_surf, image_dot):
        
        # Loop through the 2D array and draw walls on the map where they should be.
        for y in range(self.height):
            for x in range(self.width):
                
                # If we need to draw a Wall
                if self.environment[y][x] == 1:
                    display_surf.blit(image_surf, (x * 40, y * 40))
                    
                 # If we need to draw a wall
                if self.environment[y][x] == 2:
                    display_surf.blit(image_dot, (x * 40, y * 40))
                    
                    
     
    ############################################################################
    # Desc: Returns the direction that the Pac-Man previously moved toward.    #
    # Inputs: None                                                             #
    # Outputs: Integer representing the direction Pac-Man previously moveed.   #
    ############################################################################
    def getSensors(self):
        return self.directionPacmanMoved
        
        
        
    ############################################################################
    # Desc: Resets the Environment after a game has been completed.            #
    # Inputs: None                                                             #
    # Outputs: None                                                            #
    ############################################################################   
    def resetMap(self):
        self.currPacDots = 115
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], 
                            [1,0,2,2,2,2,2,1,2,2,2,2,2,2,1], 
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], 
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], 
                            [1,1,1,2,1,1,2,2,2,1,1,2,1,1,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,2,2,2,2,2,2,1,1,2,1], 
                            [1,2,2,2,2,1,2,1,2,1,2,2,2,2,1], 
                            [1,2,1,1,2,1,2,1,2,1,2,1,1,2,1], 
                            [1,2,2,2,2,2,2,1,2,2,2,2,2,2,1], 
                            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
