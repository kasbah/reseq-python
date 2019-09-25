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
    if receive_interface is None:
        receive_interface = interface
    interface.write(cmd)
    time.sleep(0.1)
    ret = b""
    while receive_interface.in_waiting == 0:
        pass
    while receive_interface.in_waiting > 0:
        ret += receive_interface.readline().rstrip() + b"\n"
    return ret

res = send(fpga_out, b"RESET\n", fpga_in)
print(res)

#res = send(y_motor, b"1D6422185\r")
#print(b"y_motor: " + res)
#res = send(y_motor, b"1G\r")
#print(b"y_motor: " + res)
res = send(y_motor, b"1D\r")
print(res)
y_motor_pos = int(res.split(b"*")[1])
res = send(y_motor, b"1G\r")
print(res)

res = send(fpga_out, b"TDIYERD\n", fpga_in)
print(res)
pos = int(res.split(b' ')[1])

cmd = "TDIYPOS " + str(pos + 10000) + "\n"
print(cmd)
res = send(fpga_out, bytes(cmd, 'utf8'), fpga_in)
print(res)


cmd = "TDIYARM2 " + str(8000) + " 1\n"
print(cmd)
res = send(fpga_out, bytes(cmd, 'utf8'), fpga_in)
print(res)
print("TDIYWAIT")
send(fpga_out, b"TDIYWAIT\n")

res = send(y_motor, bytes("1D" + str(y_motor_pos + 2000000) + "\r", 'utf8'))
print(b"y_motor: " + res)
time.sleep(1)
res = send(y_motor, b"1G\r")
print(b"y_motor: " + res)

time.sleep(10)

#res = send(fpga_out, b"TDIYERD\n", fpga_in)
#print(res)

res = send(y_motor, bytes("1D" + str(y_motor_pos) + "\r", 'utf8'))
print(b"y_motor: " + res)
time.sleep(1)
res = send(y_motor, b"1G\r")
print(b"y_motor: " + res)

time.sleep(10)

#res = send(fpga_out, b"TDIYERD\n", fpga_in)
#print(res)

while fpga_in.in_waiting > 0:
    print(fpga_in.readline().rstrip())
