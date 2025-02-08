from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage, SystemMessage
from logging import getLogger


LOG = getLogger(__name__)


class LLMService:
    def __init__(self):
        self.__llm = OllamaLLM(
            model="deepseek-r1:1.5b",
            base_url="http://ollama:11434",  # Default base URL for Ollama
            temperature=0.3,  # Lower creativity for concise responses
            top_p=0.85,       # Adjust diversity slightly
            max_tokens=150    # Limit the length of responses
        )

    async def review_file(self, changes: str) -> str:
        LOG.info('start file reviewing')
        return str(await self.__llm.ainvoke([
            SystemMessage(
                content="Review the file provide by user. Focus on code style on obvious bugs. File:"
            ),
            HumanMessage(content=changes),
        ]))