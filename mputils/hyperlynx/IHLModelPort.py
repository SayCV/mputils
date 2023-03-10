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

class IHLModelPort(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ConnType(self):
        return self.obj.ConnType

    @property
    def Name(self):
        return self.obj.Name

    @property
    def ConnNet(self):
        return self.obj.ConnNet

    @ConnType.setter
    def ConnType(self, ConnType):
        self.obj.ConnType=ConnType

    @property
    def Side(self):
        return self.obj.Side

    @ConnNet.setter
    def ConnNet(self, ConnNet):
        self.obj.ConnNet=ConnNet

    @Side.setter
    def Side(self, Side):
        self.obj.Side=Side
