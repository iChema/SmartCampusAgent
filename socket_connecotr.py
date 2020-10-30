import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')

@sio.event
def my_message(data):
    #print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.on('hola')
def hola(data):
    print(data)

@sio.event
def disconnect():
    print('disconnected from server')