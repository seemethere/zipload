"""A simply python module to load zip archives into your python path

How this actually works:
    1. Unzip archive into a temporary directory
    2. Add that temporary directory to your Python Path
    3. Cleanup python path and temporary directory at
       exit (function / global level)
"""

import atexit
import contextlib
import os
import sys
import tempfile
import zipfile


@contextlib.contextmanager
def load(zip_path, path_to_add=""):
    """Load a zip file into your python path at a smaller scale

    Example:

        .. sourcecode:: python
            import zipload

            with zipload.load("example.zip", "lib/python3.8/site-packages"):
                import numpy
    """
    with tempfile.TemporaryDirectory(prefix="zipload-py") as tmp_dir:
        _extract_zip(zip_path, tmp_dir, path_to_add)
        sys.path.append(os.path.join(tmp_dir, path_to_add))
        yield None
        sys.path.remove(os.path.join(tmp_dir, path_to_add))


def global_load(zip_path, path_to_add=""):
    """Load a zip file into your python path at a global level

    Example:

        .. sourcecode:: python
            import zipload
            # Must go above libraries you would want to load
            zipload.global_load("example.zip", "lib/python3.8/site-packages")

            import numpy
    """
    tmp_dir = tempfile.TemporaryDirectory(prefix="zipload-py")
    atexit.register(tmp_dir.cleanup)
    _extract_zip(zip_path, tmp_dir.name, path_to_add)
    sys.path.append(os.path.join(tmp_dir.name, path_to_add))
    atexit.register(os.path.join, tmp_dir.name, path_to_add)


def _extract_zip(zip_path, tmp_dir, path_to_add=None):
    with zipfile.ZipFile(zip_path, "r") as my_zip:
        if path_to_add != "":
            for filename in my_zip.namelist():
                if filename.startswith(path_to_add):
                    my_zip.extract(filename, tmp_dir)
        else:
            my_zip.extractall(tmp_dir.name)
