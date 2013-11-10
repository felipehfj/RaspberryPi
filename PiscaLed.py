#!/usr/bin/python

# Piscando LED com RPi

import RPi.GPIO as GPIO, time

modoEndereco = GPIO.BCM   # Modo de enderecamento dos pinos do RPi
modoIO = GPIO.OUT         # Modo de configuracao da porta de Entrada/Saida
pinoLed = 18              # Pino do RPi associado ao led
tempoEspera = 0.5         # Tempo de espera do pisca

try:
  GPIO.setmode(modoEndereco)
  GPIO.setwarnings(False)
  GPIO.setup(pinoLed, modoIO)
  print ("Programa iniciado")

  while True:
          GPIO.output(pinoLed, True)
          time.sleep(tempoEspera)
          GPIO.output(pinoLed, False)
          time.sleep(tempoEspera)
         
except KeyboardInterrupt:
  GPIO.cleanup()
  print ("Programa encerrado")
