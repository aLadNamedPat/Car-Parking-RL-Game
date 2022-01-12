import pygame
import math


class ParkedCar:
    def __init__(self, POS, img):
        self.x, self.y = POS
        self.image = img
        parkedCar = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(parkedCar)

    def get_mask(self):
        parkedCar = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(parkedCar)
        return pygame.mask.from_surface(parkedCar, threshold=0)

    def collide(self, driverCar):
        movingCarMask = driverCar.get_mask()
        parkedCarMask = self.get_mask()

        offset = (self.x - driverCar.x, self.y - driverCar.y)

        overlap = movingCarMask.overlap(parkedCarMask, offset)

        if overlap:
            return True

        return False

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
