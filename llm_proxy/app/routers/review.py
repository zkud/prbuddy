from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from asyncio import gather
from logging import getLogger, StreamHandler


from ..llm.llm import LLMService


router = APIRouter()
llm = LLMService()
LOG = getLogger(__name__)
handler = StreamHandler()
LOG.addHandler(handler)


class File(BaseModel):
    name: str
    changes: str


class Diff(BaseModel):
    files: List[File]


class FileReview(BaseModel):
    name: str
    review: str


class Review(BaseModel):
    files: List[FileReview]


@router.get("/review-changes") 
async def review_changes(diff: Diff) -> Review:
    LOG.info('start reviewing')
    file_reviews = await gather(*(
        review_file(file)
        for file in diff.files
    ))
    LOG.info('review finished')
    return Review(files=file_reviews)


async def review_file(file: File) -> FileReview:
    review = await llm.review_file(file.changes)
    return FileReview(
        name=file.name,
        review=review
    )
