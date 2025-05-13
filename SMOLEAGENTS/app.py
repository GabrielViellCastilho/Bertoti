import gradio as gr
from historia import gerar_historia, gerar_prompts_imagem
from imagem import gerar_imagem

def gerar_historia_interface(tema):
    historia = gerar_historia(tema)
    prompts = gerar_prompts_imagem(historia)
    return historia, prompts[0], prompts[1], prompts[2]

with gr.Blocks(title="Gerador Criativo com IA") as demo:
    gr.Markdown("# ✨ Gerador Criativo de Histórias e Imagens com IA")
    gr.Markdown("Digite um tema, gere uma história e visualize imagens baseadas nela!")

    with gr.Row():
        tema_input = gr.Textbox(label="📝 Tema da História", placeholder="Ex: Um dragão que protege uma aldeia")

    gerar_btn = gr.Button("🔮 Gerar História e Prompts")

    historia_output = gr.Textbox(label="📖 História Gerada")
    prompt1 = gr.Textbox(label="🎨 Prompt de Imagem 1")
    prompt2 = gr.Textbox(label="🎨 Prompt de Imagem 2")
    prompt3 = gr.Textbox(label="🎨 Prompt de Imagem 3")

    with gr.Row():
        gerar_img1 = gr.Button("🖼️ Gerar Imagem 1")
        gerar_img2 = gr.Button("🖼️ Gerar Imagem 2")
        gerar_img3 = gr.Button("🖼️ Gerar Imagem 3")

    imagem_output = gr.Image(label="📷 Imagem Gerada")

    gerar_btn.click(
        fn=gerar_historia_interface,
        inputs=tema_input,
        outputs=[historia_output, prompt1, prompt2, prompt3]
    )

    gerar_img1.click(fn=gerar_imagem, inputs=prompt1, outputs=imagem_output)
    gerar_img2.click(fn=gerar_imagem, inputs=prompt2, outputs=imagem_output)
    gerar_img3.click(fn=gerar_imagem, inputs=prompt3, outputs=imagem_output)

demo.launch()
