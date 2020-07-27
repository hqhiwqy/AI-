from utils.utils import my_sum

from utils.class_utils import *
print(my_sum(1, 2))

encoder = Encoder()

decoder = Decoder()

print(encoder.encode('abcde'))

print(decoder.decode('abcde'))