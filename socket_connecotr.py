import socketio

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    # Get ID
    # TODO esta mac address es de Chema, comenatar para tomar la real 
    mac = ['dc:fb:48:29:94:d7']
    # mac = bluetooth.read_local_bdaddr()
    my_id = int(mac[-1].replace(':', ''), 16)
    sio.emit('joinAgent',{'curp': my_id,'sala':0})

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