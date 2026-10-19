🎙️ Edge TTS Studio

A lightweight, mobile-first web application that converts text into highly realistic, natural-sounding speech. Powered by Microsoft's Edge Text-to-Speech (TTS) neural voices and built with Python and Flask.

> **⚠️ Important Note on Hosting:** Microsoft actively blocks datacenter IP addresses (like Render, AWS, or Railway) from using their free Edge TTS API. Therefore, this application is designed to be **run locally** on your own device. It works perfectly on a local PC or via Termux on Android!

---

## 📖 About the Project

**Edge TTS Studio** was designed to provide a fast, free, and clutter-free way to generate audio from text. Whether you are an author wanting to listen to your drafts, a student needing audio for study materials, or a developer testing TTS, this tool gives you access to hundreds of high-quality Microsoft voices without the need for an API key. 

Because the interface is fully responsive, it works perfectly on desktop computers, tablets, and mobile phones.

---

## ✨ Key Features

- **📝 Flexible Text Input:** Paste or type text directly into the editor, or upload a `.txt` file to extract the text automatically.
- **🔍 Smart Voice Search:** Search through hundreds of global voices by name, language, or accent (e.g., `en-US`, `Spanish`, `Jenny`).
- **🎛️ Beginner-Friendly Controls:** No confusing percentages or frequencies. Adjust the speaking **Speed** (Very Slow to Very Fast) and **Pitch** (Deep to High) using simple dropdown menus.
- **🔢 Live Character Count:** Instantly see the length of your text.
- **💾 Instant Audio Generation:** Play the generated speech directly in your browser and download it as a high-quality `.mp3` file with one click.

---

## 🚀 How to Run Locally (Beginner's Guide)

You can run this app on your computer or directly on your Android phone using Termux. 

### Option A: Running on Android (Using Termux)
1. Install **Termux** (from F-Droid).
2. Update packages and install Python: `pkg update && pkg upgrade -y` then `pkg install python -y`
3. Clone this repository: 
   ```bash
   git clone https://github.com/RealmRiser/Edge-TTS-Studio.git
   cd Edge-TTS-Studio
```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Open Chrome on your phone and go to: http://127.0.0.1:5000

Option B: Running on Windows / Mac / Linux

1. Make sure you have Python installed.
2. Clone this repository and navigate into the folder.
3. Install dependencies: pip install -r requirements.txt
4. Run the app: python app.py
5. Open your browser and go to http://127.0.0.1:5000.

---

🛠️ Tech Stack

· Backend: Python, Flask
· TTS Engine: edge-tts (Microsoft Edge's neural TTS API)
· Production Server: Gunicorn (for deployment, if using a VPS)
· Frontend: HTML5, CSS3, Vanilla JavaScript

---

Built with ❤️ by RealmRiser

```

Once you tap that single copy button, just go to GitHub, paste it into your README file, and tap **Commit changes**. It will format perfectly on your GitHub page!
