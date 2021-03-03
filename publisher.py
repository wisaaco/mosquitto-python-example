#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" 
Publish some messages to queue
"""
import paho.mqtt.client as mqtt

client = mqtt.Client()

msgs = [{'topic': "gatos/yolo", 'payload': "jump"},
        {'topic': "perros/pics", 'payload': "some photo"},
        {'topic': "perros/news", 'payload': "extra extra"},
        {'topic': "perros/news", 'payload': "super extra"}]


client.connect("test.mosquitto.org", 1883, 60)
client.publish("gatos/yolo","HOLA MUNDO, ¿alguién me escucha?")



# vi: set fileencoding=utf-8 :
