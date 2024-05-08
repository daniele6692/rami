import os

from src.utils.const import LOCAL_STAGE


def get_env_var(var_name):
    return os.getenv(var_name)


def get_env_file_path():
    stage = get_env_var('RAMI_STAGE')
    print(f"Stage value is {stage}")
    return f'./stages/{stage}/.env'


def is_running_locally():
    stage = get_env_var('RAMI_STAGE')
    return stage == LOCAL_STAGE
