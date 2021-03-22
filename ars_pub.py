from sys import path as sysPath
import rticonnextdds_connector as rti
from os import path as osPath
from time import sleep
import random
filepath = osPath.dirname(osPath.realpath(__file__))

connector = rti.Connector("MyParticipantLibrary::Ars_pub", filepath + "/DDS.xml")
outputDDS = connector.getOutput("MyPublisher::MyWriter")

while True:
    randomTemp = random.randint(0, 10)
    outputDDS.instance.setNumber("Temp", randomTemp)
    outputDDS.write()
    sleep(0.1)
    print(f'published: {randomTemp}')
