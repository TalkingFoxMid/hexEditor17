import unittest
import random
from HexDataManager.hex_data_manager import HexDataManager


class TestHexDataManager(unittest.TestCase):
    def test_get_page_first(self):
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        assert (hex_data_manager.get_page(0) ==
                [77, 97, 114, 120, 105, 115,
                 109, 32, 105, 115, 32, 97, 32,
                 109, 101, 116, 104, 111, 100, 32,
                 111, 102, 32, 115, 111, 99, 105, 111,
                 101, 99, 111, 110, 111, 109, 105, 99, 32,
                 97, 110, 97, 108, 121, 115, 105, 115, 32, 116,
                 104, 97, 116, 32, 117, 115, 101, 115, 32, 97, 32,
                 109, 97, 116, 101, 114, 105, 97, 108, 105, 115, 116,
                 32, 105, 110, 116, 101, 114, 112, 114, 101, 116, 97, 116,
                 105, 111, 110, 32, 111, 102, 32, 104, 105, 115, 116, 111,
                 114, 105, 99, 97, 108, 32, 100, 101, 118, 101, 108, 111,
                 112, 109, 101, 110, 116, 44, 32, 98, 101, 116, 116, 101,
                 114, 32, 107, 110, 111, 119, 110, 32, 97, 115, 32, 104,
                 105, 115, 116, 111, 114, 105, 99, 97, 108, 32, 109, 97,
                 116, 101, 114, 105, 97, 108, 105, 115, 109, 44, 32, 116,
                 111, 32, 117, 110, 100, 101, 114]
                )

    def test_get_page_second(self):
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        assert (hex_data_manager.get_page(1) ==
                [115, 116, 97, 110, 100,
                 32, 99, 108, 97, 115, 115,
                 32, 114, 101, 108, 97, 116,
                 105, 111, 110, 115, 32, 97,
                 110, 100, 32, 115, 111, 99,
                 105, 97, 108, 32, 99, 111, 110,
                 102, 108, 105, 99, 116, 32, 97,
                 115, 32, 119, 101, 108, 108, 32,
                 97, 115, 32, 97, 32, 100, 105, 97,
                 108, 101, 99, 116, 105, 99, 97, 108,
                 32, 112, 101, 114, 115, 112, 101, 99,
                 116, 105, 118, 101, 32, 116, 111, 32,
                 118, 105, 101, 119, 32, 115, 111, 99,
                 105, 97, 108, 32, 116, 114, 97, 110,
                 115, 102, 111, 114, 109, 97, 116, 105,
                 111, 110, 46, 32, 73, 116, 32, 111, 114,
                 105, 103, 105, 110, 97, 116, 101, 115, 32,
                 102, 114, 111, 109, 32, 116, 104, 101, 32,
                 119, 111, 114, 107, 115, 32, 111, 102, 32,
                 49, 57, 116, 104, 45, 99, 101, 110, 116,
                 117, 114, 121, 32, 71, 101, 114, 109, 97])

    def test_page_count(self):
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        assert hex_data_manager.pages_count == 10

    def test_page_over_maximum(self):
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        assert hex_data_manager.get_page(116) == []

    def test_change_value(self):
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        assert hex_data_manager.get_page(4)[4] == 99
        hex_data_manager.set_value(4, 4, 10)
        assert hex_data_manager.get_page(4)[4] == 10

    def test_save_to_file(self):
        rng = random.randint(1, 255)
        hex_data_manager = HexDataManager("./HexDataManager/test_data")
        hex_data_manager.get_page(0)[0] = rng
        hex_data_manager.write_changes_in_file("./HexDataManager/test_file")
        hex_data_manager = HexDataManager("./HexDataManager/test_file")
        assert hex_data_manager.get_page(0)[0] == rng
        assert hex_data_manager.get_page(2)[0] == 110

    def test_save_to_new_file(self):
        rng = random.randint(1, 255)
        hex_data_manager = HexDataManager("")
        hex_data_manager.append_empty_bytes_for_page(0, 10)
        hex_data_manager.get_page(0)[0] = rng
        hex_data_manager.write_changes_in_new_file(
            "./HexDataManager/test_file")
        hex_data_manager = HexDataManager("./HexDataManager/test_file")
        assert hex_data_manager.get_page(0)[0] == rng
