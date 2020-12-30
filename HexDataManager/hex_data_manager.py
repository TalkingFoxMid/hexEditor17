import os


class HexDataManager:
    def __init__(self, file_name):
        self.pages = {}
        self.file_name = file_name
        self.bytes_per_page = 16 * 10
        if (file_name == ""):
            self.file_size = 0
            self.pages_count = 1
            return
        self.file_size = os.stat(file_name).st_size
        self.pages_count = int(self.file_size / self.bytes_per_page) + 1

    def init_page_from_file(self, page_number):
        if self.file_name == "":
            self.pages[page_number] = []
            return
        with open(self.file_name, "rb") as f:
            f.seek(page_number * self.bytes_per_page)
            page_content = f.read(self.bytes_per_page)
        self.pages[page_number] = [i for i in page_content]

    def get_page(self, page_number):
        if page_number not in self.pages:
            self.init_page_from_file(page_number)
        return self.pages[page_number]

    def set_value(self, page_number, position_on_page, value):
        if page_number not in self.pages:
            self.init_page_from_file(page_number)
        self.pages[page_number][position_on_page] = value

    def append_empty_bytes_for_page(self, page_number, count):
        if page_number not in self.pages:
            self.pages[page_number] = [0] * count
        else:
            self.pages[page_number] += [0] * count

    def get_byte_from_int(self, int_value):
        return int_value.to_bytes(1, "little")

    def write_changes_in_new_file(self, new_file_name):
        with open(new_file_name, "wb") as fw:
            for i in range(self.pages_count):
                page = self.pages[i]
                fw.seek(160 * i)
                fw.write(
                    b"".join([self.get_byte_from_int(i) for i in page]))

    def write_changes_in_file(self, new_file_name):
        if self.file_name == "":
            self.write_changes_in_new_file(new_file_name)
            return
        with open(self.file_name, "rb") as fr:
            with open(new_file_name, "wb") as fw:
                for i in range(self.pages_count):
                    if i in self.pages:
                        page = self.pages[i]
                        fw.seek(160 * i)
                        fw.write(b"".join(
                            [self.get_byte_from_int(i) for i in page]))
                    else:
                        fr.seek(160 * i)
                        fw.write(fr.read(160))
