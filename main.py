import pygame
import time

# Initialize Pygame
pygame.init()

# Set screen dimensions
screenWIDTH, screenHEIGHT = 800, 600
screen = pygame.display.set_mode((screenWIDTH, screenHEIGHT))
icon = pygame.image.load("Things/gift_from_monster.png")
pygame.display.set_icon(icon)
pygame.display.set_caption("Mystery House")

# Images
baby_monster_happy = pygame.image.load("Charachters/BabyMNETHappy.png")
baby_monster_happy = pygame.transform.scale(baby_monster_happy, (150, 250))

baby_monster_sad = pygame.image.load("Charachters/babyMNET.png")
baby_monster_sad = pygame.transform.scale(baby_monster_sad, (150, 250))

room2 = pygame.image.load("Locations/room2.png")
room2 = pygame.transform.scale(room2, (screenWIDTH, screenHEIGHT))

monster_loved = pygame.image.load("Charachters/monsterLOVED.png")  # New image when monster is petted
monster_loved = pygame.transform.scale(monster_loved, (250, 300))

monster_killed = pygame.image.load("Charachters/monsterDEATH.png")  # New image when monster is killed
monster_killed = pygame.transform.scale(monster_killed, (250, 325))

monster = pygame.image.load("Charachters/monster.png")
monster = pygame.transform.scale(monster, (250, 300))

room1 = pygame.image.load("locations/room1.png")
room1 = pygame.transform.scale(room1, (screenWIDTH, screenHEIGHT))

background = pygame.image.load("locations/forest.png")
background = pygame.transform.scale(background, (screenWIDTH, screenHEIGHT))

house = pygame.image.load("Things/house.png")
house = pygame.transform.scale(house, (200, 200))

playerR = pygame.image.load("Charachters/victorR.png")
playerL = pygame.image.load("Charachters/victorL.png")

dining = pygame.image.load("locations/dinning.png")
dining = pygame.transform.scale(dining, (screenWIDTH, screenHEIGHT))

letter_son = pygame.image.load("Things/letter_son.png")
letter_son = pygame.transform.scale(letter_son, (screenWIDTH, screenHEIGHT))

gift_from_monster = pygame.image.load("Things/gift_from_monster.png")
gift_from_monster = pygame.transform.scale(gift_from_monster, (screenWIDTH, screenHEIGHT))

the_endscene = pygame.image.load("locations/the_end.png")
the_endscene = pygame.transform.scale(the_endscene, (screenWIDTH, screenHEIGHT))

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
insideRoom2 = False  # New state for room2
upsideRoom2 = False
player_img = pygame.transform.scale(playerR, (playerW, playerH))  # Default image size
monster_status = "neutral"  # Default monster status (neutral, love, killed)
password_input = ""  # To store player's password input
password_correct = False
victor_gifted = False
victor_regret = False
nothing_happend = False
the_end = False
end_time = 0  # Time when the end screen should be displayed
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # Limit the frame rate to 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:  # Detect key press
            if insideHouse:
                if event.key == pygame.K_1 and not insideRoom2:  # You can only go to Room 1 if you're not in Room 2
                    insideRoom1 = True
                    insideRoom2 = False
                    print("Moved to Room 1")
                elif event.key == pygame.K_2 and not insideRoom1:  # You can only go to Room 2 if you're not in Room 1
                    insideRoom2 = True
                    insideRoom1 = False
                    print("Moved to Room 2")
                elif event.key == pygame.K_b:
                    insideRoom1 = False
                    insideRoom2 = False
                    print("Back to Dining Room")
                elif event.key == pygame.K_p and monster_status == "neutral" and insideRoom1:
                    monster_status = "love"
                    print("You pet the monster lovingly!")
                elif event.key == pygame.K_k and monster_status == "neutral" and insideRoom1:
                    monster_status = "killed"
                    print("You killed the monster!")
                elif event.key == pygame.K_e and insideRoom2 and password_correct:  # Entering the room after correct password
                    upsideRoom2 = True
                    print("upside world, face you qunsequences")


                # Password input
                if insideRoom2 and not password_correct:
                    if event.key == pygame.K_BACKSPACE:  # Remove last character
                        password_input = password_input[:-1]
                    elif event.key == pygame.K_RETURN:  # Check if password is correct
                        if password_input == "1945":
                            password_correct = True
                            print("Correct password! You can proceed.")
                        else:
                            print("Incorrect password. Try again.")
                    elif event.unicode and event.unicode.isalnum():
                        password_input += event.unicode  # Add typed character to password
                elif password_correct:
                    room2 = pygame.image.load("locations/room2BLACK.png")
                    room2 = pygame.transform.scale(room2, (screenWIDTH, screenHEIGHT))

                    room1 = pygame.image.load("locations/room1BLACK.png")
                    room1 = pygame.transform.scale(room1, (screenWIDTH, screenHEIGHT))

                    playerR = pygame.image.load("Charachters/victorR.png")
                    playerL = pygame.image.load("Charachters/victorL.png")

                    dining = pygame.image.load("locations/dinningBLACK.png")
                    dining = pygame.transform.scale(dining, (screenWIDTH, screenHEIGHT))

                    if victor_gifted:
                        playerR = pygame.image.load("Charachters/victor_giftedR.png")
                        playerL = pygame.image.load("Charachters/victor_giftedL.png")

                    if monster_status == "killed":
                        monster_killed = pygame.image.load("Charachters/monsterGRAVE.png")  # New image when monster is killed
                        monster_killed = pygame.transform.scale(monster_killed, (250, 325))
                    elif monster_status == "love":
                        monster_loved = pygame.image.load("Charachters/monsterGIFT.png")  # New image when monster is petted
                        monster_loved = pygame.transform.scale(monster_loved, (250, 300))
                    keys = pygame.key.get_pressed()
                    if victor_gifted or victor_regret or nothing_happend:
                        if keys[pygame.K_b] and (victor_gifted or victor_regret or nothing_happend):
                            the_end = True


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
        if insideRoom1 and password_correct:
            screen.blit(room1, (0, 0))
            if monster_status == "love":
                screen.blit(monster_loved, (monsterX, monsterY))
                screen.blit(baby_monster_happy, (250, 350))
                screen.blit(font.render("Press E to open the gift.", True, (255, 255, 255)), (50, screenHEIGHT - 50))
                if keys[pygame.K_e]:
                    gift_from_monster.set_colorkey((255, 255, 255))
                    screen.blit(gift_from_monster, (0, 0))
                    victor_gifted = True

            elif monster_status == "killed":
                screen.blit(monster_killed, (monsterX, monsterY))
                screen.blit(baby_monster_sad, (225, 350))
                screen.blit(font.render("Press E to open the letter.", True, (255, 255, 255)), (50, screenHEIGHT - 50))
                if keys[pygame.K_e]:
                    letter_son.set_colorkey((255, 255, 255))
                    screen.blit(letter_son, (0, 0))
                    victor_regret = True

            else:
                screen.blit(monster, (monsterX, monsterY))
                nothing_happend = True
            font = pygame.font.Font(None, 36)

        elif insideRoom1 and not password_correct:
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
        elif insideRoom2:
            screen.blit(room2, (0, 0))
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Enter the password to proceed", True, (255, 255, 255)), (50, screenHEIGHT - 50))
            if password_correct:
                screen.blit(font.render("Correct password! Press 'E' to enter the portal.", True, (0, 255, 0)), (50, screenHEIGHT - 150))
                upsideRoom2 = True
            else:
                screen.blit(font.render(f"Password: {password_input}", True, (255, 255, 255)), (50, screenHEIGHT - 100))
        else:
            screen.blit(dining, (0, 0))
            font = pygame.font.Font(None, 36)
            screen.blit(font.render("Press '1' for Room 1", True, (255, 255, 255)), (50, screenHEIGHT - 100))
            screen.blit(font.render("Press '2' for Room 2", True, (255, 255, 255)), (50, screenHEIGHT - 50))
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
                playerW, playerH = 300, 300  # Increase player size when inside the house
                playerX, playerY = 300, 300
                player_img = pygame.transform.scale(playerR, (playerW, playerH))
                print("Entered the house!")

    # Check if it's time to show the end screen
    if the_end:
        print("The end")
        screen.blit(the_endscene, (0, 0))
        if keys[pygame.K_q]:
            running = False

        
  

    pygame.display.flip()

pygame.quit()