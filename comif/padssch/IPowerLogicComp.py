# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-11:53:05
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IPowerLogicComp(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Name(self):
        return self.obj.Name

    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def PartType(self):
        return self.obj.PartType

    @property
    def PartTypeLogic(self):
        return self.obj.PartTypeLogic

    @property
    def Attributes(self):
        return self.obj.Attributes

    @Name.setter
    def Name(self, Name):
        self.obj.Name=Name

    @property
    def PCBDecal(self):
        return self.obj.PCBDecal

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Gates(self):
        return self.obj.Gates

    @property
    def ObjectType(self):
        return self.obj.ObjectType

    @property
    def selected(self):
        return self.obj.selected

    @PCBDecal.setter
    def PCBDecal(self, PCBDecal):
        self.obj.PCBDecal=PCBDecal

    @property
    def Sheets(self):
        return self.obj.Sheets

    @property
    def UnusedGates(self):
        return self.obj.UnusedGates

    @property
    def Delete(self):
        return self.obj.Delete

    @property
    def PartTypeObject(self):
        return self.obj.PartTypeObject

    @selected.setter
    def selected(self, selected):
        self.obj.selected=selected

    @property
    def ZoomSelected(self, ZoomSelected):
        return self.obj.ZoomSelected

    @ZoomSelected.setter
    def ZoomSelected(self, ZoomSelected):
        self.obj.ZoomSelected=ZoomSelected

    @PartType.setter
    def PartType(self, PartType):
        self.obj.PartType=PartType

