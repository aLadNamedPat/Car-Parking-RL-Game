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
        self.angular_velocity = 5
        self.acceleration = 0.1
        self.image = self.img
        self.mask = pygame.mask.from_surface(self.image)

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

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.angular_velocity * (self.velocity / self.max_speed)
        if right:
            self.angle -= self.angular_velocity * (self.velocity / self.max_speed)

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

    def get_corners(self):
        print(self.angle)
