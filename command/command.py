from enum import StrEnum
from typing import TypeVar, Generic

import attr


class Command(StrEnum):
    list_databases = "list databases"
    list_collections = "list collections"

    exit = "exit"


T = TypeVar("T")


@attr.s(auto_attribs=True, frozen=True)
class InputCommand(Generic[T]):
    command: Command
    arguments: list[T]
