import pygame

pygame.init()

# Adam is very handsome.
# Adam is indeed very handsome.

# Window settings
WIDTH, HEIGHT = 800, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Haunted House")
pygame.display.set_icon(pygame.image.load("house.png"))

# Load & Scale Images
char_right = pygame.image.load("character.png")
char_left = pygame.image.load("characterR.png")
char_right = pygame.transform.scale(char_right, (50, 60))
char_left = pygame.transform.scale(char_left, (50, 60))
player_img = char_right  # Default facing right
heart = pygame.image.load("heart.png")
heart = pygame.transform.scale(heart, (40, 40))
house = pygame.image.load("house.png")
house = pygame.transform.scale(house, (250, 250))
tree = pygame.image.load("tree.png")
tree = pygame.transform.scale(tree, (100, 100))
bear = pygame.image.load("bear.png")
bear = pygame.transform.scale(bear, (100, 100))
dead_bear = pygame.image.load("dead.png")
dead_bear = pygame.transform.scale(dead_bear, (100, 100))

# Object Positions
heartX, heartY = 250, 260
bearX, bearY = 250, 310
dead_bearX, dead_bearY = 250, 300
treeX, treeY = 300, 300
houseX, houseY = 400, 150
playerX, playerY = 10, 340  # Player Position
playerWidth, playerHeight = 60, 60
playerVel = 5

# Define interaction zone (smaller & shifted)
hitbox_width, hitbox_height = 100, 100  # Half of house size
hitboxX, hitboxY = houseX + 80, houseY + 100  # Shifted 100 pixels right & down

# Font
font = pygame.font.Font(None, 36)

# Game Variables
running = True
show_choice = False  # Flag to show "Enter house?" message
bear_dioalog1 = False
choiceRun = False

# Clock for FPS control
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit FPS to 60

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    # Player Movement
    if keys[pygame.K_LEFT] and playerX - playerVel > 0:
        playerX -= playerVel
        player_img = char_left
    if keys[pygame.K_RIGHT] and playerX + playerVel < WIDTH - playerWidth:
        playerX += playerVel
        player_img = char_right

    # Check if player is inside interaction hitbox
    near_house = (hitboxX <= playerX <= hitboxX + hitbox_width) and (hitboxY <= playerY <= hitboxY + hitbox_height)

    # Press 'E' to interact
    if near_house and keys[pygame.K_e]:
        show_choice = True  # Activate choice prompt

    # Draw everything
    window.fill((128, 128, 128))  # Clear screen
    window.blit(house, (houseX, houseY))
    window.blit(tree, (treeX, treeY))
    window.blit(player_img, (playerX, playerY))

    # Show interaction message if near house
    if near_house:
        houseText = font.render("Press 'E' to enter", True, (0, 0, 0))
        window.blit(houseText, (200, 550))
        
    if show_choice:
        houseChoice_text = font.render("Do you want to go in? (Y/N)", True, (0, 0, 0))
        window.blit(houseChoice_text, (200, 500))

        # Handle choice
        if keys[pygame.K_y]:  # Enter house
            window.blit
            show_choice = False  # Hide prompt after choosing
        if keys[pygame.K_n]:  # Stay outside
            print("You decided not to enter.")
            show_choice = False  # Hide prompt

        if show_choice == True:
            window.fill((128, 128, 128))  # Clear screen
            window.blit(bear, (bearX, bearY))
            window.blit(player_img, (playerX, playerY))
            
            if playerX == bearX:
                bear_dioalog1 = True
            if bear_dioalog1:
                bear_choice_text = font.render("Kill(K)? Pet(P)? or RUN!?", True, (0, 0, 0))
                window.blit(bear_choice_text, (200, 500))
                if keys[pygame.K_k]:
                    bear = dead_bear
                if keys[pygame.K_p]:
                    if bear != dead_bear:
                        window.blit(heart, (heartX, heartY))
                if playerX == 10:
                    choiceRun = True
                if choiceRun:
                    window.fill((128, 128, 128))  # Clear screen
                    window.blit(player_img, (playerX, playerY))
                    
                if keys[pygame.K_r]:
                    pass





    pygame.display.update()

pygame.quit()
