from rl_x.environments.environment_manager import extract_environment_name_from_file, register_environment
from one_policy_to_run_them_all.environments.sea_snake.create_env import create_env
from one_policy_to_run_them_all.environments.sea_snake.default_config import get_config
from one_policy_to_run_them_all.environments.sea_snake.general_properties import GeneralProperties


SEASNAKE = extract_environment_name_from_file(__file__)
register_environment(SEASNAKE, get_config, create_env, GeneralProperties)
