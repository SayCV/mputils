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

class IHyperLynxDrcDocument2(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def ParentSettingsFileName(self):
        return self.obj.ParentSettingsFileName

    @property
    def NewElecNetDiffPair(self):
        return self.obj.NewElecNetDiffPair

    @property
    def NewShareList(self):
        return self.obj.NewShareList

    @property
    def LoadComponentModel(self):
        return self.obj.LoadComponentModel

    @property
    def GetObjects(self):
        return self.obj.GetObjects

    @property
    def ShareLists(self):
        return self.obj.ShareLists

