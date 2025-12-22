import os
import allure

from pathlib import Path
from pytest import approx

from tools.logger import get_logger

logger = get_logger("FILE_ASSERTIONS")


@allure.step("Verify file size for {file_name}")
def assert_file_size(file_path: Path, file_name: str, expected_size_mb: float, tolerance=0.01):
    path = file_path.joinpath(file_name)
    actual_size = os.path.getsize(path) / (1024 * 1024)

    logger.info(f'Verifying file size for "{file_name}": expected {expected_size_mb} MB ± {tolerance} MB')

    assert actual_size == approx(expected_size_mb, abs=tolerance), (
        f"File size mismatch for '{file_name}'. "
        f"Expected: {expected_size_mb} MB ± {tolerance} MB, "
        f"Actual: {actual_size} MB"
    )
