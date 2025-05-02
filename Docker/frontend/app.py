import gradio as gr
import requests
import os

BACKEND_HOST = os.getenv("BACKEND_HOST_URL", "http://localhost:8000")

BACKEND_URL = BACKEND_HOST  # Service name in Docker Compose

def create_item(id, name, description):
    payload = {"id": int(id), "name": name, "description": description}
    r = requests.post(f"{BACKEND_URL}/items/", json=payload)
    return r.json() if r.ok else r.text

def get_all_items():
    r = requests.get(f"{BACKEND_URL}/items/")
    return r.json() if r.ok else r.text

def get_item_by_id(id):
    r = requests.get(f"{BACKEND_URL}/items/{int(id)}")
    return r.json() if r.ok else r.text

def delete_item(id):
    r = requests.delete(f"{BACKEND_URL}/items/{int(id)}")
    return r.json() if r.ok else r.text

with gr.Blocks() as demo:
    gr.Markdown("# SIMPLE UI FOR ITEM MANAGEMENT")
    
    with gr.Tab("Create"):
        id_in, name_in, desc_in = gr.Number(label="ID"), gr.Text(label="Item"), gr.Text(label="Description")
        btn = gr.Button("Create Item")
        out = gr.Textbox(label="Output")
        btn.click(create_item, [id_in, name_in, desc_in], out)

    with gr.Tab("Fetch All"):
        btn = gr.Button("Get All Items")
        out = gr.Textbox(label="Output")
        btn.click(get_all_items, outputs=out)

    with gr.Tab("Get by ID"):
        id = gr.Number(label="ID")
        btn = gr.Button("Get")
        out = gr.Textbox(label="Output")
        btn.click(get_item_by_id, inputs=id, outputs=out)

    with gr.Tab("Delete"):
        id = gr.Number(label="ID")
        btn = gr.Button("Delete")
        out = gr.Textbox(label="Output")
        btn.click(delete_item, inputs=id, outputs=out)

demo.launch(server_name="0.0.0.0", server_port=7860)

