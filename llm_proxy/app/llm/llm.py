from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
from logging import getLogger
from re import sub, DOTALL


LOG = getLogger(__name__)


class LLMService:
    def __init__(self):
        self.__llm = OllamaLLM(
            model="llama3.1:8b",
            base_url="http://ollama:11434",  # Default base URL for Ollama
            temperature=0.3,  # Lower creativity for concise responses
            top_p=0.5,        # Adjust diversity slightly
            max_tokens=150,   # Limit the length of responses
        )

    async def review_file(self, changes: str) -> str:
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
        review = await self.__llm.ainvoke(messages)
        review = sub(r"<think>.*?</think>\n?", "", review, flags=DOTALL)
        return str(review)