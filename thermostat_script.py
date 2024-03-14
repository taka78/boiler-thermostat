#!/usr/bin/env python

import time
import RPi.GPIO as GPIO
import os
import glob
import signal
import threading
from urllib.request import urlopen
import asyncio
# New (potentially compatible) import, depending on version
#from homeassistant.helpers.entity_platform import add_entities
from homeassistant.helpers.entity import Entity



os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'



myAPI = "DQO81RVKZACIGCB1"
myDelay = 15 #how many seconds between posting data

 
 
##def print_time(stop_flag):
##	global count, stop flag
##	count += 1
##	print(count)
##	if stop_flag = count:
##		signal.alarm(0)
	
	
##def timer_handler(signum, frame, stop_flag):
##	threading.Thread(target=print_numbers,10).start()
	
##signal.signal(signal

'''def thingspeak():

    print('starting...')
    try:
        temp = float(round(read_temp(), 1))
        f = urlopen(f'https://my_stupid_thingspeak_client.api.com') ##change the url daahh
        print(f.read)
        f.close()
    except Exception as e:
        print(e)'''
###this one is for another project that i will never finish i guess?


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def set_target_temp(new_temp):
    global target_temp
    target_temp = new_temp
    # Update your thermostat control script to match the new target temp

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = (float(temp_string) / 1000.0) - 2.8
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c
	
################
'''async def read_temp():
    """Asynchronously reads the temperature from the sensor."""

    lines = read_temp_raw()

    while lines[0].strip()[-3:] != 'YES':
        await asyncio.sleep(0.2)  # Use asyncio.sleep for asynchronous delay
        lines = read_temp_raw()

    equals_pos = lines[1].find('t=')

    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = (float(temp_string) / 1000.0) - 2.8
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c

    return None  # Or a default value if reading fails'''
#dont look at this, move on, there is nothing to see in here...


def close_circuit():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)

	GPIO.output(17, GPIO.HIGH)
	GPIO.cleanup()
	closed = True
	closing_time = time.time()
	return closed, closing_time
	


def open_circuit():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(17, GPIO.OUT)
	GPIO.output(17, GPIO.LOW)
	opened = True
	opening_time = time.time()
	return opened, opening_time

def set_target_temp(new_temp):
    global target_temp     
    target_temp = new_temp
    temp = read_temp()
    print(temp)
    #thingspeak()
    if float(temp) < float(target_temp) - 0.5:
        print("waiting to boily thing")
        open_circuit()
        time.sleep(300)
    elif float(temp) > float(target_temp) + 0.5:
        close_circuit()
        time.sleep(600)
    else:
        time.sleep(5)
