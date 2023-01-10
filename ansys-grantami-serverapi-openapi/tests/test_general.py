import py_compile
from pathlib import Path
import pytest

src_folder = Path(__file__) / "../../src"
files = list(src_folder.rglob("*.py"))

@pytest.mark.parametrize("file", files, ids=[f.relative_to(src_folder).as_posix() for f in files])
def test_all_code_valid(file):
    py_compile.compile(file=file, doraise=True)
