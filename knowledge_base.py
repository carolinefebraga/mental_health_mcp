# knowledge_base.py
BASE = {
    "tristeza": {
        "keywords": ["triste", "tristeza", "desanimado", "pra baixo", "sem vontade", "desanimada"],
        "responses": [
            "A tristeza é uma emoção natural e faz parte do comportamento humano. Você consegue identificar o que pode ter causado isso?",
            "Sentimentos de tristeza podem surgir por diversos fatores. Quer me contar mais sobre o que está acontecendo?",
            "Às vezes a tristeza aparece sem um motivo claro. Como tem sido seu dia hoje?"
        ]
    },

    "ansiedade": {
        "keywords": ["ansioso", "ansiedade", "preocupado", "nervoso", "aflito", "tenso"],
        "responses": [
            "A ansiedade geralmente está ligada a preocupações futuras. Você percebe algum pensamento recorrente te incomodando?",
            "Sentir ansiedade é comum. Você consegue identificar o que está te deixando assim?",
            "Talvez possamos focar no momento presente. O que está passando pela sua mente agora?"
        ]
    },

    "estresse": {
        "keywords": ["estressado", "sobrecarregado", "cansado", "muita pressão", "muito trabalho"],
        "responses": [
            "O estresse pode surgir quando lidamos com muitas demandas. Você sente que está sobrecarregado?",
            "Parece que você está com muita coisa ao mesmo tempo. Como está sua rotina?",
            "Talvez pequenas pausas ao longo do dia possam ajudar. Você tem conseguido descansar?"
        ]
    },

    "baixa_autoestima": {
        "keywords": ["não sou bom", "incapaz", "inseguro", "fracasso", "não consigo"],
        "responses": [
            "Sentimentos de insegurança podem surgir em vários momentos. O que te fez pensar assim?",
            "Às vezes somos muito duros com nós mesmos. Quer me contar mais sobre isso?",
            "Você já passou por desafios antes. O que está te fazendo duvidar agora?"
        ]
    },

    "solidão": {
        "keywords": ["sozinho", "sozinha", "isolado", "ninguém liga", "sem amigos"],
        "responses": [
            "A sensação de solidão pode ser difícil. Você tem alguém com quem costuma conversar?",
            "Mesmo quando parece que estamos sozinhos, existem formas de buscar conexão. Quer falar mais sobre isso?",
            "Você sente falta de conversar com alguém ou de estar mais próximo das pessoas?"
        ]
    },

    "motivacao": {
        "keywords": ["desmotivado", "sem energia", "sem motivação", "cansado de tudo"],
        "responses": [
            "Momentos de desmotivação são comuns. Você percebe quando isso começou?",
            "Às vezes nosso corpo e mente pedem uma pausa. Como está seu descanso?",
            "Pequenos passos podem ajudar. O que você acha que conseguiria fazer hoje, mesmo que seja algo simples?"
        ]
    },

    "raiva": {
        "keywords": ["raiva", "irritado", "irritada", "com ódio", "muita raiva"],
        "responses": [
            "A raiva também é uma emoção válida. Você consegue identificar o que desencadeou isso?",
            "Parece que algo te incomodou bastante. Quer me contar mais sobre o que aconteceu?",
            "Às vezes parar um momento antes de reagir pode ajudar. Como você está lidando com isso agora?"
        ]
    },

    "sono": {
        "keywords": ["não consigo dormir", "insônia", "sono ruim", "acordo muito", "dormindo mal"],
        "responses": [
            "Problemas com o sono podem afetar bastante o bem-estar. Isso tem acontecido com frequência?",
            "Você percebe se algo está te preocupando na hora de dormir?",
            "Criar uma rotina antes de dormir pode ajudar. Como tem sido suas noites?"
        ]
    },

    "mal_hoje": {
        "keywords": ["não me sinto bem", "mal hoje", "não estou bem", "me sinto mal"],
        "responses": [
            "Entendo. Você pode me contar um pouco mais sobre o que vem sentindo?",
            "Sinto muito que esteja assim hoje. Quer compartilhar mais detalhes?",
            "Estou aqui para te ouvir. O que tem passado pela sua cabeça?"
        ]
    }
}

CRITICAL_KEYWORDS = [
    "suicidio", "me matar", "não quero viver", "acabar com tudo",
    "me automachucar", "tirar minha vida", "sumir pra sempre"
]

CRITICAL_RESPONSE = """
Sinto muito por você estar passando por isso. Você não precisa enfrentar isso sozinho.
É muito importante buscar ajuda de um profissional ou alguém de confiança.

Se possível, procure apoio imediato:
- Centro de Valorização da Vida (CVV): 188 (Brasil)
- https://www.cvv.org.br/

Você gostaria de conversar mais sobre o que está sentindo?
"""

SELF_CARE_TIPS = [
    """
Dar o primeiro passo e falar sobre como se sente já é muito importante.

Algumas coisas simples que podem ajudar agora:

- Respire fundo — inspire por 4 segundos, segure por 4, expire por 4
- Se possível, afaste-se por alguns minutos do ambiente atual
- Beba água e tente se sentar confortavelmente

Mas mais do que tudo — o que está te fazendo sentir mal? Falar sobre isso pode ajudar. Estou aqui para te ouvir.
""",

    """
Você está fazendo algo importante ao prestar atenção em como se sente.

Talvez você possa tentar:

- Fazer uma pausa curta e se desconectar por alguns minutos
- Alongar o corpo ou dar uma pequena caminhada
- Ouvir uma música que te acalme

Se quiser, pode me contar mais sobre o que está acontecendo.
""",

    """
Às vezes pequenas ações já ajudam a trazer um pouco mais de equilíbrio.

Você pode tentar agora:

- Organizar um pouco o ambiente ao seu redor
- Tomar um pouco de água ou algo leve
- Respirar devagar e focar no momento presente

Quer me contar o que tem passado pela sua cabeça?
""",

    """
Cuidar de si nesses momentos é essencial.

Algumas ideias simples:

- Diminuir estímulos (menos celular, menos barulho)
- Buscar um lugar mais tranquilo
- Fechar os olhos por alguns instantes e respirar fundo

Se quiser, estou aqui para conversar.
""",

    """
Você não precisa resolver tudo agora.

Talvez ajude:

- Dividir o que está sentindo em partes menores
- Anotar seus pensamentos
- Focar apenas no próximo passo, não em tudo de uma vez

O que você sente que está mais pesado nesse momento?
"""
]

DEFAULT_RESPONSES = [
    "Estou aqui para te ouvir. Quer me contar mais sobre como está se sentindo?",
    "Se quiser, pode compartilhar mais sobre o que está passando.",
    "Pode falar no seu tempo, estou aqui para te escutar.",
    "Às vezes colocar em palavras já ajuda um pouco. Quer tentar me contar?"
]