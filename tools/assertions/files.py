import os
from pathlib import Path
from pytest import approx


def assert_file_size(file_path: Path, file_name: str, expected_size_mb: float, tolerance=0.01):
    path = file_path.joinpath(file_name)
    actual_size = os.path.getsize(path) / (1024 * 1024)

    assert actual_size == approx(expected_size_mb, abs=tolerance), (
        f"File size mismatch for '{file_name}'. "
        f"Expected: {expected_size_mb} MB ± {tolerance} MB, "
        f"Actual: {actual_size} MB"
    )
