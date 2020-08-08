# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-11:53:05
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IPowerLogicField(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def Name(self):
        return self.obj.Name

    @property
    def Value(self):
        return self.obj.Value

    @Value.setter
    def Value(self, Value):
        self.obj.Value=Value

