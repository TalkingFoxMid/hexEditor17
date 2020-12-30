from utils.integer_hexer import IntegerHexer


class HexIntTranslator:
    def __init__(self):
        self.integer_hexer = IntegerHexer()

    def get_int(self, hex_value_string):
        return int(hex_value_string, 16)

    def get_hex(self, int_value):
        return self.integer_hexer.get_hex_string(int_value)[-2:]
