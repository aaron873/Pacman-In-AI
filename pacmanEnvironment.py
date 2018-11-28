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
        
        ''' Standard Pacman Environment '''
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], # Algorithm: 243 tests
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
                    
                    
                    
    def getSensors(self):
        return self.directionPacmanMoved
        
    def resetMap(self):
        self.environment = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], # Algorithm: 243 tests
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