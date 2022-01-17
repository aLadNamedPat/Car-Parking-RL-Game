import pygame
from rotation import blit_rotate_center
import math
from Line_Intersection import *


class DrivingCar:
    length = 130
    width = 65

    def __init__(self):
        self.x, self.y = self.START
        self.angle = 0
        self.max_speed = 3
        self.min_speed = -3
        self.velocity = 0
        self.angular_velocity = 3
        self.acceleration = 0.1
        self.image = self.img
        self.image = self.image.convert_alpha()
        self.mask = pygame.mask.from_surface(self.image)
        self.x_pos, self.y_pos = self.x, self.y
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(
            center=self.image.get_rect(topleft=(self.x, self.y)).center)
        self.center = new_rect.center
        self.is_Alive = True
        self.win_Game = False
        radians = self.angle * math.pi / 180
        self.original_center = self.center
        # car_center = (car.x, car.y) # for use later when headless
        self.top_center = (self.center[0] + math.cos(radians)
                           * 70, self.center[1] - math.sin(radians) * 70)

        self.bottom_center = (self.center[0] - math.cos(radians)
                              * 70, self.center[1] + math.sin(radians) * 70)

        self.left_center = (self.center[0] + (math.cos((radians + math.pi/2)) * 35),
                            self.center[1] - (math.sin((radians + math.pi/2)) * 35))
        self.right_center = (self.center[0] + math.cos(radians - math.pi/2)
                             * 35, self.center[1] - math.sin(radians - math.pi/2) * 35)

        self.top_right = (self.right_center[0] + math.cos(radians)
                          * 70, self.right_center[1] - math.sin(radians) * 70)
        self.bottom_right = (self.right_center[0] - math.cos(radians)
                             * 70, self.right_center[1] + math.sin(radians) * 70)

        self.top_left = (self.left_center[0] + math.cos(radians)
                         * 70, self.left_center[1] - math.sin(radians) * 70)
        self.bottom_left = (self.left_center[0] - math.cos(radians)
                            * 70, self.left_center[1] + math.sin(radians) * 70)

    def get_corners(self):

        radians = self.angle * math.pi / 180
        # car_center = (car.x, car.y) # for use later when headless
        self.top_center = (self.center[0] + math.cos(radians)
                           * 70, self.center[1] - math.sin(radians) * 70)

        self.bottom_center = (self.center[0] - math.cos(radians)
                              * 70, self.center[1] + math.sin(radians) * 70)

        self.left_center = (self.center[0] + (math.cos((radians + math.pi/2)) * 35),
                            self.center[1] - (math.sin((radians + math.pi/2)) * 35))
        self.right_center = (self.center[0] + math.cos(radians - math.pi/2)
                             * 35, self.center[1] - math.sin(radians - math.pi/2) * 35)

        self.top_right = (self.right_center[0] + math.cos(radians)
                          * 70, self.right_center[1] - math.sin(radians) * 70)
        self.bottom_right = (self.right_center[0] - math.cos(radians)
                             * 70, self.right_center[1] + math.sin(radians) * 70)

        self.top_left = (self.left_center[0] + math.cos(radians)
                         * 70, self.left_center[1] - math.sin(radians) * 70)
        self.bottom_left = (self.left_center[0] - math.cos(radians)
                            * 70, self.left_center[1] + math.sin(radians) * 70)

        return [self.top_left, self.bottom_left, self.bottom_right, self.top_right]

    def update_corners(self):
        radians = self.angle * math.pi / 180
        # car_center = (car.x, car.y) # for use later when headless
        self.top_center = (self.center[0] + math.cos(radians)
                           * 70, self.center[1] - math.sin(radians) * 70)

        self.bottom_center = (self.center[0] - math.cos(radians)
                              * 70, self.center[1] + math.sin(radians) * 70)

        self.left_center = (self.center[0] + (math.cos((radians + math.pi/2)) * 35),
                            self.center[1] - (math.sin((radians + math.pi/2)) * 35))
        self.right_center = (self.center[0] + math.cos(radians - math.pi/2)
                             * 35, self.center[1] - math.sin(radians - math.pi/2) * 35)

        self.top_right = (self.right_center[0] + math.cos(radians)
                          * 70, self.right_center[1] - math.sin(radians) * 70)
        self.bottom_right = (self.right_center[0] - math.cos(radians)
                             * 70, self.right_center[1] + math.sin(radians) * 70)

        self.top_left = (self.left_center[0] + math.cos(radians)
                         * 70, self.left_center[1] - math.sin(radians) * 70)
        self.bottom_left = (self.left_center[0] - math.cos(radians)
                            * 70, self.left_center[1] + math.sin(radians) * 70)

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
        self.center = new_rect.center
        self.update_corners()

    def rotate(self, left=False, right=False):
        if left:
            self.angle += self.angular_velocity * self.velocity / self.max_speed

        if right:
            self.angle -= self.angular_velocity * self.velocity / self.max_speed

    def draw(self, win):
        blit_rotate_center(win, self.image, (self.x, self.y), self.angle)

    def get_mask(self):
        # self.image3 = pygame.transform.rotate(self.image2, self.angle)
        # self.win.blit(self.image3, (100, 100))
        self.image4 = pygame.transform.rotate(self.image, self.angle)
        return pygame.mask.from_surface(self.image4)

    def sensor_measures(self, objects):
        maxSensorLength = 200
        # 8 total sensor measurements
        # TopCenter, TopRight, MidRight, BottomRight, BottomCenter, BottomLeft, MidLeft, TopLeft
        sensors = [amplify(self.center, self.top_center, maxSensorLength),
                   amplify(self.center, self.top_right, maxSensorLength),
                   amplify(self.center, self.right_center, maxSensorLength),
                   amplify(self.center, self.bottom_right, maxSensorLength),
                   amplify(self.center, self.bottom_center, maxSensorLength),
                   amplify(self.center, self.bottom_left, maxSensorLength),
                   amplify(self. center, self.left_center, maxSensorLength),
                   amplify(self.center, self.top_left, maxSensorLength)
                   ]

        sensorReturns = [[], [], [], [], [], [], [], []]
        Sensors = ["front", "front-right", "center-right", "back-right",
                   "back", "back-left", "center-left", "front-left"]
        values = []
        for object in objects:
            top_left, top_right, bottom_left, bottom_right = object.get_corners()
            top_segment = (top_left, top_right)
            right_segment = (top_right, bottom_right)
            bottom_segment = (bottom_right, bottom_left)
            left_segment = (bottom_left, top_left)
            segments = [top_segment, right_segment,
                        bottom_segment, left_segment]
            for segment in segments:
                for i in range(len(sensors)):
                    if doIntersect(sensors[i], segment):
                        intersectPoint = get_intersect(segment, sensors[i])
                        sensorReturns[i].append(
                            get_distance(intersectPoint, self.center))
                    else:
                        sensorReturns[i].append(maxSensorLength)
        for sensor in sensorReturns:
            values.append(min(sensor))
        return values

    def get_distance_from_goal(self, goal):
        distance = get_distance(self.center, goal.center)
        return distance

    def if_moved(self):
        if get_distance(self.original_center, self.center) > 30:
            return True
        return False
