from rl_x.environments.environment_manager import extract_environment_name_from_file, register_environment
from one_policy_to_run_them_all.environments.badger_locked.create_env import create_env
from one_policy_to_run_them_all.environments.badger_locked.default_config import get_config
from one_policy_to_run_them_all.environments.badger_locked.general_properties import GeneralProperties


BADGER_LOCKED = extract_environment_name_from_file(__file__)
register_environment(BADGER_LOCKED, get_config, create_env, GeneralProperties)
