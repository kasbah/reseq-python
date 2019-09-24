import serial
import time

ports = {
    "fpga_in": "COM15",
    "x_motor": "COM19",
}

fpga_in = serial.Serial(ports["fpga_in"], 115200)
x_motor = serial.Serial(ports["x_motor"], 9600, timeout=1)

fpga_in.name = "fpga_in"
x_motor.name = "x_motor"


def wait_then_write(interface, cmd, receive_interface=None):
    if receive_interface is None:
        receive_interface = interface
    interface.write(cmd)
    while receive_interface.in_waiting == 0:
        pass
    while receive_interface.in_waiting > 0:
        print(receive_interface.name, receive_interface.readline().rstrip())
    print()






wait_then_write(x_motor, b"\x03")






wait_then_write(x_motor, b"L\r")


wait_then_write(x_motor, b"EE=1\r")
wait_then_write(x_motor, b"VI=1\r")


wait_then_write(x_motor, b"PM = 0\r")
wait_then_write(x_motor, b'PR "C1 ", C1\r')
wait_then_write(x_motor, b'PR "C2 ", C2\r')
wait_then_write(x_motor, b"H 50\r")
wait_then_write(x_motor, b"HM 1\r")
wait_then_write(x_motor, b"H\r")
wait_then_write(x_motor, b'PR "Homed at ", P\r')
wait_then_write(x_motor, b"P = 0\r")
wait_then_write(x_motor, b'PR "Homed OK"\r')
wait_then_write(x_motor, b"E\r")
wait_then_write(x_motor, b"PG\r")
wait_then_write(x_motor, b"L\r")
wait_then_write(x_motor, b"EE = 1\r")
wait_then_write(x_motor, b"VI = 1\r")
wait_then_write(x_motor, b"VM = 30720\r")
wait_then_write(x_motor, b"VI = 40\r")
wait_then_write(x_motor, b"A = 40000\r")
wait_then_write(x_motor, b"D = A\r")
wait_then_write(x_motor, b"HC = 20\r")
wait_then_write(x_motor, b"RC = 100\r")
wait_then_write(x_motor, b"MT = 100\r")
wait_then_write(x_motor, b"SM = 0\r")
wait_then_write(x_motor, b"SF = 15\r")
wait_then_write(x_motor, b"DB = 8\r")
wait_then_write(x_motor, b"LM = 1\r")
wait_then_write(x_motor, b"S1 = 1,0,0\r")
wait_then_write(x_motor, b"S2 = 3,1,0\r")
wait_then_write(x_motor, b"S3 = 2,1,0\r")
wait_then_write(x_motor, b"S4 = 0,0,0\r")
wait_then_write(x_motor, b"D1 = 5\r")
wait_then_write(x_motor, b"PR PN\r")
wait_then_write(x_motor, b"PR VR\r")
wait_then_write(x_motor, b"VI=1\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"VM=6144\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"VI=410\r")
wait_then_write(x_motor, b"A=16384\r")
wait_then_write(x_motor, b"D=A\r")
wait_then_write(x_motor, b"SF=8192\r")
#wait_then_write(x_motor, b"P=0\r")
wait_then_write(x_motor, b"DE=1\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"MA 0\r")
wait_then_write(x_motor, b"PR ER\r")
# SerialPort B1 (VICIB1)	VR\r
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"VI=1\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"VM=4096\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"VI=410\r")
# KloehnSerialPort A (KLOEHNA)	/1&\r
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"MR -409190\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR MV\r")
wait_then_write(x_motor, b"PR ER\r")
wait_then_write(x_motor, b"VI=1\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"VM=6144\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"VI=410\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"DE=1\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"EX 1\r")
wait_then_write(x_motor, b"PM=0\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
wait_then_write(x_motor, b"MA -4915\r")
wait_then_write(x_motor, b"PR ER\r")
wait_then_write(x_motor, b"PR VM\r")
wait_then_write(x_motor, b"PR VI\r")
