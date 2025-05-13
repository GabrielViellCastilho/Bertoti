import ollama

def ollama_chat(prompt, model="qwen2.5:3b"):
    print(f"\n🔹 Prompt enviado ao modelo:\n{prompt}\n")
    response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
    print(f"🔸 Resposta recebida:\n{response['message']['content']}\n")
    return response["message"]["content"]
