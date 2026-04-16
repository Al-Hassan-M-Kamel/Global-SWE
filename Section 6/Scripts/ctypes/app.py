
import ctypes

lib = ctypes.CDLL("./ctypes/math_utils.so")

print(lib.add(2,4))

# => 6