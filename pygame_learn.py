import pygame

pygame.init()

scr_width , scr_height= 400 ,500


screen = pygame.display.set_mode((scr_width,scr_height)) #setting window

#making a rectangular object(pos_x,pos_y,width,height)
player = pygame.Rect((300,250,50,50))
# Game loop
running = True
while running:
    screen.fill((0,0,0)) #black

    pygame.draw.rect(screen,(255,0,0),player)#activating object on screen

    key = pygame.key.get_pressed() #keyboard key
    if key[pygame.K_q]==True:
        player.move_ip(-1,0)
    elif key[pygame.K_d]==True:
        player.move_ip(1,0)    
    elif key[pygame.K_w]==True:
        player.move_ip(0,-1) 
    elif key[pygame.K_s]==True:
        player.move_ip(0,1)

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #if cross button is pressed
            running = False

    pygame.display.update() #mandatory,makes changes visible to the screen 
pygame.quit()