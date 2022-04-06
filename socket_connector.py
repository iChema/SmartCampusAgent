import socketio
import bluetooth

sio = socketio.Client()

@sio.event
def connect():
    print('connection established')
    # Get ID
    # TODO esta mac address es de Chema, comenatar para tomar la real 
    #mac = ['dc:fb:48:29:94:d7']
    mac = bluetooth.read_local_bdaddr()
    my_id = int(mac[-1].replace(':', ''), 16)
    sio.emit('joinAgent',my_id)

@sio.event
def my_message(data):
    #print('message received with ', data)
    sio.emit('my response', {'response': 'my response'})

@sio.event
def updateSensores():
    sio.emit('getAgents')

@sio.event
def disconnect():
    print('disconnected from server')