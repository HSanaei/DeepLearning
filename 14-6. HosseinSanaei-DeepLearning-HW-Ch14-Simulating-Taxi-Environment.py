# -*- coding: utf-8 -*-
"""14-6. HosseinSanaei-DeepLearning-HW-Ch14-Simulating-Taxi-Environment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IxqDHuvrEuVGS7Ql-E32We-LDFuhOO0N
"""

'''
Python Machine Learning
Teacher: Dr Rahmani
Student: Hossein SANAEI ~حسين سنايي

Aras International Campus of University of Tehran
Spring 1401 (2022)
GitHub: https://github.com/HSanaei/DeepLearing.git

Chapter 14-6:  Simulating the taxi environment
'''
# 1. First we create an instance of the Taxi environment:
import torch
import gym

env = gym.make('Taxi-v3')
n_state = env.observation_space.n
print(n_state)

n_action = env.action_space.n
print(n_action)

'''We also know that the state is represented by an integer ranging from 0 to
499, and there are 6 possible actions.
'''

# 2. We reset the environment and render it:
env.reset()

env.render()

# The passenger is on the blue R tile, and the destination is on the purple Y.

'''
Now let's go pick up the passenger by heading west for three tiles and north
for two tiles (you will need to take different actions according to your initial
state) then take the "pick-up" action:
'''
print(env.step(3))
print(env.step(3))
print(env.step(3))
print(env.step(1))
print(env.step(1))
print(env.step(4))

# Render the environment:
env.render()

# The taxi turns green, meaning the passenger is inside the taxi.

'''
Now let's head to the destination by taking the "down" action four times
(again, you will need to take your own set of actions) then executing a "dropoff":
'''
print(env.step(0))
print(env.step(0))
print(env.step(0))
print(env.step(0))
print(env.step(5))

# A +20 reward is granted in the end for a successful drop-off.

# We render the environment finally:
env.render()
'''
You can take some random actions and see how difficult it is for a model to solve the
environment. We will discuss the Q-learning algorithm in the next section.
'''