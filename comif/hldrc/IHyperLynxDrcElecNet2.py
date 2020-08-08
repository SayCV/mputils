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

class IHyperLynxDrcElecNet2(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ElecNetDiffPair(self):
        return self.obj.ElecNetDiffPair

    @property
    def KneeFrequency(self):
        return self.obj.KneeFrequency

    @property
    def SwitchFrequency(self):
        return self.obj.SwitchFrequency

    @property
    def ConstraintClassName(self):
        return self.obj.ConstraintClassName

