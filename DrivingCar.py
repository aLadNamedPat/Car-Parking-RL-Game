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
<<<<<<< HEAD
        self.angular_velocity = 3
=======
        self.angular_velocity = 0.5
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180
        self.acceleration = 0.1
        self.image = self.img
        self.image = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.x_pos, self.y_pos = self.x, self.y
<<<<<<< HEAD
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.center = new_rect.center

    def get_corners(self):

        radians = self.angle * math.pi / 180
        car_center = self.center
        # car_center = (car.x, car.y) # for use later when headless
        left_center = (car_center[0] + (math.cos((radians + math.pi/2)) * 35),
                       car_center[1] - (math.sin((radians + math.pi/2)) * 35))
        right_center = (car_center[0] + math.cos(radians - math.pi/2)
                        * 35, car_center[1] - math.sin(radians - math.pi/2) * 35)

        top_right = (right_center[0] + math.cos(radians)
                     * 70, right_center[1] - math.sin(radians) * 70)
        bottom_right = (right_center[0] - math.cos(radians)
                        * 70, right_center[1] + math.sin(radians) * 70)

        top_left = (left_center[0] + math.cos(radians)
                    * 70, left_center[1] - math.sin(radians) * 70)
        bottom_left = (left_center[0] - math.cos(radians)
                       * 70, left_center[1] + math.sin(radians) * 70)

        return [top_left, bottom_left, bottom_right, top_right]
=======
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180

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
        if self.angle > 360:
            self.angle -= 360
        if self.angle < 0:
            self.angle += 360

        self.x += vertical
        self.y -= horizontal
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.x_pos, self.y_pos = new_rect.topleft
<<<<<<< HEAD
        self.center = new_rect.center

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.angular_velocity * \
                (self.velocity / self.max_speed)
        if right:
            self.angle -= self.angular_velocity * \
                (self.velocity / self.max_speed)
=======

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.angular_velocity
        if right:
            self.angle -= self.angular_velocity
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)

    def get_mask(self):
<<<<<<< HEAD
        # self.image3 = pygame.transform.rotate(self.image2, self.angle)
        # self.win.blit(self.image3, (100, 100))
        self.image4 = pygame.transform.rotate(self.image, self.angle)
        return pygame.mask.from_surface(self.image4)
=======
        self.image3 = pygame.transform.rotate(self.image2, self.angle)
        self.win.blit(self.image3, (100, 100))
        self.image4 = pygame.transform.rotate(self.image, self.angle)
        return pygame.mask.from_surface(self.image4)

    def get_corners(self):
        print(self.angle)
>>>>>>> 17f24328ade001d49b84c0dd4e746d0e7fe6e180
