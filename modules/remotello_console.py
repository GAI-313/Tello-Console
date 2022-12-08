# -*- coding: utf-8 -*-

import cv2
from time import sleep
import struct
import redis
import numpy as np
import json
from sshtunnel import SSHTunnelForwarder

class console:
    def __init__(self, ip_add =("192.168.195.164", 22), username="roboworks",passward="tamagawa",host_key=None, p_key=None, hostname="localhost", port=6379):
        # Redis connection setup
        self.ssht = SSHTunnelForwarder(
            ip_add,
            ssh_host_key=host_key,
            ssh_username=username,
            ssh_password=passward,
        	ssh_pkey=p_key,
        	remote_bind_address=(hostname, port))
        
        self.ssht.start() 
        self.r = redis.Redis(host=hostname, port=self.ssht.local_bind_port, db=0)

        self.cmd = ''
    
    def fromRedis(self, hRedis,topic):
        """Retrieve Numpy array from Redis key 'topic'"""
        encoded = self.r.get(topic)
        h, w = struct.unpack('>II',encoded[:8])		# unpack

        # make numpy array
        a = np.frombuffer(encoded, dtype=np.uint8, offset=8)

        # decode jpeg to opencv image
        decimg = cv2.imdecode(a, flags=cv2.IMREAD_UNCHANGED).reshape(h,w,3)

        return decimg

    # get state topic default topic is battery level
    def get_state_topic(self, topic="bat"):
        json_state = self.r.get('state')
        dict_state = json.loads( json_state )
        return dict_state[topic]

    # get drone camera frame's
    def get_frame(self):
        return self.fromRedis(self.r,'image')
    
#### Drone control methot's
    # Drone takeoff
    def takeoff(self):
        self.r.set('command','takeoff')
        # return

    # Drone landing
    def land(self):
        self.r.set('command','land')
        # return
    
    # Drone up to cm arg
    """
    20 < cm < 500
    """
    def up(self, cm):
        self.r.set('command','up %d'%(cm))
        # return
    
    # Drone down to cm arg
    """
    20 < cm < 500
    """
    def down(self, cm):
        self.r.set('command','down %d'%(cm))
        # return
    
    # Drone forward to cm arg
    """
    20 < cm < 500
    """
    def forward(self, cm):
        self.r.set('command','forward %d'%(cm))
        # return
    
    # Drone back to cm arg
    """
    20 < cm < 500
    """
    def back(self, cm):
        self.r.set('command','back %d'%(cm))
        # return
    
    # Drone right to cm arg
    """
    20 < cm < 500
    """
    def right(self, cm):
        self.r.set('command','right %d'%(cm))
        # return
    
    # Drone left to cm arg
    """
    20 < cm < 500
    """
    def left(self, cm):
        self.r.set('command','left %d'%(cm))
        # return
    
    # Drone turn to clock wise to dig arg
    """
    0 < dig < 360( or infinity)
    """
    def cw(self, dig):
        self.r.set('command','cw %d'%(dig))
        # return

    # Drone turn to counter clock wise to dig arg
    """
    0 < dig < 360( or infinity)
    """
    def ccw(self, dig):
        self.r.set('command','ccw %d'%(dig))
        # return
    
    # Drone turn to counter clock wise to dig arg
    """
    0 < dig < 360( or infinity)
    """
    def ccw(self, dig):
        self.r.set('command','ccw %d'%(dig))
        # return
    
    # Drone motor stop of emergency
    def emergency(self, dig):
        self.r.set('command','emergency')
        # return
    
### Get drone status
    # get ToF height
    def get_tof(self):
        return self.get_state_topic("tof")