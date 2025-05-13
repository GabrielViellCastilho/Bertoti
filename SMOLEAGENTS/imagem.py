from diffusers import StableDiffusionPipeline
import torch
import uuid
import os

# Criar pasta outputs se não existir
OUTPUT_DIR = "outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

print("⏳ Carregando modelo de imagem...")
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", 
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)
pipe = pipe.to("cuda" if torch.cuda.is_available() else "cpu")
print("✅ Modelo de imagem carregado.")

def gerar_imagem(prompt: str):
    print(f"\n🖼️ Gerando imagem com prompt:\n{prompt}\n")
    image = pipe(prompt).images[0]
    filename = f"{uuid.uuid4().hex[:8]}.png"
    filepath = os.path.join(OUTPUT_DIR, filename)
    image.save(filepath)
    print(f"✅ Imagem salva como: {filepath}")
    return filepath
