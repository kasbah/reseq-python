import serial
import time

ports = {
    "fpga_out": "COM16",
    "fpga_in": "COM15",
    "laser2": "COM14",
    "laser1": "COM12",
    "x_motor": "COM19",
    "y_motor": "COM18",
}

#fpga_out = serial.Serial(ports["fpga_out"], 115200)
fpga_in = serial.Serial(ports["fpga_in"], 115200)
#laser2 = serial.Serial(ports["laser2"], 9600)  # red laser
#laser1 = serial.Serial(ports["laser1"], 9600)  # green laser
#x_motor = serial.Serial(ports["x_motor"], 9600)
#y_motor = serial.Serial(ports["y_motor"], 9600)

#fpga_out.name = "fpga_out"
fpga_in.name = "fpga_in"
#laser2.name = "laser2"
#laser1.name = "laser1"
#x_motor.name = "x_motor"
#y_motor.name = "y_motor"


while 1:
    print(fpga_in.readline().rstrip())