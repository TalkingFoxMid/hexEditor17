import unittest

from utils.hex_byte_verificator import HexByteVerificator


class TestHexByteVerificator(unittest.TestCase):
    def test_hex_byte_verificate_number(self):
        verificator = HexByteVerificator()
        assert verificator.verify_hex_byte("56")

    def test_hex_byte_verificate_hex(self):
        verificator = HexByteVerificator()
        assert verificator.verify_hex_byte("a0")

    def test_hex_byte_verificate_caps(self):
        verificator = HexByteVerificator()
        assert verificator.verify_hex_byte("AB")

    def test_hex_byte_verificate_single(self):
        verificator = HexByteVerificator()
        assert verificator.verify_hex_byte("5")

    def test_hex_byte_verificate_single_hex(self):
        verificator = HexByteVerificator()
        assert verificator.verify_hex_byte("b")

    def test_hex_byte_verificate_three(self):
        verificator = HexByteVerificator()
        assert not verificator.verify_hex_byte("432")

    def test_hex_byte_verificate_unknow(self):
        verificator = HexByteVerificator()
        assert not verificator.verify_hex_byte("4h")
