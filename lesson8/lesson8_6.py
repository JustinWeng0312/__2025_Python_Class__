import gradio as gr

from google import genai
client = genai.Client()

#建立gradio Blocks架構
with gr.Blocks() as demo:
    gr.Markdown("## 公司內部機器人")
    
    #建立輸入框
    input_text = gr.Textbox(label="請輸入您的問題", placeholder="在此輸入...",submit_btn=True)

    #建立gradio.According
    with gr.Accordion("懶得輸入可以點選以下問題", open=True):
        gr.Examples(
            examples=[
                "請問台灣的首都是哪裡？",
                "請問台灣的國土面積有多大?",
                "請問台灣的的人口有多少?",
                "請問台灣的主要產業是什麼?",
                "請問台灣的官方語言是什麼?"
            ],
            inputs=input_text,
        )

    #建立輸出框
    output_text = gr.Textbox(
        label="機器人回覆", 
        placeholder="機器人會在這裡回覆你", 
        interactive=False)

    @input_text.submit(inputs=[input_text], outputs=[output_text])
    def respond_to_query(message):
        # 在這裡處理用戶的問題並生成機器人的回覆
        response = client.models.generate_content(
          model="gemini-2.5-flash",
          contents=[message]
        )
        return response.text

demo.launch()
