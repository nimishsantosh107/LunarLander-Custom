'''
RUN COMMAND  python -i example.py
PRINT env AND INTERACT TO TEST
PRINT sys.path TO CHECK REPO ROOT DIR

Note: If installed using PIP then package is added to PATH by default.
      If installed using GIT:
                   sys.path.insert(0, [PATH TO REPO_ROOT_DIR])
'''

import sys
import gym
import gym_lunar_lander_custom


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