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

class IHyperLynxDrcGeometry(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def CircleX(self):
        return self.obj.CircleX

    @property
    def CircleY(self):
        return self.obj.CircleY

    @property
    def Filled(self):
        return self.obj.Filled

    @property
    def CircleR(self):
        return self.obj.CircleR

    @property
    def Outline(self):
        return self.obj.Outline

    @property
    def PointsArray(self):
        return self.obj.PointsArray

    @Filled.setter
    def Filled(self, Filled):
        self.obj.Filled=Filled

    @property
    def RectMaxX(self):
        return self.obj.RectMaxX

    @property
    def RectMaxY(self):
        return self.obj.RectMaxY

    @property
    def RectMinX(self):
        return self.obj.RectMinX

    @property
    def RectMinY(self):
        return self.obj.RectMinY

    @property
    def IsArced(self):
        return self.obj.IsArced

    @property
    def IsCircle(self):
        return self.obj.IsCircle

    @property
    def IsClosed(self):
        return self.obj.IsClosed

    @property
    def IsCutout(self):
        return self.obj.IsCutout

    @property
    def IsSegment(self):
        return self.obj.IsSegment

    @property
    def IsRect(self):
        return self.obj.IsRect

    @property
    def Area(self):
        return self.obj.Area

    @property
    def VerticesCount(self):
        return self.obj.VerticesCount

    @property
    def Extrema(self):
        return self.obj.Extrema

    @property
    def IsValid(self):
        return self.obj.IsValid

    @property
    def Element(self):
        return self.obj.Element

    @property
    def Delete(self):
        return self.obj.Delete

    @PointsArray.setter
    def PointsArray(self, PointsArray):
        self.obj.PointsArray=PointsArray
