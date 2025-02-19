import pygame

# Initialize Pygame
pygame.init()

# Set screen dimensions
screenWIDTH, screenHEIGHT = 800, 600
screen = pygame.display.set_mode((screenWIDTH, screenHEIGHT))
pygame.display.set_caption("Mystery House")

# Images
stairsUP = pygame.image.load("stairsUP.png")
stairsUP = pygame.transform.scale(stairsUP, (screenWIDTH, screenHEIGHT))

monster_loved = pygame.image.load("monsterLOVED.png")  # New image when monster is petted
monster_loved = pygame.transform.scale(monster_loved, (250, 300))

monster_killed = pygame.image.load("monsterDEATH.png")  # New image when monster is killed
monster_killed = pygame.transform.scale(monster_killed, (250, 325))

monster = pygame.image.load("monster.png")
monster = pygame.transform.scale(monster, (250, 300))

room1 = pygame.image.load("room1.png")
room1 = pygame.transform.scale(room1, (screenWIDTH, screenHEIGHT))

background = pygame.image.load("forest.png")
background = pygame.transform.scale(background, (screenWIDTH, screenHEIGHT))

house = pygame.image.load("house.png")
house = pygame.transform.scale(house, (200, 200))

playerR = pygame.image.load("victorR.png")
playerL = pygame.image.load("victorL.png")

dining = pygame.image.load("dinning.png")
dining = pygame.transform.scale(dining, (screenWIDTH, screenHEIGHT))

# Variables
playerX, playerY = 5, 340
playerW, playerH = 100, 100  # Default size outside
playerVel = 5
houseX, houseY = 500, 220  # House position
monsterX, monsterY = 300, 300
houseRect = pygame.Rect(houseX, houseY, 200, 200)  # House hitbox
playerRect = pygame.Rect(playerX, playerY, playerW, playerH)  # Player hitbox

# Game state
insideHouse = False
insideRoom1 = False
insideStairs = False  # New state for stairsUP
player_img = pygame.transform.scale(playerR, (playerW, playerH))  # Default image size
monster_status = "neutral"  # Default monster status (neutral, love, killed)
password_input = ""  # To store player's password input
password_correct = False  # To check if the entered password is correct
entered_room = False  # To track if the player can enter the room after unlocking

running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detect key press
            if insideHouse:
                if event.key == pygame.K_1 and not insideStairs:  # You can only go to Room 1 if you're not in Stairs
                    insideRoom1 = True
                    insideStairs = False
                    print("Moved to Room 1")
                elif event.key == pygame.K_2 and not insideRoom1:  # You can only go to Stairs if you're not in Room 1
                    insideStairs = True
                    insideRoom1 = False
                    print("Moved to Stairs")
                elif event.key == pygame.K_b:
                    insideRoom1 = False
                    insideStairs = False
                    print("Back to Dining Room")
                elif event.key == pygame.K_p and monster_status == "neutral" and insideRoom1:
                    monster_status = "love"
                    print("You pet the monster lovingly!")
                elif event.key == pygame.K_k and monster_status == "neutral" and insideRoom1:
                    monster_status = "killed"
                    print("You killed the monster!")
                elif event.key == pygame.K_e and insideStairs and password_correct:  # Entering the room after correct password
                    entered_room = True
                    print("You have entered the room!")

                # Password input
                if insideStairs and not password_correct:
                    if event.key == pygame.K_BACKSPACE:  # Remove last character
                        password_input = password_input[:-1]
                    elif event.key == pygame.K_RETURN:  # Check if password is correct
                        if password_input == "1945":
                            password_correct = True
                            print("Correct password! You can proceed.")
                        else:
                            print("Incorrect password. Try again.")
                    elif event.key in [pygame.K_0, pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_5, pygame.K_6, pygame.K_7, pygame.K_8, pygame.K_9]:  # Only allow number inputs
                        password_input += event.unicode  # Add typed number to password

    keys = pygame.key.get_pressed()

    # Player movement
    if keys[pygame.K_a] and playerX > 0:
        playerX -= playerVel
        player_img = pygame.transform.scale(playerL, (playerW, playerH))  # Flip left
    if keys[pygame.K_d] and playerX + playerW < screenWIDTH:
        playerX += playerVel
        player_img = pygame.transform.scale(playerR, (playerW, playerH))  # Flip right

    # Update player rectangle position
    playerRect.topleft = (playerX, playerY)

    # Render game
    if insideHouse:
        if insideRoom1:
            screen.blit(room1, (0, 0))
            if monster_status == "love":
                screen.blit(monster_loved, (monsterX, monsterY))
            elif monster_status == "killed":
                screen.blit(monster_killed, (monsterX, monsterY))
            else:
                screen.blit(monster, (monsterX, monsterY))
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Press 'P' to pet monster", True, (255, 255, 255)), (50, screenHEIGHT - 150))
            screen.blit(font.render("Press 'K' to kill monster", True, (255, 255, 255)), (50, screenHEIGHT - 100))
            screen.blit(font.render("Press 'B' to go back", True, (255, 255, 255)), (50, screenHEIGHT - 50))
        elif insideStairs:
            screen.blit(stairsUP, (0, 0))
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Enter the password to proceed", True, (255, 255, 255)), (50, screenHEIGHT - 50))
            if password_correct:
                screen.blit(font.render("Correct password! Press 'E' to enter the room.", True, (0, 255, 0)), (50, screenHEIGHT - 150))
            else:
                screen.blit(font.render(f"Password: {password_input}", True, (255, 255, 255)), (50, screenHEIGHT - 100))
        else:
            screen.blit(dining, (0, 0))
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Press '1' for Room 1", True, (255, 255, 255)), (50, screenHEIGHT - 100))
            screen.blit(font.render("Press '2' for Stairs", True, (255, 255, 255)), (50, screenHEIGHT - 50))
        screen.blit(player_img, (playerX, playerY))
    else:
        screen.blit(background, (0, 0))
        screen.blit(house, (houseX, houseY))
        screen.blit(player_img, (playerX, playerY))
        font = pygame.font.Font(None, 36)
        screen.blit(font.render("Use 'A' and 'D' to move left and right", True, (255, 255, 255)), (50, screenHEIGHT - 50))
        if playerRect.colliderect(houseRect):
            screen.blit(font.render("Press 'E' to Enter", True, (255, 255, 255)), (houseX, houseY - 30))
            if keys[pygame.K_e]:
                insideHouse = True
                playerW, playerH = 300, 300
                playerX, playerY = 400, 300
                player_img = pygame.transform.scale(playerR, (playerW, playerH))
                print("Entered the house!")
    
    pygame.display.flip()

pygame.quit()
