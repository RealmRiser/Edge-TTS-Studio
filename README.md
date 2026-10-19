# 🎙️ Edge TTS Studio

A lightweight, mobile-first web application that converts text into highly realistic, natural-sounding speech. Powered by Microsoft's Edge Text-to-Speech (TTS) neural voices and built with Python and Flask.

🚀 **[Launch the Live Web App](https://edge-tts-studio-npf7.onrender.com/)**

---

## 📖 About the Project

**Edge TTS Studio** was designed to provide a fast, free, and clutter-free way to generate audio from text. Whether you are an author wanting to listen to your drafts, a student needing audio for study materials, or a developer testing TTS, this tool gives you access to hundreds of high-quality Microsoft voices without the need for an API key. 

Because the interface is fully responsive, it works perfectly on desktop computers, tablets, and mobile phones.

---

## ✨ Key Features

- **📝 Flexible Text Input:** Paste or type text directly into the editor, or upload a `.txt` file to extract the text automatically.
- **🔍 Smart Voice Search:** Search through hundreds of global voices by name, language, or accent (e.g., `en-US`, `Spanish`, `Jenny`).
- **🎛️ Beginner-Friendly Controls:** No confusing percentages or frequencies. Adjust the speaking **Speed** (Very Slow to Very Fast) and **Pitch** (Deep to High) using simple dropdown menus.
- **🔢 Live Character Count:** Instantly see the length of your text to ensure it fits within standard limits.
- **💾 Instant Audio Generation:** Play the generated speech directly in your browser and download it as a high-quality `.mp3` file with one click.

---

## 🚀 How to Use (Beginner's Guide)

1. **Open the App:** Click the [Live Web App](https://edge-tts-studio-npf7.onrender.com/) link at the top of this page.
   > ⏳ *Note: Because this app is hosted on a free cloud server, it goes to "sleep" when not in use. **The very first time you click the link, it may take 30-50 seconds to load.** Please be patient while the server wakes up!*
2. **Enter Your Text:** Type in the text box, or click **"Choose file"** to upload a `.txt` document.
3. **Find a Voice:** Use the search bar to find a voice. For example, type `US` for American English, or `UK` for British English. Select the voice you like from the list.
4. **Adjust the Tone:** Use the dropdowns to change the speed and pitch if you want the voice to sound faster, slower, deeper, or higher.
5. **Generate:** Click **"🎬 Generate Speech"** and wait a few seconds.
6. **Download:** Once the audio player appears, click **"💾 Download MP3"** to save it to your device.

---

## 🛠️ Tech Stack & Local Development

If you are a developer and want to run this project locally or self-host it, here is how it is built:

- **Backend:** Python, Flask
- **TTS Engine:** `edge-tts` (Microsoft Edge's neural TTS API)
- **Production Server:** Gunicorn
- **Frontend:** HTML5, CSS3, Vanilla JavaScript

### Running Locally

1. Clone the repository:
   ```bash
   git clone https://github.com/RealmRiser/Edge-TTS-Studio.git
cd Edge-TTS-Studio
   cd Edge-TTS-Studio
