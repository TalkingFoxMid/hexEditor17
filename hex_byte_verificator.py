class HexByteVerificator:
    def __init__(self):
        self.alphabet_set = {'0', '1', '2', '3', '4',
                        '5', '6', '7', '8', '9',
                        'A', 'B', 'C', 'D', 'E', 'F'}
    def verify_hex_byte(self, hex_byte_string: str):
        hex_byte_string = hex_byte_string.upper()
        if len(hex_byte_string) == 0:
            return False
        if len(hex_byte_string) > 2:
            return False
        if not set(hex_byte_string).issubset(self.alphabet_set):
            return False
        return True

