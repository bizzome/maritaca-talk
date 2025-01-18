import maritalk
import os

# pip install python-dotenv
from dotenv import load_dotenv

load_dotenv()

model = maritalk.MariTalk(
    key=os.getenv("MARITACA_API_KEY"),
    model="sabia-3"  # No momento, suportamos os modelos sabia-3, sabia-2-medium e sabia-2-small
)

# Exemplo de uso
response = model.generate("O que é a vida?")
print(response)
