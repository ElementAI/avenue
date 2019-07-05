from .env import *
from .wrappers import *
import random

"""
This file give the ability to register new environments. Given the inherited class, you will have different classes of
input.

host_ids: give the google drive links id given the os.

asset_name: refer to the right binary folder in unity_assets.
 
vector_state_class: refer to the type of vector that we want. (see in avenue_states.py)

TODO: doc overwrite reward etc.
"""

class AvenueCar(AvenueEnv):
    host_ids = {'linux': '1c5s_HhWSEmwm1JbP7tyy6V252zYVPl25'}
    asset_name = 'avenue_continuous'
    vector_state_class = "AvenueState"

class AvenueCarDev(AvenueEnv):
    host_ids = {'linux': ''}  # TODO: create a new google file here
    asset_name = 'avenue_continuous_dev'
    vector_state_class = "AvenueState"

def DriveAndAvoidPedestrians(config=None, **kwargs):
    old_config = {
        "road_length": 500,
        "curvature": 0,
        "lane_number": 2,
        "task": 0,
        "time": 13,
        "city_seed": 211,
        "skip_frame": 8,
        "height": 64,
        "width": 256,
        "night_mode":False,
        "pedestrian_distracted_percent": 0.5,
        "pedestrian_density": 50,
        "weather_condition": 0
    }

    env = AvenueCar(config=dict(old_config, **config) if config else old_config, **kwargs)
    env = ConcatMulti(env, {"rgb": ["rgb"], "vector": ["velocity_magnitude"]})
    return env
