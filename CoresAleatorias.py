#!/usr/bin/python

# Autor: Felipe Ferreira

# Cores aleatorias com Raspberry utilizando PWM e led RGB

import RPi.GPIO as GPIO
import time
from random import randint

try:
    pinoR = 17  # pino RPi BCM 17
    pinoG = 27  # pino RPi BCM 27
    pinoB = 22  # pino RPi BCM 22

    tempo = 0.25 # tempo do sleep
    modoEndereco = GPIO.BCM # Modo de enderecamento do RPi
    frequencia = 100    # Frequencia do PWM
    
    GPIO.setwarnings(False) # Nao exibir mensagens de advertencia
    GPIO.setmode(modoEndereco)
    GPIO.setup(pinoR, GPIO.OUT)
    GPIO.setup(pinoG, GPIO.OUT)
    GPIO.setup(pinoB, GPIO.OUT)

    pwmR = GPIO.PWM(pinoR, frequencia)
    pwmG = GPIO.PWM(pinoG, frequencia)
    pwmB = GPIO.PWM(pinoB, frequencia)

    pwmR.start(0)
    pwmG.start(0)
    pwmB.start(0)
    
    while True:
        pwmR.ChangeDutyCycle(randint(0,100))
        pwmG.ChangeDutyCycle(randint(0,100))
        pwmB.ChangeDutyCycle(randint(0,100))
        time.sleep(tempo)
        

except KeyboardInterrupt:
    pwmR.stop(0)
    pwmG.stop(0)
    pwmB.stop(0)
    GPIO.cleanup()
    print "Configuracoes apagadas."
