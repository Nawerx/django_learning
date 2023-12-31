from dataclasses import dataclass
from environs import Env
@dataclass
class DBConfig:
    host: str
    port: int
    database: str
    user: str
    password: str


@dataclass
class Config:
    db: DBConfig



def load_config(path=".env") -> Config:
    env = Env()
    env.read_env(path)
    return Config(
        db=DBConfig(
            host=env.str("POSTGRES_HOST"),
            port=env.int("POSTGRES_PORT"),
            database=env.str("POSTGRES_DATABASE"),
            user=env.str("POSTGRES_USER"),
            password=env.str("POSTGRES_PASSWORD")
        )
    )