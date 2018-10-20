import pygame
import random



#########################
# --------------------- #
# Pacman Class          #
# Need Description Here #
# --------------------- #
#########################
class Pacman:
    
    ###########################
    # Pacman Member Variables #
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
    
    # Direction's effect on movement. Example: if pacman is moving right, idx 0, his y change is 0 and x change is +1.  
    effectOnXMovement = [1, 0, -1, 0]
    effectOnYMovement = [0, 1, 0, -1]
    
    # Current movement direction and destination. Used when AI moves each frame
    direction = 0
    destinationX = 0
    destinationY = 0
    currentDirectionStr = ["Right", "Down", "Left", "Up"]
    
    # Pacman's speed
    speed = 0.05
    
    # Reference to the Level class to give our Pacman Agent vision of the Environment
    level = None
    
    def __init__(self, input_level):
        self.level = input_level
        self.initializeMovement()
    
    # Pac-man is AI, but for now I wanted to see how this sprite moved around the level
    def movRight(self):
        self.x = self.x + self.speed
        
    def movLeft(self):
        self.x = self.x - self.speed
        
    def movUp(self):
        self.y = self.y - self.speed
        
    def movDown(self):
        self.y = self.y + self.speed
        
        
        
    ############################################################################
    # Desc: This is a function to get a new randomized movement direction      #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def initializeMovement(self):
        
        # Choose a random direction to move in, Right = 0, Down = 1, Left = 2, Up = 3
        self.direction = random.randrange(0, 4, 1)  

        # Store it in a variable so that the move() function called every frame can move in the correct direction
        self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
        self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
        
        # Keep looping until a direction without a wall is given
        while (self.level.level[ self.destinationY ][ self.destinationX ] == 1 ):
            print("There is a wall to the", self.currentDirectionStr[self.direction])
            
            # Read comments above for description
            self.direction = random.randrange(0, 4, 1)    
            self.destinationX = self.effectOnXMovement[self.direction] + self.mapX
            self.destinationY = self.effectOnYMovement[self.direction] + self.mapY
            
        # Debug print statement    
        print("Moving", self.currentDirectionStr[self.direction])        
     

     
    ############################################################################
    # Desc: This function is called from on_loop to move pacman                #
    # Inputs: Reference to self                                                #
    # Outputs: None                                                            #
    ############################################################################   
    def move(self):
        
        # Check if Pacman has reached its movement goal
        if(abs(self.x - self.destinationX * 40) <= 0.25 and abs(self.y - self.destinationY * 40) <= 0.25):
            self.initializeMovement()
            self.mapX = self.destinationX
            self.mapY = self.destinationY
        
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
     

     
#################################################################
# ------------------------------------------------------------- #
# Level Class                                                   #
# Holds information relating to where Pacman/Ghosts/PacDots are #
# ------------------------------------------------------------- #
#################################################################
class Level:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.level =  [[1,1,1,1,1,1,1,1,1,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,1,0,0,1,0,0,1],
                       [1,0,0,1,0,0,1,0,0,1],
                       [1,0,0,1,0,0,1,0,0,1],
                       [1,0,0,1,0,0,1,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,0,0,0,0,0,0,0,0,1],
                       [1,1,1,1,1,1,1,1,1,1]]

    #draws the level into the window
    def draw(self,display_surf, image_surf):
        for y in range(self.height):
            for x in range(self.width):
                if self.level[y][x] == 1:
                    display_surf.blit(image_surf, (x * 40, y * 40))
                
            
 


##################################################
# ---------------------------------------------- #
# RunPacman Class                                #
# Handles the execution of the Pacman In AI Game #
# ---------------------------------------------- #
##################################################
class RunPacman:
    
    
    ##############################
    # RunPacman Member Variables #
    ##############################
    
    # Minimum width and height of the window
    winWidth = 400
    winHeight = 400
    
    # Pacman object
    pacman = None   

    # Reference to the Level
    level = None
    
    
    ###############################
    # RunPacman Class Constructor #
    ###############################
    def __init__(self):
        self.run = True
        self.display = None
        self.pacman_image = None
        self.block_image = None
        self.level = Level()
        self.pacman = Pacman(self.level)
       


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
        self.block_image = pygame.image.load("imgs\\block.png").convert()
        
        
        
    #############################################
    # Desc: Keeps each frame execution running  #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def on_loop(self):
        self.pacman.move()

        

    #############################################
    # Desc: Updates the Progam graphical window #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def render(self):
        self.display.fill((0,0,0))
        self.display.blit(self.pacman_image, (self.pacman.x, self.pacman.y))
        self.level.draw(self.display, self.block_image)
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
         
        #########################################################################
        # This loop is called every frame. It is the main loop driving the game #
        #########################################################################
        while(self.run):
           
            ''' Player Controls for Pacman currently disabled        
            #moves depending on what keys are pressed. Collision does not work (again we won't use this later on)
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
            
            
            ##############################################################################
            # These are executed every frame to check if the user wants to quit the game #
            ##############################################################################
            
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
            
            
            
            
            
            