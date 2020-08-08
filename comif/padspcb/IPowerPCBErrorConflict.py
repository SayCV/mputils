# coding=utf-8
"""
This file is autogenerated by python script @ 20200726-10:57:03
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IPowerPCBErrorConflict(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def ConflictObjectType(self):
        return self.obj.ConflictObjectType

    @property
    def ConflictObjectDesc(self):
        return self.obj.ConflictObjectDesc

    @property
    def ConflictObject(self):
        return self.obj.ConflictObject

    @property
    def Name(self):
        return self.obj.Name

