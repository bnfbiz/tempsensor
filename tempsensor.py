#!/opt/tempsensor/venv/bin/python3

import qwiic_as6212
import argparse
import sys

parser = argparse.ArgumentParser(
                    prog='tempsensor.py',
                    description='Reports tempature from attached as6212 sensor',
                    epilog='default sensor is with i2c address of 0x48')
parser.add_argument('--i2cid', choices=['0x48', '0x49', '0x4A', '0x4B', '0x44', '0x45', '0x46', '0x47'], default='0x48')
parser.add_argument('-t','--temp_only', action='store_true')
parser.add_argument('-c', '--celcius', action='store_true')
parser.add_argument('-f', '--farenheight',action='store_true')
parser.add_argument('-v', '--verbose',
                    action='store_true')  # on/off flag
args = parser.parse_args()

myTempSensor = qwiic_as6212.QwiicAs6212Sensor(int(args.i2cid,16))

if myTempSensor.is_connected == False:
    print("The Qwiic AS6212 Sensor device isn't connected to the system. Please check your connection", \
        file=sys.stderr)

myTempSensor.set_sleep_mode(1)
if args.farenheight:
    temperature = myTempSensor.read_temp_f()
    if args.temp_only:
        print(temperature)
    else:
        print("The temperator is", temperature, "Farenheight")
if args.celcius:
    temperature = myTempSensor.read_temp_c()
    if args.temp_only:
        print(temperature)
    else:
        print("The temperature is", temperature, "Celcius")

sys.exit(0)
