# coding=utf-8
"""
This file is autogenerated by python script @ 20200808-20:13:09
"""
import sys
import os
import datetime,time

#from PowerPCBEnums import *

__author__ = 'SayCV'

import logging

logger = logging.getLogger(__name__)

class IHLSParamExtractor(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def MinFreq(self):
        return self.obj.MinFreq

    @property
    def Ports(self):
        return self.obj.Ports

    @property
    def MaxFreq(self):
        return self.obj.MaxFreq

    @MinFreq.setter
    def MinFreq(self, MinFreq):
        self.obj.MinFreq=MinFreq

    @property
    def FreqSweepType(self):
        return self.obj.FreqSweepType

    @MaxFreq.setter
    def MaxFreq(self, MaxFreq):
        self.obj.MaxFreq=MaxFreq

    @property
    def StepCount(self):
        return self.obj.StepCount

    @FreqSweepType.setter
    def FreqSweepType(self, FreqSweepType):
        self.obj.FreqSweepType=FreqSweepType

    @property
    def StepPerDecade(self):
        return self.obj.StepPerDecade

    @StepCount.setter
    def StepCount(self, StepCount):
        self.obj.StepCount=StepCount

    @property
    def Tolerance(self):
        return self.obj.Tolerance

    @StepPerDecade.setter
    def StepPerDecade(self, StepPerDecade):
        self.obj.StepPerDecade=StepPerDecade

    @property
    def RefImpedance(self):
        return self.obj.RefImpedance

    @Tolerance.setter
    def Tolerance(self, Tolerance):
        self.obj.Tolerance=Tolerance

    @property
    def Extract(self):
        return self.obj.Extract

    @RefImpedance.setter
    def RefImpedance(self, RefImpedance):
        self.obj.RefImpedance=RefImpedance

