from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter as tk
import openai
import os
import requests
from PIL import Image, ImageTk
import base64
window = ThemedTk(theme="equilux")
window.configure(themebg="equilux")
window.resizable(False, False)
window.title("AI 3D Design Generator")
window.geometry("550x800")
client = openai.OpenAI(api_key = 'ENTER YOUR OWN API KEY')
OUTPUT_DIR = "outputs"
cIndex=0
image_paths=[]



def showImage(ind):
    global imagePreview

    img = Image.open(image_paths[ind])
    img = img.resize((400,400), Image.Resampling.LANCZOS)
    imagePreview = ImageTk.PhotoImage(img)
    image_label.config(image=imagePreview)

def nextImg(event=None):
        global cIndex
        if not image_paths:
            return
        cIndex = (cIndex + 1) % len(image_paths)
        showImage(cIndex)

def prevImg(event=None):
        global cIndex
        if not image_paths:
            return
        cIndex = (cIndex - 1) % len(image_paths)
        showImage(cIndex)

def preview_first():
    if image_paths:
        os.starfile(image_paths[0])


def generate_images_from_ideas2(ideas):
    paths = []
    for i in range(len(ideas)):
        img = client.images.generate(
            model="gpt-image-1.5",
            prompt=ideas[i],
            size="1024x1024",
            n=1,
            output_format="jpeg"
        )

        filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")

        b64 = img.data[0].b64_json
        print(b64)
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(b64))

        paths.append(filepath)
    return paths





def download_image(url, filepath):
    img_data = requests.get(url).content
    with open(filepath, "wb") as f:
        f.write(img_data)

def generate_ideas(user_text , n):
    prompt = (
        f"Generate {n} unique , creative ideas for a 3D printable model based on: {user_text}\n"
        f"Return ONLY a numbered list from 1 to {n}. One idea per line."
    )

    resp= client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.9,

    )

    ideas=[]
    for line in resp.choices[0].message.content.splitlines():
        print(line)
        line = line.strip()
        if line != "":
            ideas.append(line)
    return ideas[:n]

def generate_images_from_ideas(ideas):
    paths = []

    for i in range(len(ideas)):
        idea = ideas[i]


        img= client.images.generate(
            model="dall-e-3",
            prompt=idea,
            size="1024x1024",
            n=1
        )

        url= img.data[0].url
        print(url)
        filepath = OUTPUT_DIR + "/request_" + str(1 +1) + ".jpg"
        download_image(url, filepath)
        paths.append(filepath)

    return paths


def process():
    global image_paths, cIndex

    user = entry.get().strip()
    if rb.get()=="Choice1":
        n=1
    else:
        n=2

    ideas= generate_ideas(user, n)
    image_paths= generate_images_from_ideas2(ideas)
    cIndex=0
    showImage(0)



title = ttk.Label(window , text="3D Design Generator",font=("Comfortaa", 24,))
title.place(x=130,y=70)
rb = StringVar(value="Choice5")
rad1 = ttk.Radiobutton(window, text="Short [1 variants]", value="Choice1", variable=rb,)
rad1.place(x=130, y=135)
rad2 = ttk.Radiobutton(window, text="Extended [2 Variants]", value="Choice3", variable=rb,)
rad2.place(x=280, y=135)
entry=ttk.Entry(window,width=50,)
entry.place(x=120,y=240)
preview=ttk.Button(window,text="Preview",command=preview_first())
preview.place(x=130,y=300)
enter=ttk.Button(window,text="Enter",command=process)
enter.place(x=330,y=300)
image_label=Label(window)
image_label.place(x=60,y=350)
window.bind("<Left>", prevImg())
window.bind("<Right>", prevImg())
window.mainloop()