# 存储常用类


class Encoder(object):
    def encode(self, str):
        return str[::-1]

class Decoder(object):
    def decode(self, str):
        return ''.join(reversed(list(str)))

