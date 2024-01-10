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
# Subscriber class : Listens to broker for updates, stay connected to broker
#####
class subscriber(Tk):
    
    def __init__(self, topic = 'COMP216', broker_address = 'localhost', broker_port = 1883):
        
        # Create a Mosquitto client object
        self.client = mqtt.Client()
        self.client.on_message = self.__on_message

        # Create broker member variables
        self.broker_address = broker_address
        self.broker_port = broker_port
        self.broker_topic = topic
                
        # Initialize the UI
        self.__initUI()

        # Connect to the broker
        self.__brokerconnect()

    def __initUI(self):

        # Init TkInter
        super().__init__()

        # Set window properties
        self.title('Subscriber')
        self.geometry('777x249')
        tk_style = ttk.Style()
        tk_style.theme_use('clam')
        self.app_font = 'Sans'
      
        # Exit button - Use .destroy instead to stop the TkInter .mainloop() thread REF: https://stackoverflow.com/questions/110923/how-do-i-close-a-tkinter-window
        self.exit_button = Button(self)
        self.exit_button.configure(command=self.destroy, font=(self.app_font,'9','bold'), text='Exit', foreground='green', width=18)
        self.exit_button.place(x=480,y=249-37)

        # Update broker button - This button was firing upon load, fixed! REF: https://stackoverflow.com/questions/20933639/tkinter-button-events-firing-on-load
        self.broker_update_button = Button(self)
        self.broker_update_button.configure(command=lambda: self.__brokerupdate(), font=(self.app_font,'9','bold'), text='Update Broker', foreground='green', width=18)
        self.broker_update_button.place(x=630,y=249-37)

        # Broker Address Label
        self.broker_address_label = Label(self)
        self.broker_address_label.configure(font=(self.app_font,'9','bold'), text='Broker Address:', width=15, foreground='black', anchor='e')
        self.broker_address_label.place(x=499,y=19)

        # Broker Address Textbox
        self.broker_address_txt = Text(self, height=1)
        self.broker_address_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_address_txt.place(x=613,y=19)
        self.broker_address_txt.insert(END,self.broker_address)

        # Broker Port Label
        self.broker_port_label = Label(self)
        self.broker_port_label.configure(font=(self.app_font,'9','bold'), text='Broker Port (1883):', width=15, foreground='black', anchor='e')
        self.broker_port_label.place(x=499,y=39)

        # Broker Port Textbox
        self.broker_port_txt = Text(self, height=1)
        self.broker_port_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_port_txt.place(x=613,y=39)
        self.broker_port_txt.insert(END,self.broker_port)
        
        # Broker Topic Label
        self.broker_topic_label = Label(self)
        self.broker_topic_label.configure(font=(self.app_font,'9','bold'), text='Broker Topic:', width=15, foreground='black', anchor='e')
        self.broker_topic_label.place(x=499,y=59)

        # Broker Topic Textbox
        self.broker_topic_txt = Text(self, height=1)
        self.broker_topic_txt.configure(font=(self.app_font,'9','bold'), width=21, foreground='black')
        self.broker_topic_txt.place(x=613,y=59)
        self.broker_topic_txt.insert(END,self.broker_topic)
        
        # Data Broker Information Area
        self.data_broker_info = Label(self)
        self.data_broker_info.configure(font=(self.app_font,'11','bold'), text=' ', foreground='black')
        self.data_broker_info.place(x=10,y=19)
        self.data_broker_info['text'] = f'Broker: {self.broker_address} Port: {self.broker_port} - Topic: {self.broker_topic}'

        # Data Packet Information Area
        self.data_packet_info = Label(self)
        self.data_packet_info.configure(font=(self.app_font,'13','bold'), width=25, text=' ', foreground='black')
        self.data_packet_info.place(x=100,y=59)
        self.data_broker_info['text'] = f'Received Data Packet:'

    def __brokerconnect(self):
        
        try:
            # Connect using the broker on the local machine and standard port, then subscribe to the topic
            self.client.connect(self.broker_address, self.broker_port)
            self.client.subscribe(self.broker_topic)
            self.client.loop_start()
        except:
            messagebox.showerror('Cound not connect to Broker', 'Could not connect to the broker. Please verify broker data, including broker port range (1024-65535), and that the broker is operational.')
        else:
            print(f'#######\n# Subscriber\n#####\nFound broker at {self.broker_address} on port {self.broker_port}')
            print(f'Listening for topic: {self.broker_topic}\n...')

    def __brokerdisconnect(self):
        
        try:
            # Stop the loop and attempt to disconnect
            self.client.loop_stop()
            self.client.disconnect()
        except:
            messagebox.showerror('Cound not disconnect from the Broker', 'Could not disconnect from the broker.')
        else:
            print(f'#######\n# Subscriber\n#####\nDisconnected subscriber from broker.')

    def __brokerupdate(self):

        # Disconnect from the broker
        self.__brokerdisconnect()

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
        else:
            messagebox.showinfo('Broker Data Updated', 'Broker information updated successfully.')
            # Connect to the broker
            self.__brokerconnect()
        finally:
            print(f'Broker Address: {self.broker_address} Broker Port: {self.broker_port} Broker Topic: {self.broker_topic}')

    def __on_message(self, client1, userdata, message):

        self.rx_message = f'Received Payload Data: {message.payload.decode("utf-8")}'
        self.data_broker_info['text'] = f'Received Data Packet:'
        # Print the received message topic
        print(f'({self.broker_topic}) {self.rx_message}')
        self.data_packet_info['text'] = self.rx_message

    def keep_alive(self):
        
        # Client object is created upon instantiation, now keep the client subscribed to the broker
        self.client.loop_forever()

#######
# Test Harness
#####

# Create subscriber object and stay subscribed to the broker.
sub_to_the_channel = subscriber()
sub_to_the_channel.mainloop()
