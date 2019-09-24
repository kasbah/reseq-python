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
#fpga_in = serial.Serial(ports["fpga_in"], 115200)
#laser2 = serial.Serial(ports["laser2"], 9600)  # red laser
#laser1 = serial.Serial(ports["laser1"], 9600)  # green laser
#x_motor = serial.Serial(ports["x_motor"], 9600)
y_motor = serial.Serial(ports["y_motor"], 9600)

#fpga_out.name = "fpga_out"
#fpga_in.name = "fpga_in"
#laser2.name = "laser2"
#laser1.name = "laser1"
#x_motor.name = "x_motor"
y_motor.name = "y_motor"


def wait_then_write(interface, cmd, receive_interface=None):
    if receive_interface is None:
        receive_interface = interface
    #input(interface.name + ' ' + str(cmd))
    interface.write(cmd)
    time.sleep(0.1)
    while receive_interface.in_waiting == 0:
        pass
    while receive_interface.in_waiting > 0:
        print(receive_interface.name, receive_interface.readline().rstrip())
    print()


y_motor.write(b'\r')
wait_then_write(y_motor, b"1END\r")
wait_then_write(y_motor, b"1K\r")
wait_then_write(y_motor, b"1W(EQ,0)\r")
wait_then_write(y_motor, b"1W(EX,2)\r")
wait_then_write(y_motor, b"1W(EQ,0)\r")
wait_then_write(y_motor, b"1R(EQ)\r")
wait_then_write(y_motor, b"1W(EX,2)\r")
wait_then_write(y_motor, b"1R(EX)\r")
wait_then_write(y_motor, b"1R(UF)\r")
wait_then_write(y_motor, b"1R(DF)\r")
wait_then_write(y_motor, b"1R(UF)\r")
wait_then_write(y_motor, b"1R(ST)\r")
wait_then_write(y_motor, b"1LIST(ALL)\r")
wait_then_write(y_motor, b"PR VI\r")
wait_then_write(y_motor, b"1GOSUB(INIT)\r")
wait_then_write(y_motor, b"1R(DF)\r")
wait_then_write(y_motor, b"1R(UF)\r")
wait_then_write(y_motor, b"1R(ST)\r")
wait_then_write(y_motor, b"1MOTOR\r")
wait_then_write(y_motor, b"1R(SN)\r")
wait_then_write(y_motor, b"1R(RV)\r")
wait_then_write(y_motor, b"1R(DF)\r")
wait_then_write(y_motor, b"1R(UF)\r")
wait_then_write(y_motor, b"1W(EO,2)\r")
wait_then_write(y_motor, b"1R(EO)\r")
wait_then_write(y_motor, b"1W(CQ,0)\r")
wait_then_write(y_motor, b"1R(CQ)\r")
wait_then_write(y_motor, b"1W(SC,1)\r")
wait_then_write(y_motor, b"1R(SC)\r")
wait_then_write(y_motor, b"1MA\r")
wait_then_write(y_motor, b"1M\r")
wait_then_write(y_motor, b"1V1.92200\r")
wait_then_write(y_motor, b"1AA1.92250\r")
wait_then_write(y_motor, b"1AD1.92250\r")
wait_then_write(y_motor, b"1W(EW,200)\r")
wait_then_write(y_motor, b"1R(EW)\r")
wait_then_write(y_motor, b"1W(GP,7)\r")
wait_then_write(y_motor, b"1R(GP)\r")
wait_then_write(y_motor, b"1W(GI,10)\r")
wait_then_write(y_motor, b"1R(GI)\r")
wait_then_write(y_motor, b"1W(GV,1.5)\r")
wait_then_write(y_motor, b"1R(GV)\r")
wait_then_write(y_motor, b"1W(GF,5)\r")
wait_then_write(y_motor, b"1R(GF)\r")
wait_then_write(y_motor, b"1ON\r")
wait_then_write(y_motor, b"1W(PA,0)\r")
wait_then_write(y_motor, b"1ON\r")
wait_then_write(y_motor, b"1D-2\r")
wait_then_write(y_motor, b"1G\r")
wait_then_write(y_motor, b"1D\r")
wait_then_write(y_motor, b"1IS\r")
wait_then_write(y_motor, b"1R(DF)\r")
wait_then_write(y_motor, b"1R(UF)\r")
wait_then_write(y_motor, b"1R(ST)\r")
wait_then_write(y_motor, b"1R(GP)\r")
wait_then_write(y_motor, b"1R(GI)\r")
wait_then_write(y_motor, b"1R(GV)\r")
wait_then_write(y_motor, b"1R(GF)\r")
wait_then_write(y_motor, b"1ON\r")
wait_then_write(y_motor, b"1GH\r")
wait_then_write(y_motor, b"1D-6700000\r")
wait_then_write(y_motor, b"1G\r")
wait_then_write(y_motor, b"1D\r")
