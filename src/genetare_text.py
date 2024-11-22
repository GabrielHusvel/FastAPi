# Questão 1:

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline, set_seed

app = FastAPI()

# Carregar o pipeline GPT-2
text_generator = pipeline("text-generation", model="gpt2", device=0)
set_seed(42)  

class TextInput(BaseModel):
    text: str

@app.post("/generate-text/")
def generate_text(input_text: TextInput):
    if not input_text.text:
        raise HTTPException(status_code=400, detail="Input text is required.")
    # Gerar texto
    generated = text_generator(input_text.text, max_length=50, num_return_sequences=1)
    return {"input": input_text.text, "output": generated[0]["generated_text"]}

