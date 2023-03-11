import time

import serial
import numpy as np
import math
import os


rawPoints = np.zeros([3, 6])

# 1:1 values from USB
intake = np.zeros([3, 6])

radious = 65


separate = np.zeros(3)

ser = serial.Serial("COM4", 115200, timeout=100)
while(1):
    index = -1
    data = ser.readlines(250)
    for i in range(12):

        decoded = data[i].decode('utf8')

        if ";" in decoded:
            index += 1
            separate = decoded.split(";")

            # print(separate)
            # print(separate)
            try:
                separate[0] = str(separate[0]).replace('.', '')
                separate[1] = str(separate[1]).replace('.', '')
                separate[2] = str(separate[2]).replace('.', '')
            except ValueError:
                print("Something tried to insert a wrong value into separate")
            except IndexError:
                print("index out of range")


            #else:
            # print(separate[0])
            # print(separate[1])
            # print(separate[2])
            try:
                intake[0, index] = int(separate[0])  # / int(Calibration.get())
                rawPoints[0, index] = intake[0, index] * (3.2 / 18)
                intake[1, index] = int(separate[1])  # / int(Calibration.get())
                rawPoints[1, index] = radious * math.cos(math.radians(intake[1, index] * (360 / 4096)))
                intake[2, index] = int(separate[2])  # / int(Calibration.get())
                # TU BYŁO ZMIENIONE
                rawPoints[2, index] = (intake[2, index] * (3.2 / 18 )) + radious * math.sin(math.radians(intake[1, index] * (360 / 4096)))
            except ValueError:
                print("intake value error")
        if "BEGIN" in decoded:
            index = -1

        # check this
    ser.flushInput()
    # ser.close()
    # print(rawPoints)
    # zeroing = rawPoints


    os.system('cls')
    print(rawPoints.round())
    time.sleep(0.01)