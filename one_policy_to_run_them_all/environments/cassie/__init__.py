from rl_x.environments.environment_manager import extract_environment_name_from_file, register_environment
from one_policy_to_run_them_all.environments.cassie.create_env import create_env
from one_policy_to_run_them_all.environments.cassie.default_config import get_config
from one_policy_to_run_them_all.environments.cassie.general_properties import GeneralProperties


UNITREE_H1 = extract_environment_name_from_file(__file__)
register_environment(UNITREE_H1, get_config, create_env, GeneralProperties)
