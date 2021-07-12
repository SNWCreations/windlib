from .windlib import (
    typeof,
    extract,
    get_file,
    find_files_with_the_specified_extension,
    copy_file,
    is_it_broken,
    pushd,
    compress,
    get_sha1,
    get_md5
)

__all__ = [
    "typeof",
    "extract",
    "get_file",
    "find_files_with_the_specified_extension",
    "copy_file",
    "is_it_broken",
    "pushd",
    "compress",
    "get_sha1",
    "get_md5"
]

try:
    # Python 3.8+
    import importlib.metadata as importlib_metadata
except ImportError:
    # <Python 3.7 and lower
    import importlib_metadata

__version__ = importlib_metadata.version(__name__)
