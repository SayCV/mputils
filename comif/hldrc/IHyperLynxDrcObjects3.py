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

class IHyperLynxDrcObjects3(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Sorter(self):
        return self.obj.Sorter

    @Sorter.setter
    def Sorter(self, Sorter):
        self.obj.Sorter=Sorter

