# Group3 - Gordon Stevens (300864022), Alejandro Zheng Zheng (301083081), Trevor Williamson (822916995), Tale Abor-Gabriel (301071358)

#
# Initial setup using:
# Eclipse Mosquitto (Installed not as a service): https://mosquitto.org/download/
# pip install paho-mqtt
#

#
# ---=== Start Broker ===---
# [] Open command prompt
# cd C:\Program Files\mosquitto
# mosquitto -v
#
# ---=== Start Subscriber ===---
# [] Open new command prompt
# cd C:\Program Files\mosquitto
# mosquitto_sub -t COMP216
#
# ---=== Test Publisher ===---
# [] Open new command prompt
# cd C:\Program Files\mosquitto
# mosquitto_pub -t COMP216 -m "System test"
#
# ---=== Run Python Publisher ===---
# [] Open new command prompt
# python group3_publisher.py
# - note the subscriber window command prompt and the visual studio subscriber
#

#######
# Data Format
#####

#
# id: 10001
# time: 
# temperature:
#

#######
# Import
#####
from time import asctime
from random import randint
import group3_data_generator as patternedgen

#######
# Utility class : Assemble the data, print the data
#####
class util:
    
    def __init__(self):
        # On instantiation, instantiate a generator instance, then have the start ID and temperature reading from the pattern generator
        self.gen = patternedgen.generator()
        self.start_id = 100
        
    def create_data(self):
        # When data is requested to be created, increase the counter and gets a temperature datapoint, package up all the data and return the dictionary
        self.start_id += 1
        # Transmit “wild data” something that is completely off the chart. Again your subscriber should be able to handle this.
        self.simulate_wild_data = randint(1,42)
        if self.simulate_wild_data == 42:
            self.iot_data = { 
                'id': self.start_id, 
                'time': asctime(), 
                'temperature': 'NaN' }
        else:
            self.iot_data = { 
                'id': self.start_id, 
                'time': asctime(), 
                'temperature': self.gen.data }
        return self.iot_data

    def print_data(self, process_message):
        print(f'\n{process_message.topic} \n{process_message.payload.decode("utf-8")}')

#######
# Test Harness
#####

utility_test = util()
for x in range(11):
    print(utility_test.create_data())
