

# 🌟 AI 3D Design Generator  
### _Turn tiny ideas into huge 3D creations — instantly!_

Welcome to the **AI 3D Design Generator**, a Tkinter-powered desktop app that transforms your text prompts into **beautiful, high‑resolution 3D-style images** using OpenAI’s image models.  
Type a word. Pick a mode. Boom — your idea becomes art.

This project is perfect for:
- Makers & 3D printing fans  
- Designers looking for inspiration  
- Students building cool AI apps  
- Anyone who wants to see “stars” turn into… well, actual stars ✨

---

## 🚀 Features
### 🎨 AI‑Powered 3D Idea Generation  
Give the app a word or phrase — it generates **1 or 2 creative 3D model ideas** using a chat model.

### 🖼️ High‑Quality Image Generation  
Each idea is turned into a **1024×1024** image using OpenAI’s image API.

### 🧭 Built‑In Image Viewer  
Navigate your generated images with:
- **Left / Right arrow keys**
- **Next / Previous buttons**
- Auto‑resized previews for a clean UI

### 💾 Automatic Saving  
All images are saved into an `outputs/` folder so you can keep or print them later.

### 🖥️ Clean, Dark‑Themed UI  
Powered by **ttkthemes** with the “Equilux” theme for a modern, professional look.

---

## 🛠️ Installation

### 1. Clone the repo  
```bash
git clone https://https://github.com/ThanosKatsifis/Ai3dImageGenerator.git
cd ai-3d-design-generator
```

### 2. Install dependencies  
```bash
pip install openai pillow requests ttkthemes
```

### 3. Add your API key  
Set your OpenAI API key as an environment variable:

**Windows PowerShell**
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**macOS / Linux**
```bash
export OPENAI_API_KEY="your_api_key_here"
```

### 4. Run the app  
```bash
python app.py
```

---

## 🧩 How It Works (Simple Version)

1. You type something like:  
   **“stars”**  
2. The app asks the AI for **creative 3D model ideas**.  
3. Each idea is sent to the image generator.  
4. Images are saved + displayed in the preview window.  
5. You scroll through them like a mini gallery.

---

## 📁 Project Structure
```
.
├── app.py
├── outputs/
└── README.md
```

---

## 🐞 Common Fixes & Improvements

### ❗ Buttons not working?
Make sure you pass the function **without parentheses**:
```python
preview = ttk.Button(window, text="Preview", command=preview_first)
```

### ❗ Arrow keys not switching images?
Same thing — no parentheses:
```python
window.bind("<Left>", prevImg)
window.bind("<Right>", nextImg)
```

### ❗ File opening on Windows?
Use:
```python
os.startfile(image_paths[0])
```

### ❗ Wrong filename?
Fix:
```python
filepath = os.path.join(OUTPUT_DIR, f"request_{i+1}.jpg")
```

---

## ✨ Future Ideas (Feel free to steal these)
- Add a loading animation  
- Add a “Surprise Me” random prompt button  
- Add a gallery grid view  
- Add export-to-PDF or export-to-3D-model (ambitious but fun)

---

## 🤝 Contributing
Pull requests are welcome!  
If you have ideas, improvements, or bug fixes, open an issue and let’s build something awesome together.

---

## 📜 License
No Licence


