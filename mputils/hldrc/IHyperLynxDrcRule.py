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

class IHyperLynxDrcRule(object):
    def __init__(self, obj=None):
        self.obj = obj


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
    def NetClasses(self):
        return self.obj.NetClasses

    @property
    def ComponentModels(self):
        return self.obj.ComponentModels

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
    def Parameters(self):
        return self.obj.Parameters

    @property
    def SchNets(self):
        return self.obj.SchNets

    @property
    def SchComponents(self):
        return self.obj.SchComponents

    @property
    def SchSheets(self):
        return self.obj.SchSheets

    @property
    def ElecNetDiffPairs(self):
        return self.obj.ElecNetDiffPairs

    @property
    def Violations(self):
        return self.obj.Violations

    @property
    def RuleViolations(self):
        return self.obj.RuleViolations

    @property
    def ParentRule(self):
        return self.obj.ParentRule

    @property
    def Components(self):
        return self.obj.Components

    @property
    def Author(self):
        return self.obj.Author

    @ParentRule.setter
    def ParentRule(self, ParentRule):
        self.obj.ParentRule=ParentRule

    @property
    def Version(self):
        return self.obj.Version

    @Author.setter
    def Author(self, Author):
        self.obj.Author=Author

    @property
    def Description(self):
        return self.obj.Description

    @Version.setter
    def Version(self, Version):
        self.obj.Version=Version

    @property
    def ExecutionOrder(self):
        return self.obj.ExecutionOrder

    @Description.setter
    def Description(self, Description):
        self.obj.Description=Description

    @property
    def AppliedObjectList(self):
        return self.obj.AppliedObjectList

    @ExecutionOrder.setter
    def ExecutionOrder(self, ExecutionOrder):
        self.obj.ExecutionOrder=ExecutionOrder

    @property
    def Rank(self):
        return self.obj.Rank

    @AppliedObjectList.setter
    def AppliedObjectList(self, AppliedObjectList):
        self.obj.AppliedObjectList=AppliedObjectList

    @property
    def Score(self):
        return self.obj.Score

    @property
    def ScriptFile(self):
        return self.obj.ScriptFile

    @Rank.setter
    def Rank(self, Rank):
        self.obj.Rank=Rank

    @property
    def Documentation(self):
        return self.obj.Documentation

    @ScriptFile.setter
    def ScriptFile(self, ScriptFile):
        self.obj.ScriptFile=ScriptFile

    @property
    def Group(self):
        return self.obj.Group

    @property
    def Compiled(self):
        return self.obj.Compiled

    @property
    def Execute(self):
        return self.obj.Execute

    @property
    def SetName(self):
        return self.obj.SetName

    @property
    def GetChildRules(self):
        return self.obj.GetChildRules

    @property
    def AddParameter(self):
        return self.obj.AddParameter

    @property
    def Delete(self):
        return self.obj.Delete

    @Documentation.setter
    def Documentation(self, Documentation):
        self.obj.Documentation=Documentation
