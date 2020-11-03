# LunarLander-Custom

Installation:

`pip install git+https://github.com/nimishsantosh107/LunarLander-Custom.git`

Usage:

```python
import gym
import lunar_lander_custom

env=gym.make('LunarLanderMixedCustom-v0')
```

Default Environments:

* `LunarLanderDefault-v2` - Same as original LunarLander-v2
* `LunarLanderContinuousDefault-v2` - Same as original LunarLanderContinuous-v2

Custom Environments:

* `LunarLanderMixedCustom-v0` - Modified environment with mixed action space.

|Property|Details|
|---|---|
|observation_space | `Box(-np.inf, np.inf, shape=(1,))` <br> `[-1,+1]`: useful range ± spikes. |
|action_space |`Tuple(Discrete(2), Box(-1,1, shape=(1,)))`  
|example `action` | `(1, array([0.19599484], dtype=float32))`|
|`action[0]` | **Main Engine** <br> `Discrete(2)` <br> `0` - 0% power <br> `1` - 100% power|
|`action[1]` <br> or <br> `action[1][0]` | **Orientation Engines** <br> `Box(-1,1, shape=(1,))` <br> `action[1][0]` because shape=(1,) <br> `[-1.0, -0.5)` - Left: 50%-100% power <br> `[-0.5, +0.5]` - 0% power <br> `(+0.5, +1.0]` - Right: 50%-100% power |


**Note:** Refer `example.py` for more instructions.