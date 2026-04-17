# mental_health_mcp
This repository is intended for sending the necessary materials to configure the mental health MCP.

## Como utilizar o projeto com Claude (Windows)

### 1. Instalar o Claude Desktop

1. Acesse o site oficial da Anthropic:
   https://claude.ai/download

2. Baixe a versão para **Windows**

3. Instale normalmente e abra o aplicativo

---

### 2. Configurar o MCP (Model Context Protocol)

O Claude Desktop permite integrar ferramentas externas via MCP.

#### Local do arquivo de configuração:

No Windows, o arquivo fica em:

```
C:\Users\SEU_USUARIO\AppData\Roaming\Claude\claude_desktop_config.json
```

Se não existir, você pode criar o arquivo manualmente.

---

### 3. Adicionar o servidor MCP

Abra o arquivo `claude_desktop_config.json` e adicione:

```json
{
  "mcpServers": {
    "Mental Health MCP": {
      "command": "node",
      "args": ["C:\\caminho\\para\\seu\\projeto\\server.js"]
    }
  }
}
```

Substitua:

```
C:\\caminho\\para\\seu\\projeto\\server.js
```

pelo caminho real onde está o arquivo `server.js`.

---

### 4. Subir os serviços

Antes de usar no Claude, é necessário iniciar:

#### 🔹 Backend (FastAPI)

No terminal:

```bash
cd mental_health_mcp
source venv/bin/activate  # ou venv\Scripts\activate no Windows
uvicorn main:app --reload
```

---

#### 🔹 Expor API com ngrok

```bash
ngrok http 8000
```

Copie a URL gerada (exemplo: https://xxxx.ngrok-free.dev)

---

#### 🔹 Atualizar o server.js

No arquivo `server.js`, atualize a URL da API:

```javascript
const API_URL = "https://xxxx.ngrok-free.dev/chat";
```

---

####  Iniciar MCP Server

```bash
node server.js
```

---

### 5. Usar no Claude

1. Abra o Claude Desktop
2. Vá em **Settings (Configurações)**
3. Acesse a seção **Developer / MCP**
4. Verifique se o servidor aparece como ativo
5. Ao iniciar uma conversa, utilize o botão **"+"** para acessar a tool

---

###  Aviso importante

Este sistema foi projetado com limitações intencionais para evitar riscos éticos,
não realizando diagnósticos ou recomendações clínicas.

Ele atua apenas como um assistente de apoio emocional e não substitui acompanhamento profissional.

---

### Observações

* O sistema utiliza uma base de conhecimento em Python
* As respostas são baseadas em palavras-chave e regras definidas
* O Claude atua como interface conversacional utilizando MCP

---

###  Pronto!

Após esses passos, o Claude estará integrado ao seu servidor MCP e poderá utilizar sua API de apoio emocional.


Arquitetura desenvolvida:
## Arquitetura do Sistema

O projeto é composto por três camadas principais:

### 1. API em Python (FastAPI)

A API foi desenvolvida utilizando o framework FastAPI e é responsável por:

* Receber a mensagem do usuário
* Processar o texto (normalização e análise)
* Consultar a base de conhecimento (`knowledge_base.py`)
* Identificar possíveis padrões emocionais
* Retornar uma resposta estruturada com:

  * mensagem de apoio
  * sugestões de autocuidado
  * nível de risco
  * aviso ético

#### 📍 Endpoint principal:

```http
POST /chat
```

####  Exemplo de requisição:

```json
{
  "message": "Não me sinto bem hoje"
}
```

#### Exemplo de resposta:

```json
{
  "response": "Entendo. Você pode me contar um pouco mais sobre o que vem sentindo?\n\n[...]",
  "risk_level": "low"
}
```

A lógica da API é baseada em regras e palavras-chave, garantindo previsibilidade e controle das respostas.

---

### 2. Base de Conhecimento (knowledge_base.py)

A base de conhecimento contém:

* Categorias emocionais (ex: ansiedade, tristeza, estresse)
* Palavras-chave associadas
* Respostas pré-definidas
* Sugestões de autocuidado
* Palavras críticas (para detecção de risco elevado)

Essa estrutura permite que o sistema funcione sem depender de modelos externos, utilizando lógica determinística.

---

### 3. Servidor MCP (Node.js)

O servidor MCP funciona como um intermediário entre o Claude e a API em Python.

####  Responsabilidades:

* Receber chamadas do Claude (via MCP)
* Encaminhar requisições para a API FastAPI
* Retornar a resposta da API para o Claude

####  Fluxo:

1. Usuário envia mensagem no Claude
2. Claude aciona a tool via MCP
3. MCP (Node.js) envia requisição HTTP para a API Python
4. API processa e retorna resposta
5. MCP devolve o resultado ao Claude
6. Claude exibe a resposta ao usuário

---

### 4. Exposição da API (ngrok)

Como o Claude não acessa `localhost`, foi utilizado o ngrok para expor a API:

```bash
ngrok http 8000
```

Isso gera uma URL pública que é utilizada pelo servidor MCP.

---

### Fluxo Completo do Sistema

```text
Usuário → Claude → MCP (Node.js) → API (FastAPI) → Base de Conhecimento
                                             ↓
                                      Resposta estruturada
                                             ↓
Usuário recebe resposta no Claude
```

---

###  Considerações Técnicas

* O sistema não utiliza inteligência artificial generativa para decisões clínicas
* Toda a lógica é baseada em regras controladas
* O Claude atua apenas como interface conversacional
* O MCP permite integração segura entre o modelo e sistemas externos

---

### Objetivo da Arquitetura

Garantir:

* controle das respostas
* segurança ética
* facilidade de manutenção
* integração com ferramentas modernas (MCP + LLMs)

