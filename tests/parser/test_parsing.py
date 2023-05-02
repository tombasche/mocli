from command.command import InputCommand, Command
from parser.parse import parse


def test_parse_input():
    result = parse("list databases")
    assert result.value == InputCommand(Command.list_databases)
    assert result.ok()


def test_parse_invalid_input():
    result = parse("blah blah blah")
    assert not result.ok()
    assert str(result.error) == "Invalid input: blah blah blah"
