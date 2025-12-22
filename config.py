import json

from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class BrowserConfig(BaseModel):
    chromium_options: list[str]
    page_load_strategy: str
    page_load_timeout: int
    wait_timeout: float
    wait_poll_frequency: float


class TestData(BaseModel):
    initial_region: str
    new_region: str
    expected_url_part: str
    expected_region_title_part: str
    saby_desktop_for_windows_app_file_name: str
    saby_desktop_for_windows_app_size: float


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="allow",
        env_file=".env.example",
        env_file_encoding="utf-8",
        env_nested_delimiter=".",
    )

    browser_config: BrowserConfig
    test_data: TestData


with open("./tests/data/test_data.json", encoding="utf-8") as f:
    test_data_dict = json.load(f)

settings = Settings(test_data=test_data_dict)
