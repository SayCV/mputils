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

class IHLIcModel(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def PinModel(self):
        return self.obj.PinModel

    @property
    def Selector(self):
        return self.obj.Selector

    @property
    def DirType(self):
        return self.obj.DirType

    @property
    def IoDir(self):
        return self.obj.IoDir

    @property
    def ModelPin(self):
        return self.obj.ModelPin

    @property
    def Invert(self):
        return self.obj.Invert

    @IoDir.setter
    def IoDir(self, IoDir):
        self.obj.IoDir=IoDir

    @property
    def DrvState(self):
        return self.obj.DrvState

    @Invert.setter
    def Invert(self, Invert):
        self.obj.Invert=Invert

    @property
    def SpicePorts(self):
        return self.obj.SpicePorts

    @DrvState.setter
    def DrvState(self, DrvState):
        self.obj.DrvState=DrvState
