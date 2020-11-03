import sys
import gym
import numpy as np
from gym import spaces

import lunar_lander_custom 

# env=gym.make('LunarLanderMixedCustom-v0')

# custom_space = spaces.Tuple((
#     # Main engine - 0-off, 1-on
#     spaces.Discrete(2),
#     # Left-right:  -1.0..-0.5 fire left engine, +0.5..+1.0 fire right engine, -0.5..0.5 off
#     spaces.Box(-1, +1, (1,), dtype=np.float32),
# ))
