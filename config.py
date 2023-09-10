from dotenv import load_dotenv,dotenv_values

load_dotenv()
config = dotenv_values(".env")  # take environment variables from .env.


class Config:
    MONGO_URI = config['MONGO_URI']
    USER_DB = config['USER_DB']