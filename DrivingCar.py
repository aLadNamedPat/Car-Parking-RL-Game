import pygame
from pygame.math import Vector2
from rotation import blit_rotate_center
import math


class DrivingCar:
    length = 130
    width = 65

    def __init__(self):
        self.x, self.y = self.START
        self.angle = 0
        self.max_speed = 3
        self.min_speed = -3
        self.velocity = 0
        self.angular_velocity = 0.5
        self.acceleration = 0.1
        self.image = self.img
        self.image = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.x_pos, self.y_pos = self.x, self.y

    def move_forward(self):
        self.velocity = min(self.velocity + self.acceleration, self.max_speed)
        self.move()

    def move_backward(self):
        self.velocity = max(self.velocity - self.acceleration, self.min_speed)
        self.move()

    def break_speed(self):
        if self.velocity > 0:
            self.velocity = max(self.velocity - self.acceleration / 2, 0)
        if self.velocity < 0:
            self.velocity = min(self.velocity + self.acceleration / 2, 0)
        self.move()

    def move(self):
        radians = math.radians(self.angle)
        vertical = math.cos(radians) * self.velocity
        horizontal = math.sin(radians) * self.velocity

        self.x += vertical
        self.y -= horizontal
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.x_pos, self.y_pos = new_rect.topleft

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.angular_velocity
        if right:
            self.angle -= self.angular_velocity

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)

    def get_mask(self):
        self.image3 = pygame.transform.rotate(self.image2, self.angle)
        self.win.blit(self.image3, (100, 100))
        self.image4 = pygame.transform.rotate(self.image, self.angle)
        return pygame.mask.from_surface(self.image4)

    def get_corners(self):
        print(self.angle)
