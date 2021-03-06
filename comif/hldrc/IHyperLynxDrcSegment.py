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

class IHyperLynxDrcSegment(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Layer(self):
        return self.obj.Layer

    @property
    def Width(self):
        return self.obj.Width

    @property
    def StartX(self):
        return self.obj.StartX

    @property
    def StartY(self):
        return self.obj.StartY

    @property
    def EndX(self):
        return self.obj.EndX

    @property
    def EndY(self):
        return self.obj.EndY

    @property
    def Trace(self):
        return self.obj.Trace

    @property
    def Length(self):
        return self.obj.Length

    @property
    def Net(self):
        return self.obj.Net

