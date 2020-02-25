from pyModbusTCP.client import ModbusClient
import sys

input1 = False
input2 = False
input3 = False
input4 = False
input5 = False
input6 = False
input7 = False
input8 = False
input9 = False
input10 = False
input11 = False
input12 = False
input13 = False
input14 = False
input15 = False
input16 = False
DO1 = 0
DO2 = 0
DO3 = 0
DO4 = 0
DO5 = 0
DO6 = 0
DO7 = 0
DO8 = 0
DO9 = 0
DO10 = 0
DO11 = 0
DO12 = 0
DO13 = 0
DO14 = 0
DO15 = 0
DO16 = 0

# Always open port
c = ModbusClient(host='192.168.1.10', port=502, auto_open=True)

i = 1
currentI = 1

try:
    # Write registers
    while True:

        inputs = c.read_holding_registers(1, 2)
        input1 = inputs[0] and 0b0000000100000000
        input2 = inputs[0] and 0b0000001000000000
        input3 = inputs[0] and 0b0000010000000000
        input4 = inputs[0] and 0b0000100000000000
        input5 = inputs[0] and 0b0001000000000000
        input6 = inputs[0] and 0b0010000000000000
        input7 = inputs[0] and 0b0100000000000000
        input8 = inputs[0] and 0b1000000000000000
        input9 = inputs[0] and 0b0000000000000001
        input10 = inputs[0] and 0b0000000000000010
        input11 = inputs[0] and 0b0000000000000100
        input12 = inputs[0] and 0b0000000000001000
        input13 = inputs[0] and 0b0000000000010000
        input14 = inputs[0] and 0b0000000000100000
        input15 = inputs[0] and 0b0000000001000000
        input16 = inputs[0] and 0b0000000010000000
        time = inputs[1]/1000
        if DO1:
            print("Cycle time is " + str(time) + " seconds.")
        if input1 == 256:
            if (currentI != i) and not (DO1 or DO2 or DO3 or DO4 or DO5 or DO6 or DO7 or DO8 or DO9 or DO10 or DO11 or DO12 or DO13 or DO13 or DO13 or DO14 or DO15 or DO16):
                DO1 = 1
            if (currentI != i) and DO1:
                DO1 = 0
                DO2 = 1
                currentI = i
            if (currentI != i) and DO2:
                DO2 = 0
                DO3 = 1
                currentI = i
            if (currentI != i) and DO3:
                DO3 = 0
                DO4 = 1
                currentI = i
            if (currentI != i) and DO4:
                DO4 = 0
                DO5 = 1
                currentI = i
            if (currentI != i) and DO5:
                DO5 = 0
                DO6 = 1
                currentI = i
            if (currentI != i) and DO6:
                DO6 = 0
                DO7 = 1
                currentI = i
            if (currentI != i) and DO7:
                DO7 = 0
                DO8 = 1
                currentI = i
            if (currentI != i) and DO8:
                DO8 = 0
                DO9 = 1
                currentI = i
            if (currentI != i) and DO9:
                DO9 = 0
                DO10 = 1
                currentI = i
            if (currentI != i) and DO10:
                DO10 = 0
                DO11 = 1
                currentI = i
            if (currentI != i) and DO11:
                DO11 = 0
                DO12 = 1
                currentI = i
            if (currentI != i) and DO12:
                DO12 = 0
                DO13 = 1
                currentI = i
            if (currentI != i) and DO13:
                DO13 = 0
                DO14 = 1
                currentI = i
            if (currentI != i) and DO14:
                DO14 = 0
                DO15 = 1
                currentI = i
            if (currentI != i) and DO15:
                DO15 = 0
                DO16 = 1
                currentI = i
            if (currentI != i) and DO16:
                DO16 = 0
                DO1 = 1
                currentI = i
        else:
            DO1 = 0

        value = int("" + str(int(DO8)) + str(int(DO7)) + str(int(DO6)) + str(int(DO5)) + str(int(DO4)) + str(int(DO3))
                    + str(int(DO2)) + str(int(DO1)) + str(int(DO16)) + str(int(DO15)) + str(int(DO14)) + str(int(DO13))
                    + str(int(DO12)) + str(int(DO11)) + str(int(DO10)) + str(int(DO9)), 2)
        outputs = [value]
        c.write_multiple_registers(3, outputs)
        i += 1
except KeyboardInterrupt:
    sys.exit()