from langchain_ollama import OllamaLLM
from langchain_core.messages import HumanMessage
from fastapi import FastAPI

app = FastAPI()

def load_llm():
    llm = OllamaLLM(
        model="deepseek-r1:1.5b",
        base_url="http://ollama:11434",  # Default base URL for Ollama
        temperature=0.3,  # Lower creativity for concise responses
        top_p=0.85,       # Adjust diversity slightly
        max_tokens=150    # Limit the length of responses
    )
    return llm

@app.get("/") 
async def main_route():     
  return {"message": llm.invoke([HumanMessage(content="Hi!")])}

llm = load_llm()