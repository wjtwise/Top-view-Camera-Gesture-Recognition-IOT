from Classes import *
from ctypes import addressof
import os
import cv2
import numpy as np
# import paho.mqtt.client as mqtt
import torch
from models.experimental import attempt_load
from utils.datasets import LoadImages
from utils.general import check_img_size, non_max_suppression, apply_classifier
from utils.torch_utils import load_classifier


path = '../yolov7_TOP_Camera.pt'
model = attempt_load(path, map_location=torch.device('cpu'))
stride = int(model.stride.max())  # model stride

    # Load neural network model
    # smartSwitch = iotDevs()

    # client = mqtt.Client()
    # client.username_pw_set("mqtt_user", "mqtt_pass")
    # client.on_connect = on_connect
    # client.connect(mqttBroker, 1883)
    # client.loop_start()
    # delay_mqtt = 0

folderPath = "/home/christopherwoolford/Top-view-Camera-Gesture-Recognition-IOT/Images/topview_test/images"
dataset = LoadImages(folderPath, stride=stride)

for path, img, im0s, vid_cap in dataset:
    img = torch.from_numpy(img.astype(np.float32)).to(torch.device('cpu'))
    #img = img.half() if half else img.float()  # uint8 to fp16/32
    img /= 255.0  # 0 - 255 to 0.0 - 1.0
    if img.ndimension() == 3:
        img = img.unsqueeze(0)

    pred = model(img)[0]
    pred = non_max_suppression(pred, 0.25, 0.45, classes=None, agnostic=False, multi_label=True,)[0]
    # Predictions from YOLOv7

    modelc = load_classifier(name='resnet101', n=2)  # initialize

    print(torch.load('/home/christopherwoolford/.cache/torch/hub/checkpoints/resnet101-cd907fc2.pth', map_location=torch.device('cpu')).keys())

    modelc.load_state_dict(torch.load('/home/christopherwoolford/.cache/torch/hub/checkpoints/resnet101-cd907fc2.pth', map_location=torch.device('cpu'))).to(torch.device('cpu')).eval()  

    pred = apply_classifier(pred, modelc, img, im0s)

    print(pred)

    exit()

        # evaluate the image
        # if pred == "Pointing and Lamp":
            # smartSwitch.changeStatus()
            # If the pointing at lamp then change its current state (if off then on, if on then off)