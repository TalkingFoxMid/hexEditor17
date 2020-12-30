import unittest

from utils.integer_hexer import IntegerHexer


class TestIntegerHexer(unittest.TestCase):
    def test_to_hex1(self):
        hexer = IntegerHexer()
        assert hexer.get_hex_string(10) == "0000000A"

    def test_to_hex2(self):
        hexer = IntegerHexer()
        assert hexer.get_hex_string(140425) == "00022489"
