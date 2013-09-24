#!/usr/bin/python

# Piscando dois LED com RPi e PWM

import RPi.GPIO as GPIO, time

modoEndereco = GPIO.BCM   # Modo de enderecamento dos pinos do RPi
modoIO = GPIO.OUT         # Modo de configuração da porta de Entrada/Saida
pinoLed1 = 17             # Pino do RPi associado ao led
pinoLed2 = 18             # Pino do RPi associado ao led
tempoEspera = 0.5         # Tempo de espera do pisca
frequencia = 200          # Frequencia do ciclo PWM em Hertz (Hz)

GPIO.setmode(modoEndereco)
GPIO.setup(pinoLed1, modoIO)
GPIO.setup(pinoLed2, modoIO)

led1 = GPIO.PWM(pinoLed1, frequencia)
led2 = GPIO.PWM(pinoLed2, frequencia)

led1.start(0)   # Inicia o PWM no canal do Led1
led2.start(0)   # Inicia o PWM no canal do Led2

try:
    while 1:
        for dc in range(0, 101, 10): 
            led1.ChangeDutyCycle(dc)        #Led1 aumenta o brilho 
	    led2.ChangeDutyCycle(100 - dc)  #Led2 diminui o brilho
            time.sleep(tempoEspera)
        for dc in range(100, -1, -10):
            led1.ChangeDutyCycle(dc)        #Led1 diminui o brilho
	    led2.ChangeDutyCycle(100 - dc)  #Led2 aumenta o brilho
            time.sleep(tempoEspera)
            
except KeyboardInterrupt:
  led1.stop()
  led2.stop()
  GPIO.cleanup()
  print "Configuracoes apagadas"
