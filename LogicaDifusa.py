import numpy as np
import skfuzzy as fuzz

# Generar variables del universo
#   Rango de horas es de 0 a 24, rango de luz solar es de 0 a 10
#   Corriente de salida en voltaje es de 20 a 80
x_time = np.arange(0, 25, 1)
x_light = np.arange(0, 31, 1)
x_current = np.arange(20, 81, 1)

def defuzzified(aggregated):
    # Calcular el resultado defuzzificado
    current = fuzz.defuzz(x_current, aggregated, 'centroid')
    return current

def fuzzificaton(val1,val2):
    # print(val1)
    # print(val2)
    # Generar funciones de membresía difusas
    time_lo = fuzz.trimf(x_time, [0, 0, 10])
    time_md = fuzz.trimf(x_time, [8, 12, 16])
    time_hi = fuzz.trimf(x_time, [14, 24, 24])

    light_lo = fuzz.trimf(x_light, [0, 0, 10])
    light_md = fuzz.trimf(x_light, [0, 10, 30])
    light_hi = fuzz.trimf(x_light, [20, 30, 30])

    current_lo = fuzz.trimf(x_current, [20, 30, 40])
    current_md = fuzz.trimf(x_current, [40, 50, 60])
    current_hi = fuzz.trimf(x_current, [60, 70, 80])
    

    # Necesitamos la activación de nuestras funciones de membresía borrosa en estos valores.
    # Los valores exactos val1 y val2 no existen en nuestros universos...
    # ¡Esto es para lo que existe la membresía fuzz.interp_membership!

    time_level_lo = fuzz.interp_membership(x_time, time_lo, val1)
    time_level_md = fuzz.interp_membership(x_time, time_md, val1)
    time_level_hi = fuzz.interp_membership(x_time, time_hi, val1)

    light_level_lo = fuzz.interp_membership(x_light, light_lo, val2)
    light_level_md = fuzz.interp_membership(x_light, light_md, val2)
    light_level_hi = fuzz.interp_membership(x_light, light_hi, val2)
    
    #Reglas
    current_activation_hi = np.fmin(light_level_lo, current_hi)

    active_rule2 = np.fmin(light_level_hi, time_level_lo) 
    active_rule3 = np.fmin(light_level_hi, time_level_hi)    
    active_rule4 = np.fmax(light_level_md, np.fmax(active_rule2,active_rule3))  

    current_activation_md = np.fmin(active_rule4, current_md)

    
    active_rule5 = np.fmin(light_level_lo, time_level_md)    
    active_rule6 = np.fmax(light_level_hi, active_rule5)
    current_activation_lo = np.fmin(active_rule6, current_lo)
    
    aggregated = np.fmax(current_activation_hi, np.fmax(current_activation_md,current_activation_lo))
    return defuzzified(aggregated)

#Datos de entrada
#print(fuzzificaton(7, 2))