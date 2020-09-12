### pip3 install pade ###
### pip3 install aiohttp ###
### pip3 install eventlet ###
### pip3 install service_identity ###
### pip3 install python-socketio ###
### pip3 install numpy ###
### pip3 install -U scikit-fuzzy ###

from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from sys import argv
from aiohttp import web
import eventlet
import socketio
import numpy as np
import skfuzzy as fuzz

### Agente ###
class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        var = num + 136
        mensaje = '¡Estoy escuchando!'
        print(mensaje)
        #display_message('Agente_1', '¡Estoy escuchando!')
        #my_message('Hola soy el Agente.')

class AgenteHelloWorld(Agent):
    def __init__(self, aid):
        super(AgenteHelloWorld, self).__init__(aid=aid, debug=False)
        comp_temp = ComportTemporal(self, 1.0)
        self.behaviours.append(comp_temp)
        sio.wait()

class HelloAgent(Agent):
    def __init__(self, aid):
        super(HelloAgent, self).__init__(aid=aid, debug=False)

    def on_start(self):
        super(HelloAgent,self).on_start()
        #self.call_later(10.0, self.say_hello)
        sio.connect('http://localhost:3000')

    def say_hello(self):
        display_message(self.aid.localname, "Hello, I\'m an agent!")

### Socket ###
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

if __name__ == '__main__':

    agents = list()

    num = 133
    agente_hello = AgenteHelloWorld(AID(name='Agent2'))
    hello_agent = HelloAgent(AID(name='Agent'))
    agents.append(hello_agent)
    agents.append(agente_hello)

    start_loop(agents)