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

res = send(y_motor, "1G\r")
print(res)

time.sleep(2)

res = send(y_motor, "1D\r")
print(res)
y_motor_pos = int(res.split('*')[1])

res = send(fpga_out, "TDIYERD\n", fpga_in)
print(res)
encoder_pos = int(res.split(' ')[1])

res = send(fpga_out, "TDIYPOS {}\n".format(encoder_pos - 100000), fpga_in)
print(res)


res = send(fpga_out, "TDIYARM2 8000 1\n", fpga_in)
print(res)

send(fpga_out, "TDIYWAIT\n")

time.sleep(1)


res = send(y_motor, "1D{}\r1G\r".format(y_motor_pos - 420000))
print(res)
time.sleep(10)

res = send(fpga_out, "TDIYERD\n", fpga_in)
print(res)

res = send(y_motor, "1D{}\r1G\r".format(y_motor_pos))
print(res)

res = send(fpga_out, "TDIYERD\n", fpga_in)
print(res)
