###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

"""Samples's writer."""

from sys import path as sysPath
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti

connector = rti.Connector("MyParticipantLibrary::Temperature",
                          filepath + "/DDS.xml")
outputDDS = connector.getOutput("MyPublisher::MyTempWriter")

while(True):
    randomTemp = random.randint(10,61)
    outputDDS.instance.setNumber("Temp", randomTemp)
    outputDDS.write()
    sleep(0.1)


