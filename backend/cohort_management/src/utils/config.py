'''
Config file for connection with db.
'''

import os
from pydantic_settings import BaseSettings, SettingsConfigDict


class GlobalConfig(BaseSettings):
    '''Class with personalized config for app.'''

    DATABASE_URL: str = "postgresql+asyncpg://postgres:123ilawa45@localhost/devdb"
    DB_FORCE_ROLL_BACK: bool = False

    model_config = SettingsConfigDict(
        env_file=f"config/.env/.env.{os.getenv('ENV_STATE', 'development')}"
    )


config = GlobalConfig()
