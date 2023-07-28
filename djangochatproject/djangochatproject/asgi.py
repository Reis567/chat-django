import os
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import rooms.routing

# Define a configuração de ambiente para o projeto
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangochatproject.settings')

# Criação da aplicação Channels para lidar com diferentes protocolos
application = ProtocolTypeRouter({
    # Quando uma conexão HTTP é estabelecida, a aplicação Django padrão é usada para lidar com as solicitações
    "http": get_asgi_application(),
    
    # Quando uma conexão WebSocket é estabelecida, o middleware de autenticação é aplicado antes do roteamento
    "websocket": AuthMiddlewareStack(
        
        # O roteamento do WebSocket é feito utilizando as URLs definidas no módulo 'rooms.routing'
        URLRouter(
            rooms.routing.websocket_urlpatterns
        )
    )
})