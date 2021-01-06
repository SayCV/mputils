# -*- coding: UTF-8 -*-
# 
# =====
# SPDX-License-Identifier: (GPL-2.0+ OR MIT):
# 
# !!! THIS IS NOT GUARANTEED TO WORK !!!
# 
# Copyright (c) 2018-2020, SayCV
# =====
# 

import re
import sys
import traceback
import os
import logging
import colorlog
import functools

sys.path.append("..") 
from comif import *

sys.path.append(os.environ.get('MPUTILS_ROOTDIR'))

__author__ = 'SayCV'

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/")
SRC_DIR=os.path.dirname(SCRIPTS_DIR)

# ----------------------------------------------------------------------------------------------------
# ====================================================================================================

refdes_control_required=False

#
# Refdes control required
# Scope
#   Update entire design
#   Update selection
# Action
#   Reset part references to "?"
#   Incremental reference update
# Annotation Type
#   Left-Right
#   Top-Bottom
#

plogAnnotationScopeUpdateEntireDesign = 0
plogAnnotationScopeUpdateSelection = 1
plogAnnotationActionResetReferenceToQuestionMark = 2
plogAnnotationActionIncrementalReferenceUpdate = 3
plogAnnotationTypeLeftRight = 4
plogAnnotationTypeTopBottom = 5

plogMultiPartPkgs=[]

PY3 = sys.version_info[0] == 3

log_colors_config = {
    'DEBUG': 'cyan',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'red',
}

def get_logger(name=None, filename=None, filemode=None, level=logging.WARNING):
    logger = logging.getLogger(name)
    if not getattr(logger, '_init_done', None):
        logger._init_done = True
        if filename:
            mode = filemode if filemode else 'a'
            hdlr = logging.FileHandler(filename, mode)
        else:
            hdlr = logging.StreamHandler() # pylint: disable=redefined-variable-type
            # the `_Formatter` contain some escape character to
            # represent color, which is not suitable for FileHandler,
            # (TODO) maybe we can add another Formatter for FileHandler.
            # hdlr.setFormatter(_Formatter())
            hdlr.setFormatter(colorlog.ColoredFormatter(
            fmt = '%(log_color)s%(asctime)s [%(levelname)s] %(message)s',
            datefmt = '%Y-%m-%d %X',
            log_colors = log_colors_config))
        logger.addHandler(hdlr)
        logger.setLevel(level)
    return logger

logger = get_logger(level=logging.DEBUG)

# ----------------------------------------------------------------------------------------------------
# ====================================================================================================

def PreprocessSheetComponents(Sheet=None, reftypelist=None, reseted=False):
    complist = []
    # reftypelist = {}
    for Comp in Sheet.Components:
        comp = IPowerLogicComp(Comp)
        # comp.selected = True
        gates = comp.Gates
        #if gates.Count > 1:
        #    logger.warning("More than one gate: %s!" % comp.Name)
        gate = gates[0]
        tmp_px = gate.PositionX
        tmp_py = gate.PositionY
        # comp.selected = False

        prefixref = None
        if reseted:
            prefixref = re.compile(u'[a-zA-Z]*').findall(comp.Name)[0]
            try:
                if len(prefixref)>1 and prefixref[1].isalpha():
                    prefixref = prefixref[1:]
            except IndexError as e:
                logging.error(prefixref, comp.Name, comp.PartType)
                logging.error(e.args)
                traceback.print_exc()
        else:
            prefixref = re.compile(u'[a-zA-Z]*').findall(comp.Name)[0]

        newcomp = {}
        newcomp["obj"] = comp
        newcomp["oldref"] = comp.Name
        newcomp["newref"] = None
        newcomp["px"] = int(tmp_px)
        newcomp["py"] = int(tmp_py)
        newcomp["prefixref"] = prefixref
        newreftype = {}
        if not newcomp["prefixref"] in reftypelist:
            newreftype["count"] = 1
            newreftype["index"] = 1
            reftypelist[newcomp["prefixref"]] = newreftype
        else:
            reftypelist[newcomp["prefixref"]]["count"] = reftypelist[newcomp["prefixref"]]["count"] + 1

        found_part = False
        if gates.Count > 1:
            logger.warning("More than one gate: %d x %s!" % (gates.Count, comp.Name))
            for _multicomp in plogMultiPartPkgs:
                if _multicomp["oldref"] == comp.Name:
                    found_part = True
                    break
            plogMultiPartPkgs.append(newcomp)
        found_part = False
        if found_part:
            logger.warning("Ignoring: %s!" % comp.Name)
            continue
        
        complist.append(newcomp)
    return complist

def ResetRefSheetComponents(complist=None):
    for comp in complist:
        plogComp = IPowerLogicComp(comp["obj"])
        if plogComp.Gates.Count > 1 and (plogComp.Name.startswith("X") and len(plogComp.Name)>1 and not plogComp.Name.startswith("X", 1)):
            continue
        newref = "X" + comp["oldref"]
        #if comp["oldref"].startswith("X"):
        #    continue

        try:
            plogComp.Name = newref
        except BaseException as e: # to catch pywintypes.error
            logging.error(e.args)
            logging.error(comp["oldref"])
        
    return complist

def SortRefSheetComponents(complist=None, reftypelist=None, sorttype=plogAnnotationTypeLeftRight):
    # return -1 - [a, b] 不交换
    # return  1 - [a, b] 交换
    # return  0 - [a, b] 相等不交换
    # ymax xmin -> xmax
    # ymin xmin -> xmax
    def mySortedLeftRight(a, b): # y 逆序 -> x 顺序
        if a["py"] < b["py"]:
            return  1 # b, a
        if a["px"] < b["px"]:
            return -1 # a, b
        return 0  # a = b
    def mySorteTopBottom(a, b): # x 顺序 -> y 逆序
        if a["px"] < b["px"]:
            return -1 # a, b
        if a["py"] < b["py"]:
            return 1 # b, a
        return 0  # a = b
    def custom_sorted(a, b):
        if sorttype == plogAnnotationTypeLeftRight:
            return mySortedLeftRight(a, b)
        return mySorteTopBottom(a, b)
    complist = sorted(complist, key=functools.cmp_to_key(custom_sorted))
    for idx,comp in enumerate(complist):
        plogComp = IPowerLogicComp(comp["obj"])
        newref = comp["prefixref"] + str(reftypelist[comp["prefixref"]]["index"])
        
        if plogComp.Gates.Count > 1 and not plogComp.Name.startswith("X", 0):
            continue

        try:
            plogComp.Name = newref
        except BaseException as e: # to catch pywintypes.error
            logging.error(e.args)
            logging.error(comp["oldref"])
        
        comp["newref"] = newref
        reftypelist[comp["prefixref"]]["index"] = reftypelist[comp["prefixref"]]["index"] + 1
    return complist

# ----------------------------------------------------------------------------------------------------
# ====================================================================================================

def main():
    logger.info("Waiting for processing to finish ...")
    schfn = os.environ.get('SCH_FN')
    if schfn is None:
        # _schfn, _ = os.path.splitext(os.path.basename(__file__))
        schfn = SCRIPTS_DIR + "/demo"

    logger.info("The processing file is %s.sch" % (schfn))

    _mputils_ = mputils()
    App = _mputils_.PADSSCHApplication()

    App.Visible = True
    App.StatusBarText = "Hello from python: " + \
        __author__ + "@" + str(datetime.datetime.now())
    logger.debug("Version: %s" % App.Version)

    schFile = schfn + ".sch"
    if not os.path.exists(schFile):
        App.Quit()
        raise Exception("Invalid schFile!")

    Document = IPowerLogicDoc(App.OpenDocument(schFile))
    if Document is None:
        App.Quit()
        raise Exception("Invalid document!")

    Sheets = Document.Sheets
    logger.debug("SheetsTotalCount: %d", Sheets.Count)

    complist = []
    reftypelist = {}
    for idx, Sheet in enumerate(Sheets):
        logger.info("1st Processing Sheets %d: %s" % (idx+1, Sheet.Name))
        sheet = IPowerLogicSheet(Sheet)
        _complist = PreprocessSheetComponents(sheet, reftypelist)
        ResetRefSheetComponents(_complist)
        # complist.extend(_complist)
        # sys.exit()

    complist = []
    reftypelist = {}
    for idx, Sheet in enumerate(Sheets):
        logger.info("2nd Processing Sheets %d: %s" % (idx+1, Sheet.Name))
        sheet = IPowerLogicSheet(Sheet)
        _complist = PreprocessSheetComponents(sheet, reftypelist, reseted=True)
        _complist = SortRefSheetComponents(_complist, reftypelist)
        complist.extend(_complist)
        # sys.exit()

    for comp in complist:
        print("%06s %06s %10.2f %10.2f" %
            (comp["obj"].Name, comp["oldref"], comp["px"], comp["py"]))
    
    Document.SaveAsTemp(schfn + ".rrefs.tmp.sch")
    App.Quit()
    logger.debug("finished")

if(__name__ == '__main__'):
    main()
