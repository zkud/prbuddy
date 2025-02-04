from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage

def load_llm():
    llm = OllamaLLM(
        model="deepseek-r1:1.5b",
        base_url="http://ollama:11434",  # Default base URL for Ollama
        temperature=0.3,  # Lower creativity for concise responses
        top_p=0.85,       # Adjust diversity slightly
        max_tokens=150    # Limit the length of responses
    )
    return llm

if __name__ == "__main__":
    llm = load_llm()
    print(llm.invoke([HumanMessage(content="Hi!")]))
