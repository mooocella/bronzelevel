from machine import Pin, PWM
from time import sleep

#defining LEDs and tilt sensor
pwm_1 = PWM(Pin(15))
pwm_2 = PWM(Pin(13))
pwm_3 = PWM(Pin(12))
tilt_sensor = Pin(14, Pin.IN, Pin.PULL_DOWN)

#setting frequency
pwm_1.freq(1000)
pwm_2.freq(1000)
pwm_3.freq(1000)

while True:
  #if the tilt sensor is up, nothing happens
  if tilt_sensor.value():
    pass
  else:
    #if the tilt sensor is tilted, the leds light up in  pattern of a siren
    for duty in range(65025):
      pwm_1.duty_u16(duty)
      sleep(0.0000001)
    for duty in range(65025, 0, -1000):
      pwm_1.duty_u16(duty)
      sleep(0.0000001)
    for duty in range(65025):
      pwm_2.duty_u16(duty)
      sleep(0.0000001)
    for duty in range(65025, 0, -1000):
      pwm_2.duty_u16(duty)
      sleep(0.0000001)
    for duty in range(65025):
      pwm_3.duty_u16(duty)
      sleep(0.0000001)
    for duty in range(65025, 0, -1000):
      pwm_3.duty_u16(duty)
      sleep(0.0000001)
