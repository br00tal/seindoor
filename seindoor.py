#!/usr/bin/env python3

# Import necessary modules
import configparser
import glob
import os
import random
import RPi.GPIO as gpio
import sys
import time

# Initialize the config parser
config = configparser.ConfigParser()

# See if we specified a config file as an argument
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
  # If not, load the default config file
  config.read('seindoor.conf')

# Grab and assign the config variables
path   = config['DEFAULT']['path']
pin    = int(config['DEFAULT']['pin'])
player = config['DEFAULT']['player']

# Make sure the audio path specified in the config file exists
if not os.path.exists(path):
  print("The path %s/%s does not exist." % (os.getcwd(), path))
  exit(1)
else:
  # If it does, ensure it's absolute, for good measure
  path   = os.path.abspath(path)
  files  = glob.glob(os.path.join(path, '*'))

# Setup GPIO
gpio.setmode(gpio.BCM)
gpio.setup(pin, gpio.IN)

# Initiate the loop to check the switch
try:
  while True:
    sensor = gpio.input(pin)
    cmd = "%s %s" % (player, random.choice(files))
    if sensor:
      sys.stdout.write('+')
      os.system(cmd)
    else:
      sys.stdout.write('-')
    sys.stdout.flush()
    time.sleep(1)
finally:
  gpio.cleanup()
