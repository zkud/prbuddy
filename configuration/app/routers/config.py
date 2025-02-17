from fastapi import APIRouter
from ..schemas.config import Config


router = APIRouter()


@router.post("/configs/{user_id}") 
async def create_config(user_id: str) -> Config:
    return Config(
        github_api_token='xzy',
        github_api_url='sadf'
    )

@router.patch("/configs/{user_id}") 
async def update_config(user_id: str) -> Config:
    return Config(
        github_api_token='xzy',
        github_api_url='sadf'
    )

@router.get("/configs/{user_id}") 
async def read_config(user_id: str) -> Config:
    return Config(
        github_api_token='xzy',
        github_api_url='sadf'
    )


@router.delete("/configs/{user_id}") 
async def delete_config(user_id: str):
    pass
