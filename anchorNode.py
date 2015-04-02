# anchorNode.py

import sys
import random

import maya.OpenMaya as OpenMaya
import maya.OpenMayaAnim as OpenMayaAnim
import maya.OpenMayaMPx as OpenMayaMPx
import maya.cmds as cmds

# Useful functions for declaring attributes as inputs or outputs.
def MAKE_INPUT(attr):
    attr.setKeyable(True)
    attr.setStorable(True)
    attr.setReadable(True)
    attr.setWritable(True)
    attr.setHidden(False)
def MAKE_OUTPUT(attr):
    attr.setKeyable(False)
    attr.setStorable(False)
    attr.setReadable(True)
    attr.setWritable(False)

# Define the name of the node
kPluginNodeTypeName = "anchorNode"

# Give the node a unique ID. Make sure this ID is different from all of your
# other nodes!
anchorNodeId = OpenMaya.MTypeId(0x8704)

# Node definition
class anchorNode(OpenMayaMPx.MPxNode):
    # Declare class variables:
    # TODO:: declare the input and output class variables
    #         i.e. inNumPoints = OpenMaya.MObject()
    inNumPoints = OpenMaya.MObject()
    randomPoints = OpenMaya.MObject()
    inMin = OpenMaya.MObject()
    inMax = OpenMaya.MObject()

    inPos = OpenMaya.MObject()
    objFile = OpenMaya.MObject()
     
    # constructor
    def __init__(self):
        OpenMayaMPx.MPxNode.__init__(self)

    # compute
    def compute(self,plug,data):
        # TODO:: create the main functionality of the node. Your node should 
        #         take in three floats for max position (X,Y,Z), three floats 
        #         for min position (X,Y,Z), and the number of random points to
        #         be generated. Your node should output an MFnArrayAttrsData 
        #         object containing the random points. Consult the homework
        #         sheet for how to deal with creating the MFnArrayAttrsData. 
        '''pointsData = data.outputValue(randomNode.randomPoints)
        pointsAAD = OpenMaya.MFnArrayAttrsData()
        pointsObject = pointsAAD.create()

        minpos = data.inputValue(randomNode.inMin).asFloat3()
        maxpos = data.inputValue(randomNode.inMax).asFloat3()
        numPts = data.inputValue(randomNode.inNumPoints).asLong()'''

        nodePos = data.inputValue(anchorNode.inPos).asFloat3()
        obj = data.inputValue(anchorNode.objFile).asString()
        print nodePos
        print obj
        print "aa"

        '''print "woop"
        #create position and id 
        positionArray = pointsAAD.vectorArray("position")
        idArray = pointsAAD.doubleArray("id")

        #fill in arrays
        for i in range(numPts):         
            posx = random.uniform(minpos[0], maxpos[0])
            posy = random.uniform(minpos[1], maxpos[1])
            posz = random.uniform(minpos[2], maxpos[2])
            myVec = OpenMaya.MVector(posx, posy, posz)
            positionArray.append(myVec)
            idArray.append(random.randint(1,1000))
            print "here"

        pointsData.setMObject(pointsObject)'''

        data.setClean(plug)
    
# initializer
def nodeInitializer():
    tAttr = OpenMaya.MFnTypedAttribute()
    nAttr = OpenMaya.MFnNumericAttribute()

    # TODO:: initialize the input and output attributes. Be sure to use the 
    #         MAKE_INPUT and MAKE_OUTPUT functions.
    
    '''randomNode.inNumPoints = nAttr.create("numPts", "nPt", OpenMaya.MFnNumericData.kLong)
    MAKE_INPUT(nAttr)
    randomNode.inMin = nAttr.create("Minimum", "min", OpenMaya.MFnNumericData.k3Float)
    MAKE_INPUT(nAttr)
    randomNode.inMax = nAttr.create("Maximum", "max", OpenMaya.MFnNumericData.k3Float)
    MAKE_INPUT(nAttr)
    randomNode.randomPoints = tAttr.create("RandomPoints", "rand", OpenMaya.MFnArrayAttrsData.kDynArrayAttrs)
    MAKE_OUTPUT(tAttr)'''

    stringData = OpenMaya.MFnStringData().create(" ")
    anchorNode.objFile = tAttr.create("Objfile", "obj", OpenMaya.MFnData.kString, stringData)
    MAKE_INPUT(tAttr)
    anchorNode.inPos = nAttr.create("Position", "pos", OpenMaya.MFnNumericData.k3Float)
    MAKE_INPUT(nAttr)

    try:
        # TODO:: add the attributes to the node and set up the
        #         attributeAffects (addAttribute, and attributeAffects)
        print "Initialization!\n"
        anchorNode.addAttribute(anchorNode.inPos)
        anchorNode.addAttribute(anchorNode.objFile)

        '''randomNode.addAttribute(randomNode.inNumPoints)
        randomNode.addAttribute(randomNode.inMin)
        randomNode.addAttribute(randomNode.inMax)
        randomNode.addAttribute(randomNode.randomPoints)
        randomNode.attributeAffects(randomNode.inNumPoints, randomNode.randomPoints)
        randomNode.attributeAffects(randomNode.inMin, randomNode.randomPoints)
        randomNode.attributeAffects(randomNode.inMax, randomNode.randomPoints)'''

    except:
        sys.stderr.write( ("Failed to create attributes of %s node\n", kPluginNodeTypeName) )

# creator
def nodeCreator():
    return OpenMayaMPx.asMPxPtr( anchorNode() )

# initialize the script plug-in
def initializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.registerNode( kPluginNodeTypeName, anchorNodeId, nodeCreator, nodeInitializer )
    except:
        sys.stderr.write( "Failed to register node: %s\n" % kPluginNodeTypeName )

# uninitialize the script plug-in
def uninitializePlugin(mobject):
    mplugin = OpenMayaMPx.MFnPlugin(mobject)
    try:
        mplugin.deregisterNode( anchorNodeId )
    except:
        sys.stderr.write( "Failed to unregister node: %s\n" % kPluginNodeTypeName )
