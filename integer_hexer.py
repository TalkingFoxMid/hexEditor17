class Integer_Hexer:
    def get_hex_string(self, number):
        result = hex(number)
        result = result[2:].upper()
        result = '0'*(8-len(result))+result
        return result
