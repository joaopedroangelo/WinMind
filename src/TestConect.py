import os
from openai import OpenAI

# Carrega a chave da API
api_key = os.getenv("OPENAI_API_KEY").strip()  # Remove qualquer caractere extra
if api_key:
    print("Chave da API carregada com sucesso!")
else:
    print("Erro: A chave da API não foi carregada.")


# Criando o cliente com a chave da API
client = OpenAI(api_key=api_key)


# Testando a API
try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Hello"}
        ]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Erro: {e}")
    import traceback
    traceback.print_exc()
