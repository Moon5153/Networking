# Group3 - Gordon Stevens (300864022), Alejandro Zheng Zheng (301083081), Trevor Williamson (822916995), Tale Abor-Gabriel (301071358)

#######
# Import
#####
from group3_utils import util
import paho.mqtt.client as mqtt
from time import sleep
from json import dumps
from random import randint
from tkinter import *
from tkinter import ttk, messagebox

#######
# Publisher class : Connect to broker, send topic and message, disconnect from broker.
#####
class publisher(Tk):

    def __init__(self, broker_address='localhost', broker_port=1883, topic='COMP216', delay=0.75):

        # Create a Util object for the data assembly task, and a mosquitto client object
        self.generation = util()
        self.client = mqtt.Client()
        
        # set the broker info, delay timer, and topic for this publisher object
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.broker_topic = topic
        self.broker_delay = delay

        # Check to see if this app is running, and this check makes sure there isn't a conflict with TkInter's thread
        self.is_running = False

        # Initialize the broker window
        self.__initUI()

    def __initUI(self):

        # Init TkInter
        super().__init__()

        # Set window properties
        self.title('Publisher')
        self.geometry('777x249')
        tk_style = ttk.Style()
        tk_style.theme_use('clam')
        self.app_font = 'Sans'

        # PublishInfinite button - Proper TkInter style boldness REF: https://makeapppie.com/2014/05/04/from-apple-to-raspberry-pi-a-gentle-introduction-to-themed-widgets-with-ttk/
        self.publishinfinite_button = Button(self)
        self.publishinfinite_button.configure(command=self.__button_press_publishinfinite, font=(self.app_font,'17','bold'), text='Publish Continuously', foreground='green', width=19)
        self.publishinfinite_button.place(x=10,y=249-129)

        # PublishOnce button - Proper TkInter style boldness REF: https://makeapppie.com/2014/05/04/from-apple-to-raspberry-pi-a-gentle-introduction-to-themed-widgets-with-ttk/
        self.publishonce_button = Button(self)
        self.publishonce_button.configure(command=self.__button_press_publishonce, font=(self.app_font,'13','bold'), text='Publish One Packet', foreground='green', width=19)
        self.publishonce_button.place(x=10,y=249-77)

        # Exit button - Use .destroy instead to stop the TkInter .mainloop() thread REF: https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
        self.exit_button = Button(self)
        self.exit_button.configure(command=self.destroy, font=(self.app_font,'9','bold'), text='Exit', foreground='green', width=18)
        self.exit_button.place(x=10,y=249-37)

        # Update broker button - This button was firing upon load, fixed! REF: https://stackoverflow.com/questions/20933639/tkinter-button-events-firing-on-load
        self.broker_update_button = Button(self)
        self.broker_update_button.configure(command=lambda: self.__brokerupdate(), font=(self.app_font,'9','bold'), text='Update Broker', foreground='green', width=18)
        self.broker_update_button.place(x=149,y=249-37)

        # Broker Address Label
        self.broker_address_label = Label(self)
        self.broker_address_label.configure(font=(self.app_font,'9','bold'), text='Broker Address:', width=15, foreground='black', anchor='e')
        self.broker_address_label.place(x=17,y=19)

        # Broker Address Textbox
        self.broker_address_txt = Text(self, height=1)
        self.broker_address_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_address_txt.place(x=129,y=19)
        self.broker_address_txt.insert(END,self.broker_address)

        # Broker Port Label
        self.broker_port_label = Label(self)
        self.broker_port_label.configure(font=(self.app_font,'9','bold'), text='Broker Port (1883):', width=15, foreground='black', anchor='e')
        self.broker_port_label.place(x=17,y=39)

        # Broker Port Textbox
        self.broker_port_txt = Text(self, height=1)
        self.broker_port_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_port_txt.place(x=129,y=39)
        self.broker_port_txt.insert(END,self.broker_port)
        
        # Broker Topic Label
        self.broker_topic_label = Label(self)
        self.broker_topic_label.configure(font=(self.app_font,'9','bold'), text='Broker Topic:', width=15, foreground='black', anchor='e')
        self.broker_topic_label.place(x=17,y=59)

        # Broker Topic Textbox
        self.broker_topic_txt = Text(self, height=1)
        self.broker_topic_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_topic_txt.place(x=129,y=59)
        self.broker_topic_txt.insert(END,self.broker_topic)

        # Data Broker Information Area
        self.data_broker_info = Label(self)
        self.data_broker_info.configure(font=(self.app_font,'11','bold'), text=' ', foreground='black')
        self.data_broker_info.place(x=339,y=19)

        self.data_broker_info['text'] = f'Broker: {self.broker_address} Port: {self.broker_port} - Topic: {self.broker_topic}'

        # Data Packet Information Area
        self.data_packet_info = Label(self)
        self.data_packet_info.configure(font=(self.app_font,'17','bold'), text=' ', foreground='black')
        self.data_packet_info.place(x=329,y=59)
    
    def __threader(self):
        if self.is_running == True:
            self.__button_press_publishonce()
        self.after(randint(1100,1700), self.__threader)
    
    def __button_press_publishinfinite(self):

        # If it is not running, start it up
        if self.is_running == False:
            self.is_running = True
            self.publishinfinite_button['text'] = 'Stop Publishing'
            self.publishonce_button['state'] = 'disabled'
            self.broker_update_button['state'] = 'disabled'
            self.exit_button['state'] = 'disabled'
            self.broker_address_txt['state'] = 'disabled'
            self.broker_port_txt['state'] = 'disabled'
            self.broker_topic_txt['state'] = 'disabled'
            self.__threader()
        else:
            self.is_running = False
            self.publishinfinite_button['text'] = 'Publish Continuously'
            self.broker_update_button['state'] = 'normal'
            self.publishonce_button['state'] = 'normal'
            self.exit_button['state'] = 'normal'
            self.broker_address_txt['state'] = 'normal'
            self.broker_port_txt['state'] = 'normal'
            self.broker_topic_txt['state'] = 'normal'

    def __button_press_publishonce(self):

        # Announce the publisher has started
        print(f'\nPublishing data to broker at {self.broker_address} on port {self.broker_port}')

        # You must miss transmission with a frequency of about 1 in very 100 transmissions. This must not be deterministic!
        self.simulate_not_perfect_transmission = randint(1,100)
        if self.simulate_not_perfect_transmission == 100:
            # Simulate missing a packet transmission
            self.data_packet_info['text'] = f'Missed Publishing Payload Data: {self.data_payload}'
            print(f'Missed transmission of data packet: {self.data_payload}')
        else:
            # Send transmission; Get datapoint from Util class
            self.data_payload = dumps(obj=self.generation.create_data(), indent=2)
            # Start the __brokerconnect method
            self.data_packet_info['text'] = f'Publishing Payload Data: {self.data_payload}'
            self.__brokerconnect()

    def __brokerconnect(self):

        try:
            self.client.connect(host=self.broker_address, port=self.broker_port)
            self.client.publish(topic=self.broker_topic, payload=self.data_payload)
        except:
            messagebox.showwarning('Broker Publishing Problem', 'Could not publish data to broker, please verify broker data and try again.') # Different types of message boxes - REF: https://docs.python.org/3/library/tkinter.messagebox.html
        else:
            # Show data sent to broker
            print(f'{self.data_payload} on topic {self.broker_topic} sent to the broker!')
            self.data_packet_info['text'] = f'Published Payload Data: {self.data_payload}'
        finally:
            # Always disconnect from the broker
            self.__brokerdisconnect()

    def __brokerdisconnect(self):
        try:
            # Delay closing the connection to allow for full transaction, then disconnect from broker
            # REF: https://stackoverflow.com/questions/41485676/mqtt-mosquitto-disconnection
            sleep(self.broker_delay)
            self.client.disconnect()
        except:
            messagebox.showerror('Cound not disconnect from the Broker', 'Could not disconnect from the broker.')
        else:
            print(f'#######\n# Subscriber\n#####\nDisconnected subscriber from broker.')            

    def __brokerupdate(self):
    
        try:
            # Get() data from the textboxes - STRIP \n's! - REF: https://www.kite.com/python/answers/how-to-remove-a-trailing-newline-in-python#:~:text=Use%20str.,to%20the%20original%20string's%20variable.
            self.broker_address = self.broker_address_txt.get('1.0',END)
            self.broker_address = self.broker_address.rstrip('\n')#[0:-1]
            self.broker_topic = self.broker_topic_txt.get('1.0',END)
            self.broker_topic = self.broker_topic.rstrip('\n')
            self.broker_port_check = int(self.broker_port_txt.get('1.0',END))
             
            if (self.broker_port_check >= 1024) and (self.broker_port_check <= 65535):
                self.broker_port = self.broker_port_check
            else:
                messagebox.showerror('Invalid Broker Data', 'Please enter valid broker data, including broker port range (1024-65535)')
                
            self.data_broker_info['text'] = f'Broker: {self.broker_address} Port: {self.broker_port} - Topic: {self.broker_topic}'
        except:
            messagebox.showerror('Invalid Broker Data', 'Please enter valid broker data, including broker port range (1024-65535)')
            pass
        else:
            messagebox.showinfo('Broker Data Updated', 'Broker information updated successfully.')
        finally:
            print(f'Broker Address: {self.broker_address} Broker Port: {self.broker_port} Broker Topic: {self.broker_topic}')

#######
# Test Harness
#####
publish = publisher()
publish.mainloop()
