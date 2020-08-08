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

class IHLDbNet(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Name(self):
        return self.obj.Name

    @property
    def IsSupply(self):
        return self.obj.IsSupply

    @property
    def Length(self):
        return self.obj.Length

    @property
    def Voltage(self):
        return self.obj.Voltage

    @IsSupply.setter
    def IsSupply(self, IsSupply):
        self.obj.IsSupply=IsSupply

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Vias(self):
        return self.obj.Vias

    @property
    def Segments(self):
        return self.obj.Segments

    @property
    def RelatedNets(self):
        return self.obj.RelatedNets

    @Voltage.setter
    def Voltage(self, Voltage):
        self.obj.Voltage=Voltage

