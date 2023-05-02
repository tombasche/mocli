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
        make_result = result_factory(command)
        match command:
            case Command.list_databases:
                return make_result(output=client.databases)
            case Command.list_collections:
                if state is None:
                    return make_result(output="No database selected")
                return make_result(
                    output=client.collections_for(state.selected_database)
                )
            case Command.use_database:
                assert state is not None
                return make_result(output=f"using {state.selected_database} database")
            case Command.exit:
                return make_result(output=None)
            case _:
                raise NotImplementedError(f"Command {command} not implemented")

    return execute


def result_factory(command: Command) -> Callable[..., Result]:
    return lambda output: Result(command, output)
