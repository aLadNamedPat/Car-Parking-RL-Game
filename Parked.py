import pygame
import math


class ParkedCar:
    def __init__(self, POS, img, dimensions):
        self.x, self.y = POS
        self.image = img
        parkedCar = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(parkedCar)
        self.length, self.width = dimensions
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

    def get_corners(self):
        top_left = (self.x, self.y)
        top_right = (self.x + self.length, self.y)
        bottom_left = (self.x, self.y + self.width)
        bottom_right = (self.x + self.length, self.y + self.width)

        return top_left, top_right, bottom_left, bottom_right

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))


class Goal:
    def __init__(self, POS, img, dimensions):
        self.image = img
        self.x, self.y = POS
        self.length, self.width = dimensions
        new_rect = self.image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.center = new_rect.center

    def draw(self, win):
        win.blit(self.image, (self.x, self.y))

    def get_corners(self):
        top_left_corner = (self.x, self.y)
        # top_right_corner = (self.x + self.length, self.y)
        # bottom_left_corner = (self.x, self.y + self.width)
        bottom_right_corner = (self.x + self.length, self.y + self.width)

        return [top_left_corner, bottom_right_corner]

    def winCondition(self, drivingCar):
        x_property = False
        y_property = False
        DC = drivingCar.get_corners()
        for corner in DC:
            if self.get_corners()[0][0] < corner[0] and self.get_corners()[1][0] > corner[0]:
                x_property = True
            else:
                x_property = False
                break
            if self.get_corners()[0][1] < corner[1] and self.get_corners()[1][1] > corner[1]:
                y_property = True
            else:
                y_property = False
                break
        if x_property and y_property:
            return True
        return False
