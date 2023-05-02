from command.command import InputCommand, Command
from command.state import CommandState
from parser.parse_result import ParseResult


def parse(input_str: str) -> ParseResult:
    tokens = input_str.split()
    if tokens[0] == "exit":
        return ParseResult(value=InputCommand(command=Command.exit))

    if tokens[0] == "use":
        return ParseResult(
            value=InputCommand(
                command=Command.use_database,
                next_state=CommandState(selected_database=tokens[1]),
            )
        )
    if tokens[0] == "list":
        if tokens[1] == "databases":
            return ParseResult(value=InputCommand(command=Command.list_databases))
        elif tokens[1] == "collections":
            return ParseResult(
                value=InputCommand(
                    command=Command.list_collections,
                )
            )
    return ParseResult(error=Exception(f"Invalid input: {input_str}"))
