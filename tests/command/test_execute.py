from unittest.mock import Mock

import pytest

from command.command import Command, InputCommand
from command.execute import make_execute
from command.state import CommandState
from db_driver.mongo_client import MongoClient


@pytest.fixture
def client():
    return Mock(MongoClient)


def test_list_databases(client):
    expected_databases = ["admin", "config", "local"]
    command = InputCommand(Command.list_databases)
    client.databases.return_value = expected_databases

    result = make_execute(client)(command)

    assert result.input == command.command
    assert result.output.return_value == expected_databases


def test_list_collections(client):
    command = InputCommand(Command.list_collections)
    client.collections_for.return_value = ["system.version"]

    result = make_execute(client)(command, CommandState(selected_database="admin"))

    assert result.input == command.command
    assert result.output == ["system.version"]
    client.collections_for.assert_called_once_with("admin")


def test_exit(client):
    command = InputCommand(Command.exit)

    result = make_execute(Mock())(command)

    assert result.input == command.command
    assert result.output is None
