# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-12:11:09
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IHyperLynxDrcPhysicalNet5(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def UseNameForElecNet(self):
        return self.obj.UseNameForElecNet

    @property
    def GetPinsByType(self):
        return self.obj.GetPinsByType

    @property
    def MaxTraceWidth(self):
        return self.obj.MaxTraceWidth

    @UseNameForElecNet.setter
    def UseNameForElecNet(self, UseNameForElecNet):
        self.obj.UseNameForElecNet=UseNameForElecNet

