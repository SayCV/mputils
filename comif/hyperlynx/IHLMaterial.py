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

class IHLMaterial(object):
    def __init__(self, obj=None):
        self.obj = obj


    @property
    def RelativePermittivity(self):
        return self.obj.RelativePermittivity

    @property
    def LossTangent(self):
        return self.obj.LossTangent

    @RelativePermittivity.setter
    def RelativePermittivity(self, RelativePermittivity):
        self.obj.RelativePermittivity=RelativePermittivity

    @property
    def BulkResistivity(self):
        return self.obj.BulkResistivity

    @LossTangent.setter
    def LossTangent(self, LossTangent):
        self.obj.LossTangent=LossTangent

    @property
    def ResTempCoefficient(self):
        return self.obj.ResTempCoefficient

    @BulkResistivity.setter
    def BulkResistivity(self, BulkResistivity):
        self.obj.BulkResistivity=BulkResistivity

    @property
    def ThermalConductivity(self):
        return self.obj.ThermalConductivity

    @ResTempCoefficient.setter
    def ResTempCoefficient(self, ResTempCoefficient):
        self.obj.ResTempCoefficient=ResTempCoefficient

    @ThermalConductivity.setter
    def ThermalConductivity(self, ThermalConductivity):
        self.obj.ThermalConductivity=ThermalConductivity

