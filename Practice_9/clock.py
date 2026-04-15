import pygame

pygame.init()


def get_images():
    clock_img = pygame.image.load(r"/Users/atleeast/Documents/GitHub/ProgrammingPrinciples2/Practice_9/images/chasy.jpg").convert()
    left_hnd = pygame.image.load(r"/Users/atleeast/Documents/GitHub/ProgrammingPrinciples2/Practice_9/images/Mickey_hand.png").convert_alpha()
    right_hnd = pygame.image.load(r"/Users/atleeast/Documents/GitHub/ProgrammingPrinciples2/Practice_9/images/Mickey_sec.png").convert_alpha()
    
    return clock_img, left_hnd, right_hnd