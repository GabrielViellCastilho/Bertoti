from modelo_ollama import ollama_chat

def gerar_historia(tema: str) -> str:
    prompt = f"Create a short, creative and engaging story about: {tema}"
    return ollama_chat(prompt)

def gerar_prompts_imagem(historia: str) -> list[str]:
    prompt = f"""Below is a short story. Generate 3 rich and detailed visual prompts that could be turned into images.

Each prompt must describe **both the main characters and the setting** clearly and vividly.

Story:
{historia}

Use vivid descriptions like: 
- 'A young warrior with glowing blue eyes, standing on a cliff overlooking a stormy sea under a blood-red sky.'
- 'An old wizard with a silver beard inside a cozy wooden cabin filled with magical artifacts and candlelight.'"""

    output = ollama_chat(prompt)
    prompts = output.strip().split("\n")
    return [p.strip("- ").strip() for p in prompts if p.strip()]
