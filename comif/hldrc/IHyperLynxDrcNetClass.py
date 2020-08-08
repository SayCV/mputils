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

class IHyperLynxDrcNetClass(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ElecNets(self):
        return self.obj.ElecNets

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def AddAttribute(self):
        return self.obj.AddAttribute

    @property
    def PhysicalNets(self):
        return self.obj.PhysicalNets

