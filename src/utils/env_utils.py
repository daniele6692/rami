import os


def get_env_var(var_name):
    return os.getenv(var_name)


def get_env_file_path():
    stage = get_env_var('RAMI_STAGE')
    print(f"Stage value is {stage}")
    if stage:
        return f'./stages/{stage}/.env'
    return f'./stages/local/.env'
