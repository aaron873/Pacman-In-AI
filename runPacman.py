from pacmanAgent import PacmanAgent
from ghost import Ghost
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
    
    
    ###############################
    # RunPacman Class Constructor #
    ###############################
    def __init__(self, environment):
        self.run = True
        self.display = None
        self.pacman_image = None
        self.ghost_image = None
        self.block_image = None
        self.dot_image = None
        
        # Environment (Environment) and Pacman
        self.environment = environment
        self.pacman = PacmanAgent(self.environment)
        
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
                self.run = False
        

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
            
            # CHeck if all dots have been collected
            if(self.environment.currPacDots == 0):
                print("Pac-man collected all the Pac-Dots!!!")
                self.run = False
                #stopGame()
            
            # Program will stop running once escape is pressed
            pygame.event.get()
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_ESCAPE]):
                self.run = False    
        
        
        # When the game finished running it calls the function to terminate the program
        self.stopGame()