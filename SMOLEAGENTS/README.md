# ✨ Gerador Criativo de Histórias e Imagens com IA

Este projeto usa **modelos de linguagem (LLM)** e **geração de imagem com difusão** para criar histórias com base em um tema e gerar imagens incríveis a partir de descrições extraídas dessas histórias.

## 📌 Funcionalidades

- Geração automática de histórias criativas com base em um tema.
- Geração de prompts visuais detalhados a partir da história.
- Geração de imagens realistas com base nos prompts.
- Interface amigável com Gradio.

---

## ⚙️ Tecnologias Utilizadas

- 🧠 [Ollama](https://ollama.com) — para gerar histórias e prompts usando LLMs locais (ex: `qwen2.5:3b`)
- 🎨 [Diffusers + Stable Diffusion](https://github.com/huggingface/diffusers) — para gerar imagens a partir de texto
- 🚀 [Gradio](https://www.gradio.app) — para a interface interativa
- 🐍 Python 3.10+

---

## 📂 Estrutura do Projeto

```bash
.
├── app.py                # Arquivo principal que inicia a interface Gradio
├── historia.py           # Funções de geração de história e prompts com LLM
├── imagem.py             # Geração de imagem com Stable Diffusion
├── requirements.txt      # Dependências do projeto
├── outputs/              # Pasta onde as imagens geradas são salvas
└── README.md             # Este arquivo
└── .gitignore            # Ignora arquivos de cache
```

## 🔧 Como Executar o Projeto
### 1. Clone o repositório

```bash

git clone https://github.com/GabrielViellCastilho/Bertoti.git
cd BERTOTI/SMOLEAGENTS
```

### 2. Crie e ative um ambiente virtual (opcional, mas recomendado)

```bash

python -m venv venv
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

### 3. Instale as dependências

```bash

pip install -r requirements.txt
```

### 4. Verifique se o modelo do Ollama está instalado
Certifique-se de que o Ollama está instalado e rodando localmente, com o modelo usado no projeto (por padrão: qwen2.5:3b):

 ```bash

ollama run qwen2.5:3b
```
### 5. Execute o projeto

```bash

python app.py
```
A interface será aberta em http://127.0.0.1:7860.


📎 Exemplo de Uso
Digite um tema como: Um dragão que protege uma aldeia

Clique em "🔮 Gerar História e Prompts"

Visualize a história e os prompts.

Clique em um dos botões "🖼️ Gerar Imagem" para criar a imagem correspondente.

📁 Saída
As imagens geradas são salvas automaticamente na pasta outputs/.
