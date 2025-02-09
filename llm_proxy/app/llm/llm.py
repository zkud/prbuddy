from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, Field
from enum import Enum
from logging import getLogger
from typing import Optional


class Status(Enum):
    OK = 'OK'
    ERR = 'ERR'


class Review(BaseModel):
    status: str = Field(description="Status of code review, \"OK\" if code review is passed, \"ERR\" if there are some issues")
    summary: str = Field(description="Review summary")


LOG = getLogger(__name__)


class LLMService:
    def __init__(self):
        self.__llm = ChatOllama(
            model="deepseek-r1:1.5b",
            base_url="http://ollama:11434",  # Default base URL for Ollama
            temperature=0.3,  # Lower creativity for concise responses
            top_p=0.5,        # Adjust diversity slightly
            max_tokens=5000,  # Limit the length of responses
        ).with_structured_output(Review, method="json_schema")

    async def review_file(self, changes: str) -> Optional[str]:
        LOG.info('start file reviewing')
        messages = [
            SystemMessage(
                content="""
                    Review the file git diff provided by user. Focus on code style on obvious bugs.
                    Code might be correct, just reply with something like that's correct if it is.
                    File:
                """
            ),
            HumanMessage(content=changes),
        ]
        review: Review = await self.__llm.ainvoke(messages)

        if review.status == Status.OK.value:
            return None
            
        return review.summary