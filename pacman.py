import pygame
import random



#########################
# --------------------- #
# Pacman Class          #
# Need Description Here #
# --------------------- #
#########################
class Pacman:
    x = 40
    y = 40
    speed = .1
    
    # Pac-man is AI, but for now I wanted to see how this sprite moved around the level
    def movRight(self):
        self.x = self.x + self.speed
        
    def movLeft(self):
        self.x = self.x - self.speed
        
    def movUp(self):
        self.y = self.y - self.speed
        
    def movDown(self):
        self.y = self.y + self.speed
      


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
        self.level = [1,1,1,1,1,1,1,1,1,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,1,1,1,1,1,1,1,1,1,]

    #draws the level into the window
    def draw(self,display_surf, image_surf):
        bx = 0
        by = 0
        for x in range(0,(self.width * self.height)):
            if self.level[bx + (by * self.width)] == 1:
                display_surf.blit(image_surf, (bx * 40, by * 40))
                
            bx = bx + 1
            if bx > self.width - 1:
                bx = 0
                by = by + 1
 


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
    
    # Minimum width of the window
    winWidth = 400
    
    # Minimum height of the window
    winHeight = 400
    
    # Pacman object
    pacman = None    
    
    
    ###############################
    # RunPacman Class Constructor #
    ###############################
    def __init__(self):
        self.run = True
        self.display = None
        self.pacman_image = None
        self.block_image = None
        self.pacman = Pacman()
        self.level = Level()
       


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
        self.pacman_image = pygame.image.load("imgs\player.png").convert()
        self.block_image = pygame.image.load("imgs\block.png").convert()
        
        
        
    #############################################
    # Desc: Keeps each frame execution running  #   
    # Inputs: Reference to self                 #
    # Outputs: None                             #
    #############################################
    def on_loop(self):
        pass

        

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
            
            
            
            
            
            