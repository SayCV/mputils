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

class IHyperLynxDrcVia2(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def EndLayerMetalIndex(self):
        return self.obj.EndLayerMetalIndex

    @property
    def HasThermalPad(self):
        return self.obj.HasThermalPad

    @property
    def TieLegs(self):
        return self.obj.TieLegs

    @property
    def StartLayerMetalIndex(self):
        return self.obj.StartLayerMetalIndex

