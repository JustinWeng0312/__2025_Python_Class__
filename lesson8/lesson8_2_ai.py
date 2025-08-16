# 建立一個gradio的Block的架構
# 功能:
# 1. 輸入姓名輸入框
# 2. 輸出結果顯示框
# 3. 建立按鈕

import gradio as gr

def greet(name):
    return "你好，" + name + "！歡迎使用 Gradio！"

with gr.Blocks() as demo:
    name_textbox = gr.Textbox(label="姓名", placeholder="請輸入姓名")
    output_textbox = gr.Textbox(label="輸出", placeholder="輸出結果會顯示在這裡")
    greet_button = gr.Button("打招呼")
    
    greet_button.click(fn=greet, 
                       inputs=[name_textbox], 
                       outputs=[output_textbox])    
demo.launch()

# 這段程式碼建立了一個簡單的Gradio應用程式，使用者可以輸入姓名並點擊按鈕來獲得打招呼的回應。
# 這個應用程式使用了Gradio的Block架構來組織界面元素。
# 這段程式碼可以直接在Python環境中執行，並啟動一個本地的Gradio伺服器。