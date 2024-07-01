from pydantic_settings import BaseSettings

class cred(BaseSettings):
    database_name:str
    database_username:str
    database_password:str
    database_host:str
    database_hostname:str
    secret_key:str
    algorithm:str
    access_token_expire_minutes:int
    class Config:
        config_file="C:/Users/DELL/Desktop/API/.env"
   
settings=cred()