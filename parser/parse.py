from command.command import InputCommand, Command
from parser.parse_result import ParseResult


def parse(input_str: str) -> ParseResult:
    tokens = input_str.split()
    if tokens[0] == "exit":
        return ParseResult(value=InputCommand(command=Command.exit, arguments=[]))
    if tokens[0] == "list":
        if tokens[1] == "databases":
            return ParseResult(
                value=InputCommand(command=Command.list_databases, arguments=[])
            )
        elif tokens[1] == "collections":
            return ParseResult(
                value=InputCommand(
                    command=Command.list_collections, arguments=[tokens[2]]
                )
            )
    return ParseResult(error=Exception(f"Invalid input: {input_str}"))
