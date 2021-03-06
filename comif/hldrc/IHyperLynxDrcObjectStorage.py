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

class IHyperLynxDrcObjectStorage(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Item(self):
        return self.obj.Item

    @property
    def Count(self):
        return self.obj.Count

    @Item.setter
    def Item(self, Item):
        self.obj.Item=Item

    @property
    def Add(self):
        return self.obj.Add

    @property
    def Remove(self):
        return self.obj.Remove

    @property
    def RemoveAll(self):
        return self.obj.RemoveAll

    @property
    def Exists(self):
        return self.obj.Exists

    @property
    def Keys(self):
        return self.obj.Keys

    @property
    def Items(self):
        return self.obj.Items

    @property
    def Key(self, Key):
        return self.obj.Key

    @Key.setter
    def Key(self, Key):
        self.obj.Key=Key

