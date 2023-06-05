# mysite/routing.py
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import kfapp.urls

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    "http": get_asgi_application(),
    'websocket': AuthMiddlewareStack(
        URLRouter(
            kfapp.urls.websocket_urlpatterns
        )
    ),
})
