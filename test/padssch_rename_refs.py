# coding=utf-8
"""
demo
"""
import os
import sys
import configparser
import traceback

sys.path.append("..") 
from comif import *

__author__ = 'SayCV'

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
SRC_DIR = os.path.dirname(SCRIPTS_DIR)

_mputils_ = mputils()
App=_mputils_.PADSSCHApplication()

App.Visible=True
App.StatusBarText="Hello from python: " + __author__ + "@" + str(datetime.datetime.now())

schFile="demo.sch"
