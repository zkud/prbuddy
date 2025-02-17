from pydantic import BaseModel


class Config(BaseModel):
    github_api_url: str
    github_api_token: str
