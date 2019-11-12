"""Test basic functionality"""
import sys

# These are relative imports
from zipload import load
from utils import zip_to_test


def test_load():
    """Test load function"""
    with zip_to_test() as test_zip:
        with load(test_zip, 'test_data'):
            print(sys.path)
            # pylint: disable=import-error
            # pylint: disable=unused-import
            # pylint: disable=import-outside-toplevel
            import example_module
