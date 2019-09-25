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

fpga_out = serial.Serial(ports["fpga_out"], 115200)
fpga_in = serial.Serial(ports["fpga_in"], 115200)
y_motor = serial.Serial(ports["y_motor"], 9600)

fpga_out.name = "fpga_out"
fpga_in.name = "fpga_in"
y_motor.name = "y_motor"

def send(interface, cmd, receive_interface=None):
    print(interface.name, cmd.encode('utf8'))
    if receive_interface is None:
        receive_interface = interface
    interface.write(cmd.encode('utf8'))
    time.sleep(0.1)
    ret = b""
    while receive_interface.in_waiting == 0:
        pass
    while receive_interface.in_waiting > 0:
        ret += receive_interface.readline().rstrip() + b"\n"
    return ret.decode('utf8')

#res = send(fpga_out, "RESET\n", fpga_in)
#print(res)
#
#res = send(fpga_out, "LSEN\nSWLSRSHUT 1\nZDACW 32000\nT1HM\nT2HM\nT3HM\n", fpga_in)
#print(res)
#
#res = send(y_motor, "1V0\r15\r")
#print(res)
#
#res = send(fpga_out, "SWLSRSHUT 0\n", fpga_in)
#print(res)
#
#res = send(fpga_out, "TDIYPOS 2144260\n", fpga_in)
#print(res)
#
#res = send(y_motor, "1D-4015740\r1G\r")
#print(res)
#time.sleep(1)
#
#res = send(fpga_out, "TDIYPOS 2238750\n", fpga_in)
#print(res)
#
#res = send(y_motor, "1D-3921250\r1G\r")
#print(res)
#time.sleep(1)
#
#res = send(fpga_out, "TDIYPOS 2333230\n", fpga_in)
#print(res)
#
#res = send(y_motor, "1D-3826770\r1G\r")
#print(res)
#time.sleep(1)
#
#res = send(fpga_out, "TDIYPOS 2427720\n", fpga_in)
#print(res)

res = send(y_motor, "1D-4511650\r1G\r")
print(res)

time.sleep(10)

res = send(fpga_out, "TDIYPOS 1388350\n", fpga_in)
print(res)


res = send(fpga_out, "TDIYARM2 8000 1\n", fpga_in)
print(res)

send(fpga_out, "TDIYWAIT\n")

time.sleep(1)


res = send(y_motor, "1D-4931650\r1G\r")
print(res)

#time.sleep(5)
#
#res = send(y_motor, "1D-4039210\r1G\r")
#print(res)
