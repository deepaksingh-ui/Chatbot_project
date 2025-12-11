# AI Chatbot Final Project (Voice + AI)

This project is a ready-to-run Django + Channels demo with voice input and optional AI replies.

## Features
- Text chat UI and Browser-based voice input (Web Speech API).
- Text-to-speech for bot replies via browser `speechSynthesis` (toggleable).
- Real-time messaging via Django Channels and Daphne (ASGI).
- Messages and conversations stored in PostgreSQL.
- Optional OpenAI integration (set OPENAI_API_KEY) for AI replies. Falls back to deterministic reply when no key present.

## Quick setup (Windows CMD)
1. Create & activate venv:
   ```cmd
   python -m venv venv
   venv\Scripts\activate.bat
   ```
2. Install deps:
   ```cmd
   pip install -r requirements.txt
   pip install -r requirements-ai.txt   # optional, only if you want OpenAI
   ```
3. Start Postgres (Docker):
   ```cmd
   docker-compose up -d
   ```
4. Run migrations & create superuser:
   ```cmd
   set POSTGRES_HOST=localhost
   set DJANGO_SETTINGS_MODULE=chatbot_project.settings
   python manage.py migrate
   python manage.py createsuperuser
   ```
5. Start Daphne (ASGI):
   ```cmd
   set POSTGRES_HOST=localhost
   set DJANGO_SETTINGS_MODULE=chatbot_project.settings
   daphne -b 127.0.0.1 -p 8000 chatbot_project.asgi:application
   ```
6. Open browser `http://127.0.0.1:8000` (Chrome recommended for voice).

## Enabling OpenAI (optional)
1. Install `openai` (requirements-ai.txt)
2. Set environment variable `OPENAI_API_KEY`
3. Restart Daphne. The AI will be used automatically in the consumer.

## Notes
- Browser voice recognition relies on Web Speech API (best supported in Chrome/Edge).
- For production, configure Redis channel layer and secure settings.