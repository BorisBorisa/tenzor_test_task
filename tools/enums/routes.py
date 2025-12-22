from enum import Enum


class Routes(str, Enum):
    ABOUT = "about"
    CONTACT = "contacts"
    DOWNLOAD = "download"

    @property
    def regex_pattern(self) -> str:
        return rf'.*/{self.value}($|.*)'
