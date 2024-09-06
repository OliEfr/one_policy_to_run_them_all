from one_policy_to_run_them_all.environments.sea_snake.reward_functions.rudin_own_var import RudinOwnVarReward


def get_reward_function(name, env, **kwargs):
    if name == "rudin_own_var":
        return RudinOwnVarReward(env, **kwargs)
    else:
        raise NotImplementedError
