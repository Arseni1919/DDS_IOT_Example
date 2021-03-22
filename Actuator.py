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
import time


connector = rti.Connector("MyParticipantLibrary::Actuator",#loading the same app as the writer
                          filepath + "/DDS.xml")
tempDDS = connector.getInput("MySubscriber::MyTempReader")#thake the "socket" that give me the information
StartStopDDS = connector.getInput("MySubscriber::MyStartStopReader")
statusDDS = connector.getOutput("MyPublisher::MyStatusWriter")

initTime=time.time()
status = "Working"
start =1
temp=1
statusDDS.instance.setString("Status", status)
statusDDS.instance.setNumber("SerialNumber", initTime)
statusDDS.write()

while (True):
    StartStopDDS.take()
    numOfSamples1 = StartStopDDS.samples.getLength()
    for j in range(0, numOfSamples1):
        if StartStopDDS.infos.isValid(j):
            start = StartStopDDS.samples.getNumber(j,"Start")
    tempDDS.take()
    numOfSamples = tempDDS.samples.getLength()
    for j in range(0, numOfSamples):
        if tempDDS.infos.isValid(j):
            temp = tempDDS.samples.getNumber(j,"Temp")
    if status == "Working":
        if start == 0:
            status = "Stopped"
            statusDDS.instance.setString("Status", status)
            statusDDS.write()
        elif temp < 20 or temp > 40:
            status = "Degraded"
            statusDDS.instance.setString("Status", status)
            statusDDS.write()
    elif status == "Degraded":
        if start == 0:
            status = "Stopped"
            statusDDS.instance.setString("Status", status)
            statusDDS.write()
        elif 20 < temp and temp < 40:
            status =  "Working"
            statusDDS.instance.setString("Status",status)
            statusDDS.write()
    elif status == "Stopped":
        if start == 1:
            status =  "Working"
            statusDDS.instance.setString("Status",status)
            statusDDS.write()
sleep(1)