# coding=utf-8
"""
demo
"""
import os
import sys
import re
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
print("Version", App.Version)

schFile = SCRIPTS_DIR + "/demo.sch"
print(schFile)
if not os.path.exists(schFile):
    App.Quit()
    raise Exception("Invalid schFile!")

Document = IPowerLogicDoc(App.OpenDocument(schFile))
if Document is None:
    App.Quit()
    raise Exception("Invalid document!")

Sheets = Document.Sheets
print("SheetsCount", Sheets.Count)

reRefPrefix = re.compile(u'[a-zA-Z]*')
refSuffix = []
for idx, Sheet in enumerate(Sheets):
    sheet = IPowerLogicSheet(Sheet)
    #print("Sheet%d" % (1 + idx), "ComponentsCount", sheet.Components.Count)
    refsOld = []
    refSuffixSheet = {}
    for Comp in sheet.Components:
        comp = IPowerLogicComp(Comp)
        refsOld.append(comp.Name)
        refPrefix = reRefPrefix.findall(comp.Name)[0]
        if not refPrefix in refSuffixSheet:
            refSuffixSheet[refPrefix] = (1 + idx) * 100   
        else:
            #refSuffixSheet[refPrefix] = (1 + refSuffixSheet[refPrefix])
            pass
    refSuffix.append(refSuffixSheet)
    print("RefsDesOld", refsOld)

for idx, Sheet in enumerate(Sheets):
    sheet = IPowerLogicSheet(Sheet)
    refsTmp = []
    refSuffixSheet = refSuffix[idx]
    for Comp in sheet.Components:
        comp = IPowerLogicComp(Comp)
        refPrefix = reRefPrefix.findall(comp.Name)[0]
        if not refPrefix in refSuffixSheet:
            refSuffixSheet[refPrefix] = (1 + idx) * 100   
        else:
            refSuffixSheet[refPrefix] = (1 + refSuffixSheet[refPrefix])
            pass
        comp.Name = "X%s%d" % (refPrefix, refSuffixSheet[refPrefix])
        refsTmp.append(comp.Name)
    refSuffix.append(refSuffixSheet)
    print("RefsDesTmp", refsTmp)

for idx, Sheet in enumerate(Sheets):
    sheet = IPowerLogicSheet(Sheet)
    #print("Sheet%d" % (1 + idx), "ComponentsCount", sheet.Components.Count)
    refsNew = []
    #refSuffixSheet = {}
    for Comp in sheet.Components:
        comp = IPowerLogicComp(Comp)
        comp.Name = comp.Name[1:]
        refsNew.append(comp.Name)

    print("RefsDesNew", refsNew)

    pass
