from unittest.mock import Mock


from command.execute import make_execute
from db_driver.mongo_client import MongoClient
from parser.parse import parse


def test_list_collections():
    client = Mock(MongoClient)
    client.collections_for.return_value = ["system.version"]

    execute = make_execute(client)
    command = parse("use admin")
    result = execute(command.value, command.value.next_state)
    assert result.output == "using admin database"

    next_command = parse("list collections")
    result = execute(next_command.value, command.value.next_state)
    assert result.output == ["system.version"]


def test_list_collections_requires_selected_db():
    client = Mock(MongoClient)
    client.collections_for.return_value = ["system.version"]

    execute = make_execute(client)
    command = parse("list collections")
    result = execute(command.value, None)
    assert result.output == "No database selected"
