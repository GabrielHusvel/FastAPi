from fastapi import FastAPI, Request
from langchain_community.llms import FakeListLLM
from pydantic import BaseModel

app = FastAPI()

# Respostas pré-definidas
responses = [
    "Olá! Como posso ajudá-lo hoje?",
    "Estou bem, obrigado por perguntar!",
    "Tenha um ótimo dia!"
]

# Configurar o FakeLLM
fake_llm = FakeListLLM(responses=responses)

class InputText(BaseModel):
    text: str

@app.post("/chatbot/")
async def chatbot(input: InputText):
    response = fake_llm(input.text)
    return {"response": response}
