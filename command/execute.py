from typing import Callable

from command.command import Command, InputCommand
from command.result import Result
from db_driver.mongo_client import MongoClient


def make_execute(client: MongoClient) -> Callable[[InputCommand], Result]:
    def execute(input_command: InputCommand) -> Result:
        command = input_command.command
        arguments = input_command.arguments
        match command:
            case Command.list_databases:
                return Result(input=command, output=client.databases)
            case Command.list_collections:
                return Result(
                    input=command, output=client.collections_for(arguments[0])
                )
            case Command.exit:
                return Result(input=command, output=None)
            case _:
                raise NotImplementedError(f"Command {command} not implemented")

    return execute
