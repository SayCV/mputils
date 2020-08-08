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

class IHLModelSelector(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Selection(self):
        return self.obj.Selection

    @property
    def Count(self):
        return self.obj.Count

    @property
    def Item(self):
        return self.obj.Item

    @Selection.setter
    def Selection(self, Selection):
        self.obj.Selection=Selection

