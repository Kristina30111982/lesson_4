from dotenv import load_dotenv

load_dotenv()


class BaseSettings:
    pass


class Settings(BaseSettings):
    DATABASE_URL: str

    class Config:
        env_file = '.env'


settings = Settings()

