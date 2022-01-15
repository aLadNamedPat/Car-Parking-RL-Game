import pygame


def blit_rotate_center(win, image, top_left, angle):
    rotated_image = pygame.transform.rotate(image, angle)
<<<<<<< HEAD
    new_rect = rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    win.blit(rotated_image, new_rect.topleft)
=======
    win.blit(rotated_image, top_left)
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180
