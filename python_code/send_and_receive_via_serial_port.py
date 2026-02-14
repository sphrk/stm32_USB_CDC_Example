# import serial

# PORT = 'COM4'
# BAUD = 115200
# TIMEOUT = 2 # second
# ser = serial.Serial(port=PORT, baudrate=BAUD, timeout=TIMEOUT)

# ser.close() # close COM port

# ser.open()  # open COM port
# ser.reset_input_buffer()    # clear input buffer

# if ser.is_open:
#     print('Serial is Open.')

# ## send "Hello"
# ser.write(b"Hello")

# ## send 0x55, 0xAB, 0x08
# ser.write(b"\x55\xAB\x08")

# ## send 0x55, 0xAB, 0x08
# ser.write([0x55, 0xab, 8])

# ser.close()     # close COM port


## *****************************************
## *****************************************
# import serial

# PORT = 'COM4'
# BAUD = 115200
# TIMEOUT = 2 # second
# ser = serial.Serial(port=PORT, baudrate=BAUD, timeout=TIMEOUT)
# # ser.close() # close COM port
# # ser.open()  # open COM port
# ser.reset_input_buffer()    # clear input buffer

# ## send 0x55
# ser.write([0x55])

# x = ser.read(12)  # read 12 bytes

# print(x)
# print(type(x))
# print(x.decode())
# print(type(x.decode()))

# ser.close()     # close COM port

## *****************************************
## *****************************************
# import serial

# PORT = 'COM4'
# BAUD = 115200
# TIMEOUT = 2 # second
# ser = serial.Serial(port=PORT, baudrate=BAUD, timeout=TIMEOUT)
# # ser.close() # close COM port
# # ser.open()  # open COM port
# ser.reset_input_buffer()    # clear input buffer

# # ## send 0x55
# # ser.write([0x55])
# # x = ser.read(12)  # read 12 bytes

# # print(x)
# # print(type(x))
# # print(x.decode())
# # print(type(x.decode()))

# ## send 0x01, 21, 55
# ser.write([0x01, 21, 55])
# x = ser.read()

# print(x)
# print(type(x))
# print(x[0])
# print(type(x[0]))


# ser.close()     # close COM port

## *****************************************
## *****************************************
import serial

PORT = 'COM4'
BAUD = 115200
TIMEOUT = 2 # second
ser = serial.Serial(port=PORT, baudrate=BAUD, timeout=TIMEOUT)
# ser.close() # close COM port
# ser.open()  # open COM port
ser.reset_input_buffer()    # clear input buffer

# ------------------------------------------------------------
## send 0x01, 21, 55, 0xAA, 0xFA
ser.write([0x01, 21, 55, 0xAA, 0xFA])
x = ser.read(2)

print(x)
print(type(x))
print(x[0])
print('x[1] = ', x[1])
print('hex(x[1]) = ', hex(x[1]))

# ------------------------------------------------------------
## send 0x01, 21, 55
ser.write([0x01, 21, 55])
## send 0xAA, 0xFA
ser.write([0xAA, 0xFA])
x = ser.read(2)

print(x)
print(type(x))
print(x[0])
print('x[1] = ', x[1])
print('hex(x[1]) = ', hex(x[1]))
# ------------------------------------------------------------
## send 0x01, 21, 55
ser.write([0x01, 21, 55])
x = ser.read()
print(x)

## send 0xAA, 0xFA
ser.write([0xAA, 0xFA])
x = ser.read()
print(x)



ser.close()     # close COM port



