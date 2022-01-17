import pygame
import random
from pygame.math import Vector2
from DrivingCar import DrivingCar
from Parked import ParkedCar, Goal
from Border import Border

parkedCar1 = pygame.image.load("Images\parkedCar1.png")
parkedCar2 = pygame.image.load("Images\parkedCar2.png")
parkedCar3 = pygame.image.load("Images\parkedCar3.png")

parkedCar1 = pygame.transform.scale(parkedCar1, (120, 60))
parkedCar2 = pygame.transform.scale(parkedCar2, (120, 60))
parkedCar3 = pygame.transform.scale(parkedCar3, (120, 60))
parkedCarsList = [parkedCar1, parkedCar2, parkedCar3]
playerCar = pygame.image.load("Images\playerCar.png")
playerCar = pygame.transform.scale(playerCar, (140, 70))

testCar = pygame.image.load("Images\\testCar.png")
testCar = pygame.transform.scale(testCar, (130, 65))
parkingLot = pygame.image.load("Images\Parking Lot Image.png")
parkingLot = pygame.transform.rotate(parkingLot, 90)
parkingLot = pygame.transform.scale(parkingLot, (780, 450))

OuterBorder = pygame.image.load("Images\OuterBorder.png")
OuterBorder = pygame.transform.scale(OuterBorder, (780, 450))

winningParkingSpace = pygame.image.load("Images\ParkingSpace.png")
winningParkingSpace = pygame.transform.scale(winningParkingSpace, (160, 90))


def draw(win, images, playerCar, parkedCars, wingoal, border):
    for img, pos in images:
        win.blit(img, pos)
    for parkedCar in parkedCars:
        parkedCar.draw(win)
    wingoal.draw(win)
    playerCar.draw(win)
    border.draw(win)
    pygame.display.update()


class playerCar(DrivingCar):
    img = playerCar
    START = (16, 10)


parkingSpotsL = [
    [(16, 10), 0],
    [(16, 100), 0],
    [(16, 190), 0],
    [(16, 280), 0],
    [(16, 370), 0],
]

parkingSpotsC = [
    [(250, 100), 1],
    [(250, 190), 1],
    [(250, 280), 1],
    [(395, 100), 0],
    [(395, 190), 0],
    [(395, 280), 0],
]

parkingSpotsR = [
    [(640, 10), 1],
    [(640, 100), 1],
    [(640, 190), 1],
    [(640, 280), 1],
    [(640, 370), 1],
]

AllParkingSpaces = [
    [(16, 100), 0],
    [(16, 190), 0],
    [(16, 280), 0],
    [(16, 370), 0],
    [(250, 100), 1],
    [(250, 190), 1],
    [(250, 280), 1],
    [(395, 100), 0],
    [(395, 190), 0],
    [(395, 280), 0],
    [(640, 10), 1],
    [(640, 100), 1],
    [(640, 190), 1],
    [(640, 280), 1],
    [(640, 370), 1],
]


def genParkedCars(numCars, parkingSpots, img):
    parkingSpots2 = parkingSpots
    carParks = []
    cars = []
    spots = random.sample(range(len(parkingSpots)), numCars)
    spots1 = spots[0:len(spots) - 2]
    spots2 = spots[len(spots) - 1]
    for num in spots1:
        carParks.append(parkingSpots2[num][0])
        cars.append(ParkedCar(parkingSpots2[num][0], img, (120, 60)))
    return cars, parkingSpots2[spots2][0], parkingSpots2[spots2][1]


class PyGame2D:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((780, 450))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.FPS = 60
        self.border = Border((0, -2), OuterBorder, (780, 450))
        self.parking = genParkedCars(8, AllParkingSpaces, parkedCar3)
        self.parkedCars = self.parking[0]
        self.obstacles = self.parkedCars + [self.border]
        self.carParkedPosition = self.parking[2]
        if self.carParkedPosition == 0:
            self.goalparking = (
                self.parking[1][0] - 5, self.parking[1][1] - 10)
        if self.carParkedPosition == 1:
            self.goalparking = (
                self.parking[1][0] - 27, self.parking[1][1] - 10)

        self.goal = Goal(self.goalparking, winningParkingSpace, (160, 80))
        self.player_car = playerCar()
        self.original_distance = self.player_car.get_distance_from_goal(
            self.goal)
        self.game_speed = 60

    def action(self, action):
        moved = False
        if action == 0:
            self.player_car.move_forward()
            moved = True
        elif action == 1:
            self.player_car.move_forward()
            self.player_car.rotate(left=True)
            moved = True
        elif action == 2:
            self.player_car.move_forward()
            self.player_car.rotate(right=True)
            moved = True
        elif action == 3:
            self.player_car.move_backward()
            moved = True
        elif action == 4:
            self.player_car.move_backward()
            self.player_car.rotate(left=True)
            moved = True
        elif action == 5:
            self.player_car.move_backward()
            self.player_car.rotate(right=True)
            moved = True
        elif action == 6:
            self.player_car.rotate(left=True)
            moved = True
        elif action == 7:
            self.player_car.rotate(right=True)
            moved = True
        elif action == 8:
            moved = False

        if not moved:
            self.player_car.break_speed()

        for parkCar in self.parkedCars:
            if parkCar.collide(self.player_car):
                self.player_car.is_Alive = False

        if self.border.collide(self.player_car):
            self.player_car.is_Alive = False

        if self.goal.winCondition(self.player_car):
            self.player_car.win_Game = True

        # MAKE METHOD CHECKING HOW FAR THEY ARE FROM THE GOAL

    def evaluate(self):
        reward = 0
        """
        if self.car.check_flag:
            self.car.check_flag = False
            reward = 2000 - self.car.time_spent
            self.car.time_spent = 0
        """
        if self.player_car.if_moved():
            self.player_car.original_center = self.player_car.center
            reward += (50 - self.player_car.get_distance_from_goal(self.goal) / 100)
        if not self.player_car.is_Alive:
            reward = -1000 + self.player_car.get_distance_from_goal(self.goal)
        elif self.player_car.win_Game:
            reward += 10000
        return reward

    def is_done(self):
        if not self.player_car.is_Alive or self.player_car.win_Game:
            return True
        return False

    def observe(self):
        # return state
        radars = self.player_car.sensor_measures(self.obstacles)
        ret = [0., 0., 0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.,  0.]
        for i, r in enumerate(radars):
            ret[i] = r / 200
        ret[8] = self.player_car.velocity / self.player_car.max_speed
        ret[9] = self.player_car.angle / 360
        ret[10] = self.player_car.get_distance_from_goal(self.goal) / 900
        return tuple(ret)

    def view(self):
        # draw game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        draw(self.screen, [(parkingLot, (0, 0))], self.player_car,
             self.parkedCars, self.goal, self.border)
        self.clock.tick(self.game_speed)
