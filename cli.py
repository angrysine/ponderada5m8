import gradio as gr
import requests
import json




def answer(name):
    answer= requests.post("http://localhost:11434/api/generate",data=json.dumps({'model':'lolzero','prompt':name,"stream":False})).content
    # answer = json.loads(answer)
    answer = answer.decode()
    
    answer = json.loads(answer)
    return answer["response"]

demo = gr.Interface(fn=answer, inputs="text", outputs="text")
    
if __name__ == "__main__":
    demo.launch(show_api=False)   