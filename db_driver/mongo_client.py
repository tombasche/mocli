import pymongo


class MongoClient:
    def __init__(self, connection_string: str):
        self.connection = pymongo.MongoClient(connection_string)

    @property
    def up(self) -> bool:
        return self.connection is not None

    @property
    def databases(self) -> list[str]:
        return self.connection.list_database_names()

    def collections_for(self, database: str) -> list[str]:
        return self.connection[database].list_collection_names()
