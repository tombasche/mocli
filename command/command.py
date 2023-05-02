from enum import StrEnum

import attr

from command.state import CommandState


class Command(StrEnum):
    list_databases = "list databases"
    list_collections = "list collections"
    use_database = "use"

    exit = "exit"


@attr.s(auto_attribs=True, frozen=True)
class InputCommand:
    command: Command
    next_state: CommandState | None = None
