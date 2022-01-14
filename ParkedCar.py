import pygame
import math


class ParkedCar:
    def __init__(self, POS, img):
        self.x, self.y = POS
        self.image = img
        parkedCar = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(parkedCar)
        # FIX
        # new_rect = rotated_image.get_rect(
        #    center=self.image.get_rect(topleft=(self.x, self.y)).center)
        # self.rect = self.image.get_rect(topleft=(self.x, self.y)).center)

    def get_mask(self):
        parkedCar = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(parkedCar)
        return pygame.mask.from_surface(parkedCar, threshold=0)

    def collide(self, driverCar):
        movingCarMask = driverCar.get_mask()
        parkedCarMask = self.get_mask()

        offset = (int(self.x - driverCar.x_pos), int(self.y - driverCar.y_pos))

        overlap = movingCarMask.overlap(parkedCarMask, offset)

        if overlap:
            return overlap

        return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
