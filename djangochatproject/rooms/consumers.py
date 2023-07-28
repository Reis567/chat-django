import json
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from asgiref.sync import sync_to_async

class ChatConsumer(AsyncJsonWebsocketConsumer):
    async def conect(self):
        # Captura o parâmetro 'room_name' da rota da URL
        self.room_name = self.scope['url_route']['kwargs']['room_name']

        # Define o nome do grupo associado à sala usando o prefixo 'chat_'
        self.room_group_name = 'chat_%s' % self.room_name

        # Adiciona o consumidor ao grupo de canais associado à sala específica
        await self.channel_layer.group_add(
            self.room_name,
            self.room_group_name
        )

        # Aceita a conexão do WebSocket
        await self.accept()

    async def disconnect(self):
        # Remove o consumidor do grupo de canais associado à sala específica
        await self.channel_layer.group_discard(
            self.room_name,
            self.room_group_name
        )
