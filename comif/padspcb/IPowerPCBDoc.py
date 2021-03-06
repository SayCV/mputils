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

class IPowerPCBDoc(object):
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
    def path(self):
        return self.obj.path

    @property
    def FullName(self):
        return self.obj.FullName

    @property
    def ActiveView(self):
        return self.obj.ActiveView

    @property
    def Name(self):
        return self.obj.Name

    @property
    def Saved(self):
        return self.obj.Saved

    @Saved.setter
    def Saved(self, Saved):
        self.obj.Saved=Saved

    @property
    def unit(self):
        return self.obj.unit

    @property
    def LayerName(self):
        return self.obj.LayerName

    @property
    def LayerCount(self):
        return self.obj.LayerCount

    @property
    def LayerType(self):
        return self.obj.LayerType

    @property
    def LayerEnabled(self):
        return self.obj.LayerEnabled

    @property
    def ElectricalLayerCount(self):
        return self.obj.ElectricalLayerCount

    @unit.setter
    def unit(self, unit):
        self.obj.unit=unit

    @property
    def Preference(self):
        return self.obj.Preference

    @property
    def Components(self):
        return self.obj.Components

    @property
    def Nets(self):
        return self.obj.Nets

    @property
    def NetClasses(self):
        return self.obj.NetClasses

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Vias(self):
        return self.obj.Vias

    @property
    def Connections(self):
        return self.obj.Connections

    @property
    def RouteSegments(self):
        return self.obj.RouteSegments

    @property
    def Drawings(self):
        return self.obj.Drawings

    @property
    def Texts(self):
        return self.obj.Texts

    @property
    def Activate(self):
        return self.obj.Activate

    @property
    def GetObjects(self):
        return self.obj.GetObjects

    @property
    def SelectObjects(self):
        return self.obj.SelectObjects

    @property
    def Save(self):
        return self.obj.Save

    @property
    def SaveAs(self):
        return self.obj.SaveAs

    @property
    def SaveTemp(self):
        return self.obj.SaveTemp

    @property
    def SaveAsTemp(self):
        return self.obj.SaveAsTemp

    @property
    def SaveNoLock(self):
        return self.obj.SaveNoLock

    @property
    def SaveAsNoLock(self):
        return self.obj.SaveAsNoLock

    @property
    def IntegrityTest(self):
        return self.obj.IntegrityTest

    @property
    def Layers(self):
        return self.obj.Layers

    @property
    def Errors(self):
        return self.obj.Errors

    @property
    def MaxRealValue(self):
        return self.obj.MaxRealValue

    @property
    def MinRealValue(self):
        return self.obj.MinRealValue

    @property
    def SetColor(self):
        return self.obj.SetColor

    @property
    def GetColor(self):
        return self.obj.GetColor

    @property
    def SetVisibility(self):
        return self.obj.SetVisibility

    @property
    def GetVisibility(self):
        return self.obj.GetVisibility

    @property
    def SaveAsSwitchDocument(self):
        return self.obj.SaveAsSwitchDocument

    @property
    def Jumpers(self):
        return self.obj.Jumpers

    @property
    def BoardOutlineSurface(self):
        return self.obj.BoardOutlineSurface

    @property
    def GetPlacedComponents(self):
        return self.obj.GetPlacedComponents

    @property
    def Attributes(self):
        return self.obj.Attributes

    @property
    def AttributeTypes(self):
        return self.obj.AttributeTypes

    @property
    def PartTypes(self):
        return self.obj.PartTypes

    @property
    def Decals(self):
        return self.obj.Decals

    @property
    def OriginX(self):
        return self.obj.OriginX

    @property
    def OriginY(self):
        return self.obj.OriginY

    @Preference.setter
    def Preference(self, Preference):
        self.obj.Preference=Preference

    @property
    def GridX(self):
        return self.obj.GridX

    @GridX.setter
    def GridX(self, GridX):
        self.obj.GridX=GridX

    @property
    def GridY(self):
        return self.obj.GridY

    @property
    def AssemblyOptions(self):
        return self.obj.AssemblyOptions

    @property
    def ImportNetList(self):
        return self.obj.ImportNetList

    @property
    def ExportNetList(self):
        return self.obj.ExportNetList

    @property
    def ExportASCII(self):
        return self.obj.ExportASCII

    @property
    def ImportECOFile(self):
        return self.obj.ImportECOFile

    @property
    def ExportECOFile(self):
        return self.obj.ExportECOFile

    @property
    def CheckASCII(self):
        return self.obj.CheckASCII

    @property
    def ExportRules(self):
        return self.obj.ExportRules

    @property
    def AddText(self):
        return self.obj.AddText

    @property
    def ExportCC(self):
        return self.obj.ExportCC

    @property
    def ExportCLB(self):
        return self.obj.ExportCLB

    @property
    def ImportCLB(self):
        return self.obj.ImportCLB

    @property
    def AssociatedNets(self):
        return self.obj.AssociatedNets

    @GridY.setter
    def GridY(self, GridY):
        self.obj.GridY=GridY

    @property
    def ActiveLayer(self):
        return self.obj.ActiveLayer

    @property
    def SketchGetTag(self):
        return self.obj.SketchGetTag

    @property
    def SketchDrawByTag(self):
        return self.obj.SketchDrawByTag

    @property
    def SketchDelByTag(self):
        return self.obj.SketchDelByTag

    @ActiveLayer.setter
    def ActiveLayer(self, ActiveLayer):
        self.obj.ActiveLayer=ActiveLayer

