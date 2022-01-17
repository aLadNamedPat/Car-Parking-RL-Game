import pygame
import math


class Border:
    def __init__(self, POS, img, dimensions):
        self.x, self.y = POS
        self.image = img
        self.length, self.width = dimensions

    def get_mask(self):
        border = self.image.convert_alpha()
        return pygame.mask.from_surface(border)

    def collide(self, driverCar):
        movingCarMask = driverCar.get_mask()
        parkedCarMask = self.get_mask()

        offset = (int(self.x - driverCar.x_pos), int(self.y - driverCar.y_pos))

        overlap = movingCarMask.overlap(parkedCarMask, offset)

        if overlap:
            return True

        return False

    def get_corners(self):
        top_left = (self.x, self.y)
        top_right = (self.x + self.length, self.y)
        bottom_left = (self.x, self.y + self.width)
        bottom_right = (self.x + self.length, self.y + self.width)

        return top_left, top_right, bottom_left, bottom_right

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))
