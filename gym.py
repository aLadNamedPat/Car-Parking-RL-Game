# REWARD FUNCTION PLAN

# Take reward to be the distance from parking spot. Closer the car is to the parking spot, the greater the reward
# This reward could be based on some sort of exponential function with distance as the input
# Make distance intervals when reward is given instead of anything continuous since the rounds are discrete.
import pygame
import numpy as np
import gym


class CustomEnv(gym.Env):
    def __init__(self, env_config={}):
        pass

    def reset(self):
        observation = 0
        return observation

    def step(self, action=np.zeros((2), dtype=np.float)):
        observation, reward, done, info = 0., 0., False, {}
        return observation, reward, done, info

    def render(step):
        pass
