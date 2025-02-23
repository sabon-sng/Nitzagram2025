import pygame
from helpers import screen
from constants import*


def main():
    # Set up the game display, clock and headline
    pygame.init()

    # Change the title of the window
    pygame.display.set_caption('Nitzagram')

    clock = pygame.time.Clock()

    # Set up background image
    background = pygame.image.load('Images/background.png')
    background = pygame.transform.scale(background,(WINDOW_WIDTH, WINDOW_HEIGHT))
    count = 0
    font = pygame.font.SysFont("ariel",25)
    # TODO: add a post here
    img1 = pygame.image.load('Images/noa_kirel.jpg')
    img1 = pygame.transform.scale(img1,(0.87 * WINDOW_WIDTH, 0.41 * WINDOW_HEIGHT))

    img2 = pygame.image.load('Images/ronaldo.jpg')
    img2 = pygame.transform.scale(img2,(0.87 * WINDOW_WIDTH, 0.41 * WINDOW_HEIGHT))

    image = [img1,img2]
    clicks = len(image)
    running = True
    while running:
        pos = pygame.mouse.get_pos()
        clicks = clicks % len(image)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running = False
            if pygame.mouse.get_pos()[0] >= LIKE_BUTTON_X_POS and pygame.mouse.get_pos()[0] <= (LIKE_BUTTON_X_POS + LIKE_BUTTON_WIDTH) and pygame.mouse.get_pos()[1] >= LIKE_BUTTON_Y_POS and pygame.mouse.get_pos()[1] <= (LIKE_BUTTON_Y_POS + LIKE_BUTTON_HEIGHT) and event.type == pygame.MOUSEBUTTONDOWN:
                count+= 1
            if event.type == pygame.MOUSEBUTTONDOWN and pos[0] > (POST_X_POS) and pos[0] < (POST_X_POS +POST_WIDTH) and pos[1] > (POST_Y_POS) and pos[1] < (POST_Y_POS +POST_HEIGHT):
                clicks += 1
                clicks = clicks % len(image)

        # Grabs events such as key pressed, mouse pressed and so.
        # Going through all the events that happened in the last clock tick

        # Display the background, presented Image, likes, comments, tags and location(on the Image)
        screen.fill(BLACK)
        screen.blit(background, (0, 0))

        # Update display - without input update everything
        screen.blit(image[clicks], (0.064 * WINDOW_WIDTH, 0.2 * WINDOW_HEIGHT))
        like_text = font.render(f"you are liked by {count} people",True,(0,0,0))
        screen.blit(like_text,(LIKE_TEXT_X_POS,LIKE_TEXT_Y_POS))
        pygame.display.flip()

        # Set the clock tick to be 60 times per second. 60 frames for second.
        clock.tick(60)

    pygame.quit()
    quit()


main()
