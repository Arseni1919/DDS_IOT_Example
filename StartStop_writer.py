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
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti

connector = rti.Connector("MyParticipantLibrary::StartStop",
                          filepath + "/DDS.xml")
StartStopDDS = connector.getOutput("MyPublisher::MyStartStopWriter")

while(True):
    StartStopDDS.instance.setNumber("Start", 1)
    StartStopDDS.write()
    sleep(20)
    StartStopDDS.instance.setNumber("Start",0)
    StartStopDDS.write()
    sleep(5)


