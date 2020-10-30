### pip3 install pade ###
### pip3 install aiohttp ###
### pip3 install eventlet ###
### pip3 install service_identity ###
### pip3 install python-socketio ###
### pip3 install numpy ###
### pip3 install -U scikit-fuzzy ###
### pip3 install pymongo ###
### pip3 install pybluez ###
### pip3 install python-dotenv ###

from pade.misc.utility import display_message, start_loop, call_later
from pade.core.agent import Agent
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID
from pade.behaviours.protocols import TimedBehaviour
from sys import argv
from aiohttp import web
from socket_connecotr import sio
import eventlet
import numpy as np
import skfuzzy as fuzz
import uuid, re
import bluetooth
from database import update_status
import os
from dotenv import load_dotenv

load_dotenv()

### Agente ###
class ComportTemporal(TimedBehaviour):
    def __init__(self, agent, time):
        super(ComportTemporal, self).__init__(agent, time)

    def on_time(self):
        super(ComportTemporal, self).on_time()
        print('Aqui ando')

    def on_start(self):
        super(ComportTemporal, self).on_start()

        # Update database
        update_status(my_id)

        # Socket
        sio.connect(os.getenv('SOCKET_URI'))

class Agente(Agent):
    def __init__(self, aid):
        super(Agent, self).__init__(aid=aid, debug=False)

        comp_temp = ComportTemporal(self, 5.0)

        self.behaviours.append(comp_temp)

        sio.wait()

if __name__ == '__main__':
    # Get ID
    # TODO esta mac address es de Chema, comenatar para tomar la real 
    mac = [os.getenv('CHEMA_MAC')]
    # mac = bluetooth.read_local_bdaddr()
    my_id = int(mac[-1].replace(':', ''), 16)

    # Turn On Agent
    agents_list = list()
    agente = Agente(AID(name=str(my_id)))
    agents_list.append(agente)

    start_loop(agents_list)