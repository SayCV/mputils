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

class IHyperLynxDrcCollEngine(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Or(self):
        return self.obj.Or

    @property
    def Xor(self):
        return self.obj.Xor

    @property
    def Subtract(self):
        return self.obj.Subtract

    @property
    def And(self):
        return self.obj.And

