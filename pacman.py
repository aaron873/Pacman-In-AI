import pygame

class Pacman:
    x = 44
    y = 44
    speed = .25
    
    # Pac-man is AI, but for now I wanted to see how this sprite moved around the level
    def movRight(self):
        self.x = self.x + self.speed
        
    def movLeft(self):
        self.x = self.x - self.speed
        
    def movUp(self):
        self.y = self.y - self.speed
        
    def movDown(self):
        self.y = self.y + self.speed
        
class Level:
    def __init__(self):
        self.width = 10
        self.height = 10
        self.level = [1,1,1,1,1,1,1,1,1,1,
                      1,0,0,0,0,0,0,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
                      1,0,0,1,0,0,1,0,0,1,
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
                
class RunPacman:
    
    winWidth = 500
    winHeight = 400
    pacman = 0    
    
    def __init__(self):
        self.run = True
        self.display = None
        self.pacman_image = None
        self.block_image = None
        self.pacman = Pacman()
        self.level = Level()
        
    def initGame(self):
        pygame.init()
        self.display = pygame.display.set_mode((self.winWidth, self.winHeight), pygame.HWSURFACE)
        pygame.display.set_caption("Pac-man AI")
        self.run = True
        self.pacman_image = pygame.image.load("player.png").convert()
        self.block_image = pygame.image.load("block.png").convert()
        
    #I don't know what this does but we need it
    def on_loop(self):
        pass
    
    #updates the window as pacman moves
    def render(self):
        self.display.fill((0,0,0))
        self.display.blit(self.pacman_image, (self.pacman.x, self.pacman.y))
        self.level.draw(self.display, self.block_image)
        pygame.display.flip()
        
    #stops the program
    def stopGame(self):
        pygame.quit()
        
    def executeGame(self):
        if self.initGame() == False:
            self.run = False
            
        #keeps going while the program itself is still running
        while(self.run):
            
            #takes in keyboard input (later on we won't use this)
            for even in pygame.event.get():
                if even.type == pygame.QUIT: #program exits when the 'x' is clicked on
                    self.stopGame()
                    
            #moves depending on what keys are pressed. Collision does not work (again we won't use this later on)
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_RIGHT]):
                 self.pacman.movRight()
                 
            if (keys[pygame.K_LEFT]):
                self.pacman.movLeft()
                
            if (keys[pygame.K_UP]):
                self.pacman.movUp()
            
            if (keys[pygame.K_DOWN]):
                self.pacman.movDown()
                
            #program willstop running once escape is pressed
            if (keys[pygame.K_ESCAPE]):
                self.run = False
                
            #updates the window
            self.on_loop()
            self.render()
            
        self.stopGame()
        
if __name__ == "__main__" :
    game = RunPacman()
    game.executeGame()
            
            
            
            
            
            