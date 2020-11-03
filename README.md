# LunarLanderCustom

Environments:

* `LunarLanderCustom-v2` - Same as original LunarLander-v2
* `LunarLanderContinuousCustom-v2` - Same as original LunarLanderContinuous-v2

Usage:

```python
import sys
sys.path.insert(0,'./lunar_lander/')

import gym
import lunar_lander

env=gym.make('LunarLanderCustom-v2')
```