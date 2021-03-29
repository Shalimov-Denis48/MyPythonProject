from my_funcs.file_workers import read_from_file


def test_read_from_file():
    test_data = ['one', 'two', 'three']
    assert test_data == read_from_file("testfile.txt")
