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

class IHyperLynxDrcPackagePinModel(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Capacitance(self):
        return self.obj.Capacitance

    @property
    def Inductance(self):
        return self.obj.Inductance

    @Capacitance.setter
    def Capacitance(self, Capacitance):
        self.obj.Capacitance=Capacitance

    @property
    def PackageModel(self):
        return self.obj.PackageModel

    @property
    def Delete(self):
        return self.obj.Delete

    @property
    def SetName(self):
        return self.obj.SetName

    @Inductance.setter
    def Inductance(self, Inductance):
        self.obj.Inductance=Inductance

