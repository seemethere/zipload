"""Utils to be used explicitly for testing"""
import contextlib
import os
import tempfile
import zipfile


@contextlib.contextmanager
def zip_to_test(prepend_path=""):
    """Creates a zip file for testing, destroys upon exit"""
    module_path = 'test_data/example_module'
    with tempfile.TemporaryDirectory(prefix='zipload-py-test') as tmp_dir:
        zip_path = os.path.join(tmp_dir, 'test.zip')
        with zipfile.ZipFile(zip_path, 'w') as created_zip:
            for root, _, files in os.walk(module_path):
                for file in files:
                    created_zip.write(os.path.join(root, prepend_path, file))
        yield zip_path
