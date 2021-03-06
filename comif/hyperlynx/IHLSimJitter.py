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

class IHLSimJitter(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def Gaussian(self):
        return self.obj.Gaussian

    @property
    def GaussianFreq(self):
        return self.obj.GaussianFreq

    @Gaussian.setter
    def Gaussian(self, Gaussian):
        self.obj.Gaussian=Gaussian

    @property
    def Uniform(self):
        return self.obj.Uniform

    @GaussianFreq.setter
    def GaussianFreq(self, GaussianFreq):
        self.obj.GaussianFreq=GaussianFreq

    @property
    def UniformMean(self):
        return self.obj.UniformMean

    @Uniform.setter
    def Uniform(self, Uniform):
        self.obj.Uniform=Uniform

    @property
    def Sine(self):
        return self.obj.Sine

    @UniformMean.setter
    def UniformMean(self, UniformMean):
        self.obj.UniformMean=UniformMean

    @property
    def SineInitPhase(self):
        return self.obj.SineInitPhase

    @Sine.setter
    def Sine(self, Sine):
        self.obj.Sine=Sine

    @property
    def SineFreq(self):
        return self.obj.SineFreq

    @SineInitPhase.setter
    def SineInitPhase(self, SineInitPhase):
        self.obj.SineInitPhase=SineInitPhase

    @property
    def Distortion(self):
        return self.obj.Distortion

    @SineFreq.setter
    def SineFreq(self, SineFreq):
        self.obj.SineFreq=SineFreq

    @Distortion.setter
    def Distortion(self, Distortion):
        self.obj.Distortion=Distortion

