class iotDevs():
    def __init__(self, folderpath="", status="", object="", client="", address="000.00.00.0"):
        self.folderpath = folderpath
        self.status = status
        self.object = object
        self.address = address
        self.client = client

        # Device setup, initialize MQTT broker
        client = mqtt.Client(self.client)
        client.connect(self.address)
        delay_mqtt = 0

    def deviceSetup(self):
        # Initialize MQTT broker
        client = mqtt.Client(self.client)
        client.connect(self.address)
        delay_mqtt = 0

    def changeStatus(self):
        if (self.status == True):
            self.status = False
        else:
            self.status = True
        # Swaps the state between on and off

    def setStatus(self, action):
        # Define what status refers to
        self.status = action

    def changeFolderpath(self, folderpath):
        self.folderpath = folderpath

    def changeObject(self, object):
        self.object = object

    def changeClient(self, client):
        self.client = client

    def changeAddress(self, address):
        self.address = address

def iotConnect(client,userdata,flags,rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed To Connect")

mqttBroker ="172.20.10.5" #Connecting to broker
client = mqtt.Client()
client.username_pw_set("mqtt_user", "mqtt_pass")
client.on_connect = on_connect
client.connect(mqttBroker, 1883)
client.loop_start()
delay_mqtt = 0