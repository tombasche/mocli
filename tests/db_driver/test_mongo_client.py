import pytest

from db_driver.mongo_client import MongoClient


@pytest.fixture(autouse=True, scope="session")
def connection() -> MongoClient:
    return MongoClient("mongodb://localhost:27017")


def test_db_connection(connection):
    assert connection.up is True


def test_list_databases(connection):
    expected_databases = ["admin", "config", "local"]
    assert all(
        [expected_db in connection.databases for expected_db in expected_databases]
    )


def test_list_collections(connection):
    collections = connection.collections_for("admin")
    expected_collections = ["system.version"]
    assert all(
        [
            expected_collection in collections
            for expected_collection in expected_collections
        ]
    )
