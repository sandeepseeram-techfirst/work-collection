import socketIO
from .models import Cryptocurrency 
import json

sio = socketIO.Server()

@sio.event
def connect():
    print('Client connected!')
 
@sio.event
def disconnect():
    print('Client disconnected!')

@sio.event
def message(message):
    try:
        data = json.loads(message)
        if data['type'] == 'price':
            symbol = data['symbol']
            price = data['price']
            cryptocurrency = Cryptocurrency.objects.get(symbol=symbol)
            cryptocurrency.price = price
            cryptocurrency.save() 
            sio.emit('price', {'symbol': symbol, 'price': price})
    except Exception as e:
        print(e)

if __name__ == '__main__':
    sio.run(server=True)