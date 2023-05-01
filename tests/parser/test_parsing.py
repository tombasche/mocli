from command.command import InputCommand, Command
from parser.parse import parse


def test_parse_input():
    result = parse("list databases")
    assert result.value == InputCommand(Command.list_databases, arguments=[])
    assert result.ok()


def test_parse_input_with_arguments():
    result = parse("list collections admin")
    assert result.value == InputCommand(Command.list_collections, arguments=["admin"])
    assert result.ok()


def test_parse_invalid_input():
    result = parse("blah blah blah")
    assert not result.ok()
    assert str(result.error) == "Invalid input: blah blah blah"
