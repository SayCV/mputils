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

class IHLScmGeneric(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Type(self):
        return self.obj.Type

    @property
    def PortCount(self):
        return self.obj.PortCount

    @property
    def x(self):
        return self.obj.x

    @property
    def y(self):
        return self.obj.y

    @property
    def GetNode(self):
        return self.obj.GetNode

    @property
    def GetPortIndex(self):
        return self.obj.GetPortIndex

    @property
    def GetCoord(self):
        return self.obj.GetCoord

    @property
    def SetCoord(self):
        return self.obj.SetCoord

    @property
    def Name(self):
        return self.obj.Name

