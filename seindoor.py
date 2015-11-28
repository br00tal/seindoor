#!/usr/bin/env python

# Import necessary modules
import configparser
import os
import RPi.GPIO as gpio
import sys
import time

# Initialize the config parser
config = configparser.ConfigParser()

# Config file stuff
argtotal = len(sys.argv)
if argtotal > 2:
  print("More than one argument specified!")
  exit(1)
elif argtotal == 2:
  try:
    with open(sys.argv[1]) as f:
      config.read(sys.argv[1])
  except IOError:
    raise
else:
  config.read('seindoor.conf')

# Grab and assign the config variables
path   = config['DEFAULT']['path']
pin    = int(config['DEFAULT']['pin'])
player = config['DEFAULT']['player']
files  = os.listdir(path)

# Setup GPIO
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.IN)

# Initiate the loop to check the switch
try:
  while True:
    sensor = gpio.input(pin)
    if sensor:
      sys.stdout.write('+')
    else:
      sys.stdout.write('-')
    sys.stdout.flush()
    time.sleep(1)
finally:
  gpio.cleanup()

# Loop through and play the files
for i in files:
  cmd = "%s %s/%s" % (player, path, i)
  os.system(cmd)
