from gym.envs.registration import registry, register, make, spec

register(
    id='LunarLanderCustom-v2',
    entry_point='lunar_lander_custom.env.lunar_lander:LunarLander',
    max_episode_steps=1000,
    reward_threshold=200,
)

register(
    id='LunarLanderContinuousCustom-v2',
    entry_point='lunar_lander_custom.env.lunar_lander:LunarLanderContinuous',
    max_episode_steps=1000,
    reward_threshold=200,
)

register(
    id='LunarLanderMixedCustom-v0',
    entry_point='lunar_lander_custom.env.lunar_lander:LunarLanderMixed',
    max_episode_steps=1000,
    reward_threshold=200,
)
