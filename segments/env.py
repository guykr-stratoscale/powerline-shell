import os

def add_env_segment():

    if os.getenv('PROMPT_MODE'):
        bg = Color.ENV_BG
        fg = Color.ENV_FG
        powerline.append('env', fg, bg)
    else:
        bg = Color.NO_ENV_BG
        fg = Color.NO_ENV_FG
        powerline.append('no env', fg, bg)

add_env_segment()
