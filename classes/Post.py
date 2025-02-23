import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,description,location,likes_counter,comments): #TODO: add parameters
        def get_username():
            self.username = username
            return self.username

        def get_description():
            self.description = description
            return self.description
        def get_location():
            self.location = location
            return self.location
        def get_likes_counter():
            self.likes_counter = likes_counter
            return self.likes_counter
        def get_comments():
            self.comments = comments
            return self.comments

        def display():
            img1 = pygame.image.load('Images/ronaldo.jpg')
            POST_WIDTH = 0.87 * WINDOW_WIDTH
            POST_HEIGHT = 0.41 * WINDOW_HEIGHT
            img1 = pygame.transform.scale(img1, (0.87 * WINDOW_WIDTH, 0.41 * WINDOW_HEIGHT))
            screen.blit(img1, (0.87 * WINDOW_WIDTH, 0.41 * WINDOW_HEIGHT))











        #TODO: write me!
        pass

    def display(self):
        img1 = pygame.image.load('Images/ronaldo.jpg')
        img1 = pygame.transform.scale(img1, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))
        screen.blit(img1, (WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        return None
        # TODO: write me!
        pass


    def display_comments(self):
        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



