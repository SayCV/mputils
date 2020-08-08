# coding=utf-8
"""
This file is autogenerated by python script @ 20200726-10:57:03
"""
import sys
import os

__author__ = 'SayCV'



# PPcbObjectType
# PADS Layout Database Object Types Constants


ppcbObjectTypeUnknown = 0

ppcbObjectTypeComponent = 1

ppcbObjectTypeNet = 2

ppcbObjectTypePin = 3

ppcbObjectTypeVia = 4

ppcbObjectTypeConnection = 5

ppcbObjectTypeRouteSegment = 6

ppcbObjectTypeJumper = 7

ppcbObjectTypePartType = 8

ppcbObjectTypeCBP = 9

ppcbObjectTypeSBP = 10

ppcbObjectTypeWirebond = 11

ppcbObjectTypeNetClass = 12

ppcbObjectTypeDrawing = 13

ppcbObjectTypeText = 14

ppcbObjectTypeLabel = 15

ppcbObjectTypePolyline = 16

ppcbObjectTypeCircle = 17

ppcbObjectTypeLibrary = 18

ppcbObjectTypeLibraryItem = 19

ppcbObjectTypeAll = 9999

ppcbObjectTypeApplication = 20

ppcbObjectTypeAttribute = 21

ppcbObjectTypeAttributeType = 22

ppcbObjectTypeDocument = 23

ppcbObjectTypeMeasure = 24

ppcbObjectTypeView = 25

ppcbObjectTypeAssemblyOptions = 26

ppcbObjectTypeAttributes = 27

ppcbObjectTypeAttributeTypes = 28

ppcbObjectTypeDecal = 29

ppcbObjectTypeObjects = 30

ppcbObjectTypePadStackLayer = 31

ppcbObjectTypePad = 32

ppcbObjectTypeThermalPad = 33

ppcbObjectTypeAntiPad = 34

ppcbObjectTypeLayer = 35

ppcbObjectTypeError = 36

ppcbObjectTypeErrorConflict = 37

ppcbObjectTypeAssociatedNet = 38




# PPcbUnit
# PADS Layout Unit Constants


ppcbUnitCurrent = 0

ppcbUnitDatabase = 1

ppcbUnitMils = 2

ppcbUnitInch = 3

ppcbUnitMetric = 4




# PPcbMeasureFormat
# PADS Layout Measure Format Constants


ppcbMeasureFormatStandard = 0

ppcbMeasureFormatCurrent = 1

ppcbMeasureFormatShort = 2

ppcbMeasureFormatLong = 3




# PPcbLibraryItemType
# PADS Layout Library Item Type Constants


ppcbLibraryItemTypePartType = 0

ppcbLibraryItemTypeDecal = 1

ppcbLibraryItemTypeLogicDrawing = 2

ppcbLibraryItemTypeDrawing = 3

ppcbLibraryItemTypeAll = 9999




# PPcbImportLibMode
# PADS Layout Library Import Type Constants


ppcbImportLibModeSilentOverwrite = 1

ppcbImportLibModeNoLocalOverwrite = 2

ppcbImportLibModeNoGlobalOverwrite = 3

ppcbImportLibModePromptLocalOverwrite = 4

ppcbImportLibModePromptGlobalOverwrite = 5




# PPcbLayerType
# PADS Layout Layer Type Constants


ppcbLayerUnknown = 0

ppcbLayerComponent = 1

ppcbLayerRouting = 2

ppcbLayerDrill = 3

ppcbLayerSilkscreen = 4

ppcbLayerPasteMask = 5

ppcbLayerSolderMask = 6

ppcbLayerAssembly = 7

ppcbLayerGeneral = 8

ppcbLayerAll = 9999




# PPcbDocumentColor
# PADS Layout Document Color


ppcbDocumentColorBackground = 0

ppcbDocumentColorSelection = 1

ppcbDocumentColorHighlight = 2

ppcbDocumentColorBoardOutline = 3

ppcbDocumentColorConnection = 4




# PPcbDesignObject
# PADS Layout Design Object


ppcbDesignObjectTrace = 0

ppcbDesignObjectVia = 1

ppcbDesignObjectPad = 2

ppcbDesignObjectCopper = 3

ppcbDesignObjectLine = 4

ppcbDesignObjectText = 5

ppcbDesignObjectError = 6

ppcbDesignObjectOutlineTop = 7

ppcbDesignObjectOutlineBottom = 8

ppcbDesignObjectRefDes = 9

ppcbDesignObjectPartType = 10

ppcbDesignObjectAttribute = 11

ppcbDesignObjectKeepout = 12

ppcbDesignObjectPinNumber = 13




# PPcbGridType
# PADS Layout Grid Type Constants


ppcbGridNone = 0

ppcbGridDesign = 1

ppcbGridVia = 2

ppcbGridDisplay = 3

ppcbGridAll = 9999




# PPcbASCIIVersion
# PADS Layout ASCII Version Constants


ppcbASCIIVerCurrent = 0

ppcbASCIIVer1_1 = 2

ppcbASCIIVer1_5 = 3

ppcbASCIIVer2_0 = 4

ppcbASCIIVer2_1 = 5

ppcbASCIIVer3_0 = 7

ppcbASCIIVer3_5 = 8

ppcbASCIIVer4_0 = 9

ppcbASCIIVer5_0 = 10

ppcbASCIIVer2005 = 11

ppcbASCIIVer2005_2 = 12

ppcbASCIIVer2007 = 13

ppcbASCIIVer9_0 = 14

ppcbASCIIVer9_2 = 15

ppcbASCIIVer9_3 = 16

ppcbASCIIVer9_4 = 17

ppcbASCIIVer9_5 = 18

ppcbASCIIVer10_0 = 19




# PPcbASCIISections
# PADS Layout ASCII File Sections


ppcbASCIISectionPCB = 1

ppcbASCIISectionReuse = 2

ppcbASCIISectionText = 4

ppcbASCIISectionLines = 8

ppcbASCIISectionClusters = 16

ppcbASCIISectionVias = 32

ppcbASCIISectionDecals = 64

ppcbASCIISectionPartTypes = 128

ppcbASCIISectionParts = 256

ppcbASCIISectionJumpers = 512

ppcbASCIISectionConnections = 1024

ppcbASCIISectionRoutes = 2048

ppcbASCIISectionTeardrops = 4096

ppcbASCIISectionMisc = 8192

ppcbASCIISectionRules = 16384

ppcbASCIISectionCAM = 32768

ppcbASCIISectionPour = 0x00010000

ppcbASCIISectionAssemblyOptions = 0x00020000

ppcbASCIISectionTestPoints = 0x00040000

ppcbASCIISectionAttributes = 0x00080000

ppcbASCIISectionAll = 0xffffffff




# PPcbAttrFlags
# PADS Layout Attribute Flags


ppcbAttrNone = 0

ppcbAttrPart = 1

ppcbAttrNet = 2

ppcbAttrPin = 4

ppcbAttrVia = 8

ppcbAttrPCB = 16

ppcbAttrPartType = 32

ppcbAttrDecal = 64

ppcbAttrNetClass = 128

ppcbAttrAll = 0xffffffff




# PPcbOriginType
# PADS Layout Origin Type Constants


ppcbOriginTypeDesign = 0

ppcbOriginTypeParent = 1




# PPcbHorizontalJustification
# PADS Layout Horizontal Justification Constants


ppcbJustifyLeft = 0

ppcbJustifyHCenter = 1

ppcbJustifyRight = 2




# PPcbVerticalJustification
# PADS Layout Vertical Justification Constants


ppcbJustifyTop = 0

ppcbJustifyVCenter = 1

ppcbJustifyBottom = 2




# PPcbDrawingType
# PADS Layout Drawing Type Constants


ppcbDrw2Dline = 0

ppcbDrwBoard = 1

ppcbDrwCopper = 3

ppcbDrwCopperPour = 6

ppcbDrwCopperHatch = 7

ppcbDrwCopperThermal = 8

ppcbDrwKeepout = 9




# PPcbLabelType
# PADS Layout Label Type Constants


ppcbLabelTypeRefDesignator = 0

ppcbLabelTypePartType = 1

ppcbLabelTypeAttribute = 2




# PPcbLabelDisplayMode
# PADS Layout Label Display Mode Constants


ppcbLabelDisplayNone = 0

ppcbLabelDisplayValue = 1

ppcbLabelDisplayNameAndValue = 2

ppcbLabelDisplayFullNameAndValue = 3




# PPcbRightReadingStatus
# PADS Layout Right Reading Status Constants


ppcbRightReadingNone = 0

ppcbRightReadingOrthogonal = 1

ppcbRightReadingAngled = 2




# PPcbTestPointType
# PADS Layout Test Point Type Constants


ppcbTestPointNone = 0

ppcbTestPointTopLayer = 1

ppcbTestPointBottomLayer = 2




# PPcbPinElectricalType
# PADS Layout Pin Electrical Type Constants


ppcbElectricalTypeUnknown = 0

ppcbElectricalTypeSource = 1

ppcbElectricalTypeBidirectional = 2

ppcbElectricalTypeOpenCollector = 3

ppcbElectricalTypeOrTieableSource = 4

ppcbElectricalTypeTristate = 5

ppcbElectricalTypeLoad = 6

ppcbElectricalTypeTerminator = 7

ppcbElectricalTypePower = 8

ppcbElectricalTypeGround = 9




# PPcbSegmentType
# PADS Layout Segment Type Constants


ppcbSegmentUnknown = 0

ppcbSegmentLine = 1

ppcbSegmentArc = 2




# PPcbBondPadShape
# PowerBGA Bond Pad Shape Constants


ppcbBondPadShapeUnknown = 0

ppcbBondPadShapeRectangle = 1

ppcbBondPadShapeOval = 2




# PPcbBondPadEdge
# PowerBGA Bond Pad Edge Constants


ppcbBondPadEdgeUnknown = 0

ppcbBondPadEdgeLeft = 1

ppcbBondPadEdgeTop = 2

ppcbBondPadEdgeRight = 3

ppcbBondPadEdgeBottom = 4




# PPcbOutlineType
# PADS Layout Outline Type Constants


ppcbOutlineTypeCenter = 0

ppcbOutlineTypeOuter = 1

ppcbOutlineTypeInner = 2




# PPcbShapeType
# PADS Layout Shape Type Constants


ppcbShapeTypeOpen = 0

ppcbShapeTypeHollow = 1

ppcbShapeTypeFilled = 2

ppcbShapeTypeVoid = 3




# PPcbPadShape
# PADS Layout Pad Shape


ppcbPadShapeOvalFinger = 0

ppcbPadShapeRectangularFinger = 1

ppcbPadShapeRound = 2

ppcbPadShapeSquare = 3

ppcbPadShapeAnnular = 4

ppcbPadShapeOdd = 5




# PPcbPadCornerType
# PADS Layout Pad Corner Type


ppcbPadCornerType90Degree = 0

ppcbPadCornerTypeChamfered = 1

ppcbPadCornerTypeRounded = 2




# PPcbThermalPadShape
# PADS Layout Thermal Pad Shape


ppcbThermalPadShapeRound = 6

ppcbThermalPadShapeSquare = 7




# PPcbAntiPadShape
# PADS Layout Anti Pad Shape


ppcbAntiPadShapeRound = 8

ppcbAntiPadShapeSquare = 9




# PPcbPlaneType
# PADS Layout Plane Type


ppcbPlaneTypeNoPlane = 0

ppcbPlaneTypeCAMPlane = 1

ppcbPlaneTypeSplitMixedPlane = 2




# PPcbRoutingDirection
# PADS Layout Routing Direction


ppcbRoutingDirectionHorizontal = 0

ppcbRoutingDirectionVertical = 1

ppcbRoutingDirectionAny = 2

ppcbRoutingDirectionDiagonal45 = 3

ppcbRoutingDirectionDiagonal135 = 4




# PPcbDielectricLayer
# PADS Layout Dielectric Layer


ppcbDielectricLayerAbove = 0

ppcbDielectricLayerBelow = 1




# PPcbDielectricType
# PADS Layout Dielectric Type


ppcbDielectricTypeCoating = 0

ppcbDielectricTypeSubstrate = 1

ppcbDielectricTypePrepreg = 2




# PPcbLayerColor
# PADS Layout Layer Color


ppcbLayerColorTrace = 0

ppcbLayerColorVia = 1

ppcbLayerColorPad = 2

ppcbLayerColorCopper = 3

ppcbLayerColorLine = 4

ppcbLayerColorText = 5

ppcbLayerColorError = 6

ppcbLayerColorOutlineTop = 7

ppcbLayerColorOutlineBottom = 8

ppcbLayerColorRefDes = 9

ppcbLayerColorPartType = 10

ppcbLayerColorAttribute = 11

ppcbLayerColorKeepout = 12

ppcbLayerColorPinNumber = 13




# PPcbErrorType
# PADS Layout Error Type


ppcbErrorTypePadToPadError = 0

ppcbErrorTypePadToTrackError = 1

ppcbErrorTypeTrackToTrackError = 2

ppcbErrorTypeCopperPourError = 3

ppcbErrorTypeDrillHoleError = 4

ppcbErrorTypeDrillToDrillError = 5

ppcbErrorTypeTraceWidthError = 6

ppcbErrorTypePlacementKeepoutError = 7

ppcbErrorTypeHeightKeepoutError = 8

ppcbErrorTypeDrillKeepoutError = 9

ppcbErrorTypeTraceKeepoutError = 10

ppcbErrorTypePourKeepoutError = 11

ppcbErrorTypeViaKeepoutError = 12

ppcbErrorTypeTestPointKeepoutError = 13

ppcbErrorTypeBoardOutlineError = 14

ppcbErrorTypeSameNetPadToPadError = 15

ppcbErrorTypeSameNetPadToTrackError = 16

ppcbErrorTypeBodyToBodyError = 17

ppcbErrorTypeConnectivityError = 32

ppcbErrorTypeConnectivityDrillError = 33

ppcbErrorTypeConnectivityPlaneError = 34

ppcbErrorTypeDrillLayerPairingError = 35

ppcbErrorTypeDrillToPlaneShortError = 36

ppcbErrorTypeEDC_CapacitanceError = 64

ppcbErrorTypeEDC_LengthError = 65

ppcbErrorTypeEDC_DelayError = 66

ppcbErrorTypeEDC_MinImpedanceError = 67

ppcbErrorTypeEDC_MaxImpedanceError = 68

ppcbErrorTypeEDC_LoopError = 69

ppcbErrorTypeEDC_StubError = 70

ppcbErrorTypeEDC_ParallelismError = 71

ppcbErrorTypeTiePlaneError = 96

ppcbErrorTypeTearDropGenError = 97

ppcbErrorTypeLatiumMarkerError = 98

ppcbErrorTypeBLZ_ViaAtSMDFitInsideError = 99

ppcbErrorTypeBLZ_ViaAtSMDCenterError = 100

ppcbErrorTypeBLZ_ViaAtSMDEndError = 101

ppcbErrorTypeBLZ_ViaAtSMDCenterOutError = 102

ppcbErrorTypeBLZ_ViaAtSMDTooManyError = 103

ppcbErrorTypeBLZ_GapBadError = 104

ppcbErrorTypeBLZ_GapViolationError = 105

ppcbErrorTypeBLZ_GapObstacleSizeError = 106

ppcbErrorTypeBLZ_GapObstacleCountError = 107

ppcbErrorTypeBLZ_GapIrregularLengthError = 108

ppcbErrorTypeBLZ_GapControlledPercentError = 109

ppcbErrorTypeBLZ_LengthToleranceError = 110

ppcbErrorTypeBLZ_ProfileCornerError = 111

ppcbErrorTypeBLZ_GapSeparationDistanceError = 112

ppcbErrorTypeTestPointGenError = 128

ppcbErrorTypeTestPointProbeToProbeError = 129

ppcbErrorTypeTestPointProbeToComponentError = 130

ppcbErrorTypeTestPointProbeToBoardError = 131

ppcbErrorTypeTestPointProbeToKeepoutError = 132

ppcbErrorTypeTestPointNailCountError = 133

ppcbErrorTypeBLZ_ProbeNotComponentError = 134

ppcbErrorTypeBLZ_ProbeOnSMDPinError = 135

ppcbErrorTypeBLZ_ProbeGridError = 136

ppcbErrorTypeBLZ_ProbeNailDiameterError = 137

ppcbErrorTypeBLZ_ProbeToPadError = 138

ppcbErrorTypeBLZ_ProbeToTraceError = 139

ppcbErrorTypeDFMGenError = 160

ppcbErrorTypeDFMAcidTrapError = 161

ppcbErrorTypeDFMSliverError = 162

ppcbErrorTypeDFMSolderBridgeError = 163

ppcbErrorTypeDFMStarvedThermalError = 164

ppcbErrorTypeDFMLayerCompareError = 165

ppcbErrorTypeDFMDrillError = 166

ppcbErrorTypeDFFGenError = 167

ppcbErrorTypeDFFAcidTrapError = 168

ppcbErrorTypeDFFSliverError = 169

ppcbErrorTypeDFFSolderBridgeError = 170

ppcbErrorTypeDFFStarvedThermalError = 171

ppcbErrorTypeDFFLayerCompareError = 172

ppcbErrorTypeDFFDrillError = 173

ppcbErrorTypeDFFDrillToMaskError = 174

ppcbErrorTypeDFFPadToMaskError = 175

ppcbErrorTypeDFFDrillToPadError = 176

ppcbErrorTypeDFFTraceWidthError = 177

ppcbErrorTypeDFFPadSizeError = 178

ppcbErrorTypeBGA_GenError = 192

ppcbErrorTypeBGA_WBRMinLengthError = 193

ppcbErrorTypeBGA_WBRMaxLengthError = 194

ppcbErrorTypeBGA_WBRMaxAngleError = 195

ppcbErrorTypeBGA_WBRWBToWBError = 196

ppcbErrorTypeBGA_WBRWBToSBPError = 197

ppcbErrorTypeViaCountError = 224




# PPcbErrorClass
# PADS Layout Error Class


ppcbErrorClassClearanceError = 0

ppcbErrorClassConnectivityError = 32

ppcbErrorClassHighSpeedError = 64

ppcbErrorClassMiscError = 96

ppcbErrorClassTestPointError = 128

ppcbErrorClassDfmError = 160

ppcbErrorClassBgaError = 192

ppcbErrorClassViaCountError = 224




# PPcbErrorValueType
# PADS Layout Error Value Type


ppcbErrorValueTypeMeasure = 0

ppcbErrorValueTypeInt = 1

ppcbErrorValueTypeDouble = 2




# __MIDL___MIDL_itf_powerpcb_0001_0109_0001
# PADS Layout DRC Mode Type Constants


ppcbDRCNone = 0

ppcbDRCOff = 1

ppcbDRCWarn = 2

ppcbDRCIgnoreClearance = 3

ppcbDRCPrevent = 4




# __MIDL___MIDL_itf_powerpcb_0001_0109_0002
# PADS Layout Nudge Mode Type Constants


ppcbNudgeNone = 0

ppcbNudgeOff = 1

ppcbNudgeWarn = 2

ppcbNudgeAuto = 3




# PPcbPadStackLayerType
# PADS Layout Pad Stack Layer Type


ppcbPadStackLayerTypeMounted = 0xfffffffe

ppcbPadStackLayerTypeInner = 0xffffffff

ppcbPadStackLayerTypeOpposite = 0



