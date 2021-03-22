###############################################################################
# (c) 2005-2015 Copyright, Real-Time Innovations.  All rights reserved.       #
# No duplications, whole or partial, manual or electronic, may be made        #
# without express written permission.  Any such copies, or revisions thereof, #
# must display this notice unaltered.                                         #
# This code contains trade secrets of Real-Time Innovations, Inc.             #
###############################################################################

"""Samples's reader."""

from __future__ import print_function
from sys import path as sysPath
from os import path as osPath
from time import sleep
filepath = osPath.dirname(osPath.realpath(__file__))
sysPath.append(filepath + "/../../../")
import rticonnextdds_connector as rti



connector = rti.Connector("MyParticipantLibrary::DashBoard",#loading the same app as the writer
                          filepath + "/DDS.xml")
temperatures_DDS = connector.getInput("MySubscriber::MyTempReader")
#StartStopDDS = connector.getInput("MySubscriber::MyStartStopReader")
actuators_DDS = connector.getInput("MySubscriber::MyActuatorReader")


while True:
    temperatures_DDS.take()
    numOfSamples = temperatures_DDS.samples.getLength()
    for j in range(0, numOfSamples):
        if temperatures_DDS.infos.isValid(j):
            temp = temperatures_DDS.samples.getNumber(j, "Temp")
            toPrint = "Received Temp: " + repr(temp)
            print(toPrint)
#for checking the start and stop buttom
    #StartStopDDS.take()
    #numOfSamples1 = StartStopDDS.samples.getLength()
    #for j in range(0, numOfSamples1):
     #   if StartStopDDS.infos.isValid(j):
      #      start = StartStopDDS.samples.getNumber(j,"Start")
       #     toPrint1 = "Received StartStop: " + repr(start)
        #    print(toPrint1)

    actuators_DDS.take()
    numOfSamples2 = actuators_DDS.samples.getLength()
    for j in range(0, numOfSamples2):
        if actuators_DDS.infos.isValid(j):
            status = actuators_DDS.samples.getString(j, "Status")
            number = actuators_DDS.samples.getNumber(j, "SerialNumber")
            toPrint2 = "Actuator ID: " + repr(number) + " Status: " + repr(status)
            print(toPrint2)
sleep(1)
