from pydantic_settings import BaseSettings, SettingsConfigDict

#Setting to change the behaviour of a core code without changing the core code
class Settings(BaseSettings):
    PROJECT_NAME: str = "JobHunter"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DATABASE_URL: str = "postgresql://jobhunter:jobhunter_secret@localhost:5432/jobhunter"

    model_config = SettingsConfigDict(env_file=".env",case_sensitive=True, extra="ignore")

settings = Settings() #Singleton Pattern, it imports the module once, reads, 
                      #validate and stores the data for instant look-up

