from fastapi import FastAPI, HTTPException
from langchain.schema import HumanMessage
from langchain_openai.chat_models import ChatOpenAI
import os
from pydantic import BaseModel
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()

app = FastAPI()

# Modelo de entrada
class TextInput(BaseModel):
    text: str

# Configuração do OpenAI LangChain
llm = ChatOpenAI(
    model="gpt-3.5-turbo",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7
)

@app.post("/translate/")
async def translate_to_french(input: TextInput):
    """
    Traduz texto do inglês para o francês usando OpenAI via LangChain
    """
    try:
        # Criar o prompt e obter a tradução
        message = HumanMessage(content=f"Translate this to French: {input.text}")
        response = llm.invoke([message])
        return {"original_text": input.text, "translated_text": response.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# from fastapi import FastAPI, HTTPException
# from langchain_openai.chat_models import ChatOpenAI
# from langchain.chains import TransformChain
# from pydantic import BaseModel
# from dotenv import load_dotenv
# import os


# # Carregar o arquivo .env
# load_dotenv('.env')


# # Configurar o FastAPI
# app = FastAPI()

# # Configurar o modelo OpenAI para LangChain
# openai_llm = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  

# class InputText(BaseModel):
#     text: str

# # Endpoint para tradução
# @app.post("/translate/")
# async def translate(input: InputText):
#     try:
#         chain = TransformChain(llm=openai_llm)
#         translated_text = chain.run(f"Translate this to French: {input.text}")
#         return {"translated_text": translated_text}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
    
# def translate_using_openai_api(text):
#     """
#     Use the OpenAI API to translate text
#     """
#     template = ChatPromptTemplate([
#         ("system", "You are an English to French translator. Reject any other language."),
#         ("user", "Translate this: {text}")
#     ])
#     llm = ChatOpenAI(model="gpt-4o", api_key=os.getenv("OPENAI_API_KEY"))
#     response = llm.invoke(template.format_messages(text=text))
#     print(response.content)