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

class IHyperLynxDrcPin(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def Component(self):
        return self.obj.Component

    @property
    def Net(self):
        return self.obj.Net

    @property
    def PositionX(self):
        return self.obj.PositionX

    @property
    def PositionY(self):
        return self.obj.PositionY

    @property
    def PinModel(self):
        return self.obj.PinModel

    @property
    def Layer(self):
        return self.obj.Layer

    @property
    def IsConnected(self):
        return self.obj.IsConnected

    @property
    def Pads(self):
        return self.obj.Pads

    @property
    def Teardrops(self):
        return self.obj.Teardrops

    @property
    def IsSMD(self):
        return self.obj.IsSMD

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def AddAttribute(self):
        return self.obj.AddAttribute

    @property
    def Type(self):
        return self.obj.Type

