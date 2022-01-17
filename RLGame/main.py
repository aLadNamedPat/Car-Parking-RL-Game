import pygame
import sys
import random
import os
from pygame.math import Vector2
from DrivingCar import DrivingCar
from Parked import ParkedCar, Goal
from Border import Border
import time

pygame.init()
pygame.font.init()

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

# DISPLAY SURFACE HERE
display_surface = pygame.display.set_mode((780, 450))
# display_surface.blit(parkingLot, (0, 0))
# display_surface.blit(parkedCar2, (640, 100))
FPS = 60
run = True
clock = pygame.time.Clock()


def draw(win, images, playerCar, parkedCars, wingoal, border):
    # for img, pos in images:
    #     win.blit(img, pos)
    for parkedCar in parkedCars:
        parkedCar.draw(win)
    wingoal.draw(win)
    playerCar.draw(win)
    border.draw(win)
    pygame.display.update()


class playerCar(DrivingCar):
    img = playerCar
    START = (16, 10)
    win = display_surface


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
    # ADDING WIN GAME CONDITION
    spots2 = spots[len(spots) - 1]
    for num in spots1:
        carParks.append(parkingSpots2[num][0])
        cars.append(ParkedCar(parkingSpots2[num][0], img, (120, 60)))
    return cars, parkingSpots2[spots2][0], parkingSpots2[spots2][1]


border = Border((0, -2), OuterBorder, (780, 450))
parking = genParkedCars(8, AllParkingSpaces, parkedCar3)
parkedCars = parking[0]
obstacles = parkedCars + [border]
carParkedPosition = parking[2]
if carParkedPosition == 0:
    goalparking = (parking[1][0] - 5, parking[1][1] - 10)
if carParkedPosition == 1:
    goalparking = (parking[1][0] - 27, parking[1][1] - 10)

goal = Goal(goalparking, winningParkingSpace, (160, 80))

player_car = playerCar()

while run:
    clock.tick(FPS)
    draw(display_surface, [(parkingLot, (0, 0))],
         player_car, parkedCars, goal, border)
    # if goal.winCondition(player_car):
    #     print("WIN")
    # pygame.draw.circle(display_surface, (0, 0, 255),
    #                    goal.center, 4)
    # print(type(obstacles))
    # player_car.sensor_measures(obstacles)
    # for parkCar in parkedCars:
    #     if parkCar.collide(player_car):
    #         print("collide")
    #         print(parkCar.collide(player_car))
    #         print(player_car.x, player_car.y)

    # if border.collide(player_car):
    #     print("HIT")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            break

    keys = pygame.key.get_pressed()
    moved = False

    if keys[pygame.K_a]:
        player_car.rotate(left=True)
    if keys[pygame.K_d]:
        player_car.rotate(right=True)
    if keys[pygame.K_w]:
        moved = True
        player_car.move_forward()
    if keys[pygame.K_s]:
        moved = True
        player_car.move_backward()

    if not moved:
        player_car.break_speed()
pygame.quit()
