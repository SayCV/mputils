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

class IHyperLynxDrcGraphShortestPath(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def GetDistance(self):
        return self.obj.GetDistance

    @property
    def GetNodes(self):
        return self.obj.GetNodes

    @property
    def GetEdges(self):
        return self.obj.GetEdges

    @property
    def GetItems(self):
        return self.obj.GetItems

