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

class IHyperLynxDrcGraphEdge(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Nodes(self):
        return self.obj.Nodes

    @property
    def Weight(self):
        return self.obj.Weight

    @property
    def SetName(self):
        return self.obj.SetName

    @property
    def Store(self):
        return self.obj.Store

    @Weight.setter
    def Weight(self, Weight):
        self.obj.Weight=Weight

