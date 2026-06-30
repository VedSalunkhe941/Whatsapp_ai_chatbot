# 🤖 WhatsApp AI Auto Reply Bot

Automatically read WhatsApp messages from your screen, generate AI responses using OpenAI GPT, and send replies just like a real person.

> ⚠️ **Educational project only.** This project demonstrates desktop automation with Python and AI integration.

---

## ✨ Features

* 📩 Detects the latest incoming WhatsApp message
* 🤖 Generates human-like replies using OpenAI GPT
* 💬 Replies in English, Marathi, or Hinglish
* 🧠 Maintains a natural conversation style
* 🚫 Avoids replying to your own messages
* 🔄 Continuously monitors the chat
* ⚡ Fully automated after starting the script

---

## 🛠️ Tech Stack

| Technology    | Purpose                       |
| ------------- | ----------------------------- |
| Python        | Main programming language     |
| OpenAI API    | AI-generated replies          |
| PyAutoGUI     | Mouse and keyboard automation |
| Pyperclip     | Clipboard access              |
| Regex         | Message extraction            |
| python-dotenv | Environment variables         |

---

## 📁 Project Structure

```text
WhatsApp-AI-Bot/
│
├── chatbot.py          # Main automation script
├── client.py           # OpenAI API integration
├── .env                # API key (not uploaded)
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/WhatsApp-AI-Bot.git
```

### 2. Move into the project folder

```bash
cd WhatsApp-AI-Bot
```

### 3. Create a virtual environment (Recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure the API Key

Create a file named `.env`

```env
OPENAI_API_KEY=your_openai_api_key
```

---

## ▶️ Run the Bot

```bash
python chatbot.py
```

After running:

1. Open WhatsApp Desktop.
2. Switch to the chat you want.
3. The script waits for 3 seconds.
4. It starts reading messages automatically.

---

## ⚙️ How It Works

```text
Start Script
      │
      ▼
Open WhatsApp
      │
      ▼
Select Chat Messages
      │
      ▼
Copy Chat
      │
      ▼
Extract Latest Incoming Message
      │
      ▼
Already Replied?
      │
   Yes │ No
      │
      ▼
Send Message to GPT
      │
      ▼
Receive AI Reply
      │
      ▼
Type Reply
      │
      ▼
Press Enter
      │
      ▼
Repeat
```

---

## 📍 Screen Coordinates

The script uses screen coordinates.

Update these values according to your screen resolution.

```python
pyautogui.click(...)
pyautogui.moveTo(...)
pyautogui.dragTo(...)
```

To find coordinates:

```python
import pyautogui

while True:
    print(pyautogui.position())
```

---

## 🎭 Customizing the AI

The personality is defined in `client.py`.

You can modify the system prompt to make the bot:

* Friendly
* Funny
* Professional
* Marathi
* Hinglish
* Formal
* Casual

---

## 📦 Dependencies

```
openai
python-dotenv
pyautogui
pyperclip
```

or simply install everything with:

```bash
pip install -r requirements.txt
```

---

## 💡 Future Improvements

* Support multiple chats
* GUI using Tkinter or CustomTkinter
* Remember previous conversations
* OCR instead of selecting text
* Better duplicate message detection
* Media message support
* Voice message transcription
* Emoji reactions
* Logging system

---

## ⚠️ Disclaimer

This project is created for educational purposes to learn Python automation and AI integration.

Use it responsibly. Automating interactions on messaging platforms may violate their terms of service. You are responsible for how you use this project.

---

## 👨‍💻 Author

**Ved Salunkhe**

Computer Engineering Student

Interested in AI, Automation, Python, Cybersecurity, and Backend Development.

⭐ If you found this project helpful, consider giving it a star!
