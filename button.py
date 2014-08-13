import RPi.GPIO as gpio
gpio.setmode(gpio.BOARD)
gpio.setup(7, gpio.IN)
gpio.setup(11, gpio.OUT)

while True:
  input_value = gpio.input(7)
  if input_value == False:
    print("pressed!")
    gpio.output(11, True)
  else:
    gpio.output(11, False)
