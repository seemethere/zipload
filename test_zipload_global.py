"""Test basic global functionality"""
import sys
from zipload import global_load
from utils import zip_to_test


def test_global_load():
    """Test load function"""
    with zip_to_test() as test_zip:
        global_load(test_zip, 'test_data')
        print(sys.path)
        # pylint: disable=import-error
        # pylint: disable=unused-import
        # pylint: disable=import-outside-toplevel
        import example_module
