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

class IPowerPCBApp(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Application(self):
        return self.obj.Application

    @property
    def Parent(self):
        return self.obj.Parent

    @property
    def Version(self):
        return self.obj.Version

    @property
    def ActiveDocument(self):
        return self.obj.ActiveDocument

    @property
    def Name(self):
        return self.obj.Name

    @property
    def DefaultFilePath(self):
        return self.obj.DefaultFilePath

    @property
    def FullName(self):
        return self.obj.FullName

    @DefaultFilePath.setter
    def DefaultFilePath(self, DefaultFilePath):
        self.obj.DefaultFilePath=DefaultFilePath

    @property
    def Visible(self):
        return self.obj.Visible

    @Visible.setter
    def Visible(self, Visible):
        self.obj.Visible=Visible

    @property
    def Preference(self):
        return self.obj.Preference

    @Preference.setter
    def Preference(self, Preference):
        self.obj.Preference=Preference

    @property
    def StatusBarText(self):
        return self.obj.StatusBarText

    @property
    def BoardAreaValue(self):
        return self.obj.BoardAreaValue

    @property
    def ProgressBar(self):
        return self.obj.ProgressBar

    @StatusBarText.setter
    def StatusBarText(self, StatusBarText):
        self.obj.StatusBarText=StatusBarText

    @ProgressBar.setter
    def ProgressBar(self, ProgressBar):
        self.obj.ProgressBar=ProgressBar

    @property
    def CLibPath(self):
        return self.obj.CLibPath

    @CLibPath.setter
    def CLibPath(self, CLibPath):
        self.obj.CLibPath=CLibPath

    @property
    def CLibSearchScheme(self):
        return self.obj.CLibSearchScheme

    @CLibSearchScheme.setter
    def CLibSearchScheme(self, CLibSearchScheme):
        self.obj.CLibSearchScheme=CLibSearchScheme

    @property
    def CLibModeActive(self):
        return self.obj.CLibModeActive

    @CLibModeActive.setter
    def CLibModeActive(self, CLibModeActive):
        self.obj.CLibModeActive=CLibModeActive

    @property
    def FlowMigrated(self):
        return self.obj.FlowMigrated

    @property
    def OpenDocument(self):
        return self.obj.OpenDocument

    @property
    def Quit(self):
        return self.obj.Quit

    @property
    def RunMacro(self):
        return self.obj.RunMacro

    @property
    def StrNumCmp(self):
        return self.obj.StrNumCmp

    @property
    def MRU_Entry(self):
        return self.obj.MRU_Entry

    @property
    def MRU_EntryDisp(self):
        return self.obj.MRU_EntryDisp

    @FlowMigrated.setter
    def FlowMigrated(self, FlowMigrated):
        self.obj.FlowMigrated=FlowMigrated

