from fastapi import FastAPI, HTTPException
from transformers import pipeline
from pydantic import BaseModel

app = FastAPI()

# Carregar o modelo de tradução
translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de", device=0)

# Modelo de entrada
class TextInput(BaseModel):
    text: str

@app.post("/translate/")
async def translate_to_german(input: TextInput):
    """
    Traduz texto do inglês para o alemão usando Helsinki-NLP diretamente com transformers.
    """
    try:
        # Obter a tradução
        result = translator(input.text, max_length=400)
        translated_text = result[0]["translation_text"]
        return {"original_text": input.text, "translated_text": translated_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# from fastapi import FastAPI, HTTPException
# from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
# from pydantic import BaseModel

# app = FastAPI()

# # Carregar o modelo de tradução
# # translator = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de", device=0)
# gpu_llm = HuggingFacePipeline.from_model_id(
#     model_id="Helsinki-NLP/opus-mt-en-de",
#     task="translation",
#     device=0,
#     pipeline_kwargs={"max_new_tokens": 10},
# )
# # Modelo de entrada
# class TextInput(BaseModel):
#     text: str

# @app.post("/translate/")
# async def translate_to_german(input: TextInput):
#     """
#     Traduz texto do inglês para o alemão usando Helsinki-NLP diretamente com transformers.
#     """
#     try:
#         # Obter a tradução
#         result = gpu_llm(input.text, max_length=400)
#         print(result)
#         print(type(result))

#         translated_text = result[0]["translation_text"]
#         return {"original_text": input.text, "translated_text": translated_text}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))


