import struct
struct.pack("h", 0x1496)  # h : int16_t
struct.pack("<h", 0x1496) # byte order : "<" Little-endian (Default)
struct.pack(">h", 0x1496) # byte order : ">" Big-endian

struct.pack("3h", 2, 8, 1)  # H : uint16_t
struct.pack(">3h", 2, 8, 1)

struct.pack("I", 0xAB12CD34) # I : uint32_t
res = struct.pack("I", 0xAB12CD34)
res.hex()

struct.pack("f", 3.1415) # f : float32_t
res = struct.pack("f", 3.1415)
res.hex()


