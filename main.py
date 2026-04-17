from fastapi import FastAPI
from pydantic import BaseModel
import random

from knowledge_base import BASE, CRITICAL_KEYWORDS, DEFAULT_RESPONSES, SELF_CARE_TIPS

app = FastAPI()

# Declaração ética
ETHICAL_NOTICE = """
Este sistema foi projetado com limitações intencionais para evitar riscos éticos,
não realizando diagnósticos ou recomendações clínicas.
Atua apenas como um assistente de apoio emocional e escuta inicial.
"""

class Input(BaseModel):
    message: str


# Normalização (resolve feminino/masculino)
def normalize_text(text):
    text = text.lower()

    replacements = {
        "ansiosa": "ansioso",
        "preocupada": "preocupado",
        "nervosa": "nervoso",
        "aflita": "aflito",
        "tensa": "tenso",
        "estressada": "estressado",
        "cansada": "cansado",
        "sobrecarregada": "sobrecarregado",
        "insegura": "inseguro",
        "sozinha": "sozinho",
        "desanimada": "desanimado"
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    return text


def check_critical(text):
    text = normalize_text(text)

    for word in CRITICAL_KEYWORDS:
        if word in text:
            return True
    return False


def get_response(user_input):
    user_input = normalize_text(user_input)

    # Caso crítico (não adiciona dicas)
    if check_critical(user_input):
        return {
            "response": "Sinto muito que você esteja passando por isso. É importante procurar ajuda profissional ou conversar com alguém de confiança. Você não está sozinho.",
            "risk": "high"
        }

    # Busca na base
    for topic, data in BASE.items():
        for keyword in data["keywords"]:
            if keyword in user_input:

                response_text = random.choice(data["responses"])

                # Adiciona dica de autocuidado
                response_text += "\n\n" + random.choice(SELF_CARE_TIPS)

                return {
                    "response": response_text,
                    "risk": "low"
                }

    # Fallback
    return {
        "response": random.choice(DEFAULT_RESPONSES) + "\n\n" + random.choice(SELF_CARE_TIPS),
        "risk": "low"
    }


# Endpoint principal
@app.post("/chat")
def chat(input: Input):
    result = get_response(input.message)

    return {
        "ethical_notice": ETHICAL_NOTICE,
        "user_input": input.message,
        "response": result["response"] + "\n\n" + ETHICAL_NOTICE,
        "risk_level": result["risk"]
    }


# Simulação de TOOL MCP
TOOLS = [
    {
        "name": "mental_health_helper",
        "description": "Auxilia usuários com respostas de apoio emocional (não clínico)",
        "input_schema": {
            "type": "object",
            "properties": {
                "message": {"type": "string"}
            }
        }
    }
]