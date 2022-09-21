from Classes import *
from ctypes import addressof
import os
import cv2
import numpy as np
import pytorch
import paho.mqtt.client as mqtt
import torch

def main():
    model = torch.load(path)
    # Load neural network model
    smartSwitch = iotDevs()

    client = mqtt.Client()
    client.username_pw_set("mqtt_user", "mqtt_pass")
    client.on_connect = on_connect
    client.connect(mqttBroker, 1883)
    client.loop_start()
    delay_mqtt = 0

    folderPath = "FingerImages"
    myList = os.listdir(folderPath)
    imList = []
    for imPath in myList:
        image = cv2.imread(f'{folderPath}/{imPath}') # cv2.imread(<folderPath/n>) for n images
        pred = model.eval(image)
        # evaluate the image
        if pred == "Pointing and Lamp":
            smartSwitch.changeStatus()
            # If the pointing at lamp then change its current state (if off then on, if on then off)