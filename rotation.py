import pygame


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    win.blit(rotated_image, top_left)
