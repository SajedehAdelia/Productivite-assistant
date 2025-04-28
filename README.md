### 📄 README.md (English Version)

```markdown
# Productivity Assistant - AI Planner

A lightweight prototype of a mobile/web application to plan tasks via a chatbot-like interface, featuring automatic task detection based on keywords.

## Main Features
- Simple and intuitive interface
- Automatic task detection through keyword matching
- Generates a planning based on recognised tasks
- No heavy dependencies, low carbon footprint
- Quickly developed using Python (Flask) + Jinja2

## How to Use
1. Install Flask:
   ```bash
   pip install flask
   ```
2. Start the application:
   ```bash
   python app.py
   ```
3. Open the app in your browser at `http://127.0.0.1:5000`
4. Type your planning in free-text form.
5. The assistant detects tasks and generates a simple plan.

## Examples of Recognised Keywords
- meeting → "Meeting scheduled"
- gym → "Gym session"
- study → "Study time"
- work → "Work session"
- call → "Call planned"
- appointment → "Appointment set"

## Eco-Friendly Reflection
- Minimalistic, lightweight code.
- No unnecessary network calls.
- Simple infrastructure reducing server impact.

## Notes
- This project is an MVP (Minimal Viable Product): the "AI" part is simulated through basic keyword detection.
- Future improvement could integrate a real AI model using NLP APIs (e.g., OpenAI, Huggingface).

---
