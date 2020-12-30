import unittest

from utils.hex_int_translator import HexIntTranslator


class TestHexIntTranslator(unittest.TestCase):
    def test_to_int1(self):
        translator = HexIntTranslator()
        assert translator.get_int("2b") == 43

    def test_to_int2(self):
        translator = HexIntTranslator()
        assert translator.get_int("ff") == 255

    def test_to_hex1(self):
        translator = HexIntTranslator()
        assert translator.get_hex(44) == "2C"

    def test_to_hex2(self):
        translator = HexIntTranslator()
        assert translator.get_hex(166) == "A6"
