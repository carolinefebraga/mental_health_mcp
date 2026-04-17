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

### ⚠️ Aviso importante

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
