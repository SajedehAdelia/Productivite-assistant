
````markdown
# Productivity Assistant - AI Planner

A lightweight prototype of a mobile/web application to plan tasks via a chatbot-like interface, featuring automatic task detection based on keywords.

## Main Features
- Simple and intuitive interface
- Automatic task detection through keyword matching
- Clickable calendar with daily task highlights
- Generates a planning based on recognised tasks
- Speech-to-text input (in supported browsers)
- No heavy dependencies, low carbon footprint
- Quickly developed using Python (Flask) + Jinja2

## How to Use
1. Install Flask:
   ```bash
   pip install flask
````

2. Start the application:

   ```bash
   python app.py
   ```
3. Open the app in your browser at `http://127.0.0.1:5000`
4. Type or speak your planning in free-text form.
5. The assistant detects tasks and generates a simple plan on the calendar.

## Examples of Recognised Keywords

* `meeting` → "Meeting scheduled"
* `gym` → "Gym session"
* `study` → "Study time"
* `work` → "Work session"
* `call` → "Call planned"
* `appointment` → "Appointment set"

## 🗣️ Speech-to-Text Support

* You can now **speak** your tasks using the microphone button.
* Uses the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) for in-browser speech recognition.
* **No installation required** — but make sure to use a supported browser.

  * Recommended: Chrome or Microsoft Edge
  * Not supported: Firefox and Safari (as of now)

## Eco-Friendly Reflection

* Minimalistic, lightweight code.
* No unnecessary network calls.
* Simple infrastructure reducing server impact.

## Notes

* This project is an MVP (Minimal Viable Product): the "AI" part is simulated through basic keyword detection.
* Future improvement could integrate a real AI model using NLP APIs (e.g., OpenAI, Huggingface).


