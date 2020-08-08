# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-20:13:09
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IHLSpicePort(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def CktConn(self):
        return self.obj.CktConn

    @property
    def Name(self):
        return self.obj.Name

    @CktConn.setter
    def CktConn(self, CktConn):
        self.obj.CktConn=CktConn
