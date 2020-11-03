try:
    import Box2D
    from lunar_lander import LunarLander
    from lunar_lander import LunarLanderContinuous
    from lunar_lander import LunarLanderMixed
except ImportError:
    Box2D = None
