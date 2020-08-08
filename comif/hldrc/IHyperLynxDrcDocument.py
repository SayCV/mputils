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

class IHyperLynxDrcDocument(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def FullName(self):
        return self.obj.FullName

    @property
    def IsSaved(self):
        return self.obj.IsSaved

    @property
    def View(self):
        return self.obj.View

    @property
    def LocalModelDirectories(self):
        return self.obj.LocalModelDirectories

    @property
    def IBISModelDirectories(self):
        return self.obj.IBISModelDirectories

    @property
    def DRCDirectories(self):
        return self.obj.DRCDirectories

    @property
    def Annotations(self):
        return self.obj.Annotations

    @property
    def Boards(self):
        return self.obj.Boards

    @property
    def Components(self):
        return self.obj.Components

    @property
    def PhysicalNets(self):
        return self.obj.PhysicalNets

    @property
    def ElecNets(self):
        return self.obj.ElecNets

    @property
    def Pins(self):
        return self.obj.Pins

    @property
    def Vias(self):
        return self.obj.Vias

    @property
    def ObjectLists(self):
        return self.obj.ObjectLists

    @property
    def AreaFills(self):
        return self.obj.AreaFills

    @property
    def DiffPinPairModels(self):
        return self.obj.DiffPinPairModels

    @property
    def SeriesPinPairModels(self):
        return self.obj.SeriesPinPairModels

    @property
    def NetClasses(self):
        return self.obj.NetClasses

    @property
    def CouplingAssignments(self):
        return self.obj.CouplingAssignments

    @property
    def ComponentModels(self):
        return self.obj.ComponentModels

    @property
    def PinModels(self):
        return self.obj.PinModels

    @property
    def EnclosureModels(self):
        return self.obj.EnclosureModels

    @property
    def PackageModels(self):
        return self.obj.PackageModels

    @property
    def PinDeviceModels(self):
        return self.obj.PinDeviceModels

    @property
    def ViolationTypePrefix(self):
        return self.obj.ViolationTypePrefix

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def Format(self):
        return self.obj.Format

    @property
    def ViolationTypes(self):
        return self.obj.ViolationTypes

    @property
    def Application(self):
        return self.obj.Application

    @property
    def MountingHoles(self):
        return self.obj.MountingHoles

    @property
    def Holes(self):
        return self.obj.Holes

    @property
    def ConductiveTexts(self):
        return self.obj.ConductiveTexts

    @property
    def Schematics(self):
        return self.obj.Schematics

    @property
    def Planes(self):
        return self.obj.Planes

    @property
    def Contours(self):
        return self.obj.Contours

    @property
    def Fiducials(self):
        return self.obj.Fiducials

    @property
    def ElecNetDiffPairs(self):
        return self.obj.ElecNetDiffPairs

    @property
    def ViolationGroups(self):
        return self.obj.ViolationGroups

    @property
    def UnroutedSegments(self):
        return self.obj.UnroutedSegments

    @property
    def ModelIndex(self):
        return self.obj.ModelIndex

    @property
    def Save(self):
        return self.obj.Save

    @property
    def SaveAs(self):
        return self.obj.SaveAs

    @property
    def NewCircle(self):
        return self.obj.NewCircle

    @property
    def NewSegment(self):
        return self.obj.NewSegment

    @property
    def NewRect(self):
        return self.obj.NewRect

    @property
    def NewCollection(self):
        return self.obj.NewCollection

    @property
    def NewDBCollection(self):
        return self.obj.NewDBCollection

    @property
    def NewAnnotation(self):
        return self.obj.NewAnnotation

    @property
    def NewComponentModel(self):
        return self.obj.NewComponentModel

    @property
    def NewPinDeviceModel(self):
        return self.obj.NewPinDeviceModel

    @property
    def NewPackageModel(self):
        return self.obj.NewPackageModel

    @property
    def NewEnclosureModel(self):
        return self.obj.NewEnclosureModel

    @property
    def NewPathFinder(self):
        return self.obj.NewPathFinder

    @property
    def GetViolationType(self):
        return self.obj.GetViolationType

    @property
    def NewVector(self):
        return self.obj.NewVector

    @property
    def NewSetupWizard(self):
        return self.obj.NewSetupWizard

    @property
    def NewGeometries(self):
        return self.obj.NewGeometries

    @property
    def NewTextReport(self):
        return self.obj.NewTextReport

    @property
    def NewMeasureEngine(self):
        return self.obj.NewMeasureEngine

    @property
    def NewFieldSolver(self):
        return self.obj.NewFieldSolver

    @property
    def NewCrossSectionBuilder(self):
        return self.obj.NewCrossSectionBuilder

    @property
    def GetRules(self):
        return self.obj.GetRules

    @property
    def NewRule(self):
        return self.obj.NewRule

    @property
    def NewObjectList(self):
        return self.obj.NewObjectList

    @property
    def NewViolationGroup(self):
        return self.obj.NewViolationGroup

    @property
    def NewObjectStorage(self):
        return self.obj.NewObjectStorage

    @property
    def Path(self):
        return self.obj.Path

