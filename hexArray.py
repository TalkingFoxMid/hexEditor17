class HexArray:
    def __init__(self, array: list):
        self.byte_array = array
        self.start_array = array.copy()
    def get_byte_array(self):
        return self.byte_array
    def get_byte_start_array(self):
        return self.start_array
