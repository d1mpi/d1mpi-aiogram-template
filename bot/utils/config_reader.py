from dataclasses import dataclass
from environs import Env
from pathlib import Path

BASE_DIR = Path(__file__).parent

env = Env()
env.read_env(f'{BASE_DIR}/.env')


@dataclass
class Config:
    token: str
    lang: str
    postgres_connect: str
    super_users: list[int]


def load_config():
    return Config(
        token=env("BOT_TOKEN"),
        lang=env("BOT_LANGUAGE"),
        postgres_connect=env("POSTGRES_CONNECT"),
        super_users=[int(_id) for _id in env('SUPERUSERS_TELEGRAM_ID').split() if _id.isdigit()]
    )


config = load_config()
