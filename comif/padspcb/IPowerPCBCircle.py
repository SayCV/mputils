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

class IPowerPCBCircle(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def Geometry(self):
        return self.obj.Geometry

    @property
    def LineWidth(self):
        return self.obj.LineWidth

    @property
    def OutlineType(self):
        return self.obj.OutlineType

    @property
    def ShapeType(self):
        return self.obj.ShapeType

    @property
    def Radius(self):
        return self.obj.Radius

    @property
    def CenterX(self):
        return self.obj.CenterX

    @property
    def CenterY(self):
        return self.obj.CenterY

    @property
    def layer(self):
        return self.obj.layer

    @property
    def LineStyle(self):
        return self.obj.LineStyle

    @property
    def Application(self):
        return self.obj.Application

