
from cffi import FFI

ffi = FFI()

ffi.cdef("int add(int a, int b);")

lib = ffi.dlopen("./math_utils.so")

print(lib.add(3, 4))  # → 7