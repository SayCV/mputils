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

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
SRC_DIR = os.path.dirname(SCRIPTS_DIR)

App=HLApplication()

App.Visible=True
