from typing import Callable

from command.command import Command, InputCommand
from command.result import Result
from command.state import CommandState
from db_driver.mongo_client import MongoClient


def make_execute(client: MongoClient) -> Callable[..., Result]:
    def execute(
        input_command: InputCommand, state: CommandState | None = None
    ) -> Result:
        command = input_command.command
        match command:
            case Command.list_databases:
                return Result(input=command, output=client.databases)
            case Command.list_collections:
                if state is None:
                    return Result(input=command, output="No database selected")
                return Result(
                    input=command,
                    output=client.collections_for(state.selected_database),
                )
            case Command.use_database:
                assert state is not None
                return Result(
                    input=command, output=f"using {state.selected_database} database"
                )
            case Command.exit:
                return Result(input=command, output=None)
            case _:
                raise NotImplementedError(f"Command {command} not implemented")

    return execute
