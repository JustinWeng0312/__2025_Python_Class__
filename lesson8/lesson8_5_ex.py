import gradio as gr

with gr.Blocks() as demo: 
    a = gr.Number(label="數字輸入", value=0)
    b = gr.Number(label="數字輸入", value=0)
 
    with gr.Row():
        c_add = gr.Number(label="加法", value=0)
        c_sub = gr.Number(label="減法", value=0)
        c_mul = gr.Number(label="乘法", value=0)
        c_div = gr.Number(label="除法", value=0)

    result_button = gr.Button("加/減/乘/除法")
       
    @result_button.click(inputs=[a, b], outputs=[c_add,c_sub,c_mul,c_div])
    def result_numbers(a, b):
        return a + b, a - b, a * b, a / b

demo.launch()
