import shutil
import tempfile
from collections.abc import Generator
from pathlib import Path

import pytest
from rpgmvp_converter.constants import PNG_HEADER
from rpgmvp_converter.converter import RpgMvpConverter


@pytest.fixture()
def converter() -> RpgMvpConverter:
    return RpgMvpConverter()


@pytest.fixture()
def output_dir() -> Generator[Path, None, None]:
    d = tempfile.mkdtemp()
    yield Path(d)
    shutil.rmtree(d)


@pytest.fixture()
def examples_dir() -> Path:
    # Locate the 'examples' directory relative to this test file
    project_root = Path(__file__).parent.parent
    path = project_root / "examples"
    assert path.exists(), "Examples directory must exist"
    return path


def test_convert_single_file(
    converter: RpgMvpConverter, examples_dir: Path, output_dir: Path
) -> None:
    input_file = examples_dir / "Cure1.rpgmvp"
    assert input_file.exists(), "Input RPGMVP file must exist"

    output_file = output_dir / "Cure1.png"

    success = converter.convert_file(input_file, output_file)

    assert success, "File conversion should return True"
    assert output_file.exists(), "Output PNG file should exist"

    # Verify file header
    with output_file.open("rb") as f:
        header = f.read(len(PNG_HEADER))
        assert header == PNG_HEADER, "Output file must have valid PNG header"


def test_convert_directory(
    converter: RpgMvpConverter, examples_dir: Path, output_dir: Path
) -> None:
    target_output_dir = output_dir / "converted_examples"

    converter.convert_directory(examples_dir, target_output_dir)
    assert target_output_dir.exists()

    # Verify a few expected files exist
    expected_files = ["Cure1.png", "Slash.png", "Thunder1.png"]
    for filename in expected_files:
        file_path = target_output_dir / filename
        assert file_path.exists(), f"{filename} should exist in output directory"

        with file_path.open("rb") as f:
            header = f.read(len(PNG_HEADER))
            assert header == PNG_HEADER, f"{filename} has invalid PNG header"
