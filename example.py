'''
requires sys.path to contain path to repo root (can add manually too)

RUN COMMAND  python -i example.py
PRINT env AND INTERACT TO TEST
PRINT sys.path TO CHECK REPO ROOT DIR
'''

import sys
import gym
import gym_lunar_lander_custom

# print("SYS PATH: ", sys.path) # CHECK REPO ROOT DIR EXISTS

env=gym.make('LunarLanderMixedCustom-v0')

def random_rollout(render=False):
    total_reward, total_moves = 0,0
    
    observation = env.reset()
    done = False

    while(not done):
        if(render):
            env.render()

        action = env.action_space.sample()
        observation_, reward, done, info = env.step(action)

        total_reward += reward
        total_moves += 1

        observation = observation_ #redundant
    env.close()

    print(f"REWARD: {total_reward} \t LENGTH: {total_moves}")

random_rollout(render=True)