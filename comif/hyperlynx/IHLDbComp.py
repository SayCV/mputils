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

class IHLDbComp(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Type(self):
        return self.obj.Type

    @property
    def PartType(self):
        return self.obj.PartType

    @property
    def Value(self):
        return self.obj.Value

    @property
    def RefDes(self):
        return self.obj.RefDes

    @property
    def Model(self):
        return self.obj.Model

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def FindPin(self):
        return self.obj.FindPin

    @property
    def AssignModel(self):
        return self.obj.AssignModel

    @Value.setter
    def Value(self, Value):
        self.obj.Value=Value

