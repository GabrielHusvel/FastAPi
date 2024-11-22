# Questão 2: 


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline


app = FastAPI()

# Carregar o pipeline de tradução
translator = pipeline("translation_en_to_fr", model="Helsinki-NLP/opus-mt-en-fr", device=0)

class TranslationInput(BaseModel):
    text: str

@app.post("/translate/")
def translate_text(input_text: TranslationInput):
    if not input_text.text:
        raise HTTPException(status_code=400, detail="Input text is required.")
    # Traduzir texto
    translated = translator(input_text.text, max_length=400)
    return {"input": input_text.text, "translation": translated[0]["translation_text"]}
