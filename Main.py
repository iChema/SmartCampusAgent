import threading
import RPi.GPIO as GPIO
import LogicaDifusa as ld
import SensorLuz as sl
import Sensores as sen
from datetime import datetime
from decimal import Decimal

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16, GPIO.IN)  # PIR motion sensor data


def hay_alguien():
    luz = 0
    intensidad = 20
    #print(datetime.now().second)
    if GPIO.input(16) == 1:
        #print ("Hay alguien")
        luz = sl.main()
        #print("Intencidad de luz: ", luz, "lux")
        if Decimal(luz) > 30:
            luz = 30
        intensidad = ld.fuzzificaton(datetime.now().hour+datetime.now().minute/60, luz)
        #print("Milisegundos de onda: ", intensidad)
        on_off=True
        sen.onOff(str(intensidad))    
    else:
        #print("No hay nadie")
        on_off=False
        sen.onOff("OFF")    
    return sen.main(), luz, intensidad, on_off

    #print(sen.main())
    #print("Intencidad de luz: ", luz, "lux")
    #print("Milisegundos de onda: ", intensidad)

'''



    
        if 1 == 1:  # GPIO.input(16) == 1:
            #print ("Hay alguien")
            luz = sl.main()
            #print("Intencidad de luz: ", luz, "lux")
            if Decimal(luz) > 20:
                luz = 20
            #intensidad = ld.fuzzificaton(datetime.now().hour+datetime.now().minute/60, luz)
            #print("Milisegundos de onda: ", intensidad)
            #GPIO.output(11, 1)
            tiempo_de_espera = 1
        else:
            #print("No hay nadie")
            #GPIO.output(11, 0)
            if tiempo_de_espera == 1:
                time.sleep(10)
                tiempo_de_espera = 0
        if (time.time() - seguntos_incial) >= 5:
            luz = sl.main()
            #print("Intencidad de luz: ", luz, "lux")
            if Decimal(luz) > 20:
                luz = 20
            #intensidad = ld.fuzzificaton( datetime.now().hour+datetime.now().minute/60, luz)
            seguntos_incial = time.time()
            #print("Milisegundos de onda: ", intensidad)











import LogicaDifusa as ld
import SensorLuz as sl
import SensorPresencia as sp
import time
from datetime import datetime

while True:
    if(sp.presencia()==1):
        now = datetime.now()
        luz = sl.main()
        print(luz)
        print(ld.fuzzificaton(now.hour+now.minute/60, luz))
    time.sleep(1.0)

'''
