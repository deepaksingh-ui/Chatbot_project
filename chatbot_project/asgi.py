import os

# 1) make sure settings env var is set first
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "chatbot_project.settings")

# 2) initialize Django apps BEFORE importing anything that may touch models
import django
django.setup()

# 3) now import ASGI helpers and app-level routing
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# import your routing (should NOT import models at module-level)
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})
