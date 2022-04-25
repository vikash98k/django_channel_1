from django.urls import path
from . import consumers


websocket_urlpatterns = [
	path('ws/',consumers.Calculator.as_asgi()),
	#path('ac/',consumers.MyAsyncConsumer.as_asgi()) 
]