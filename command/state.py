import attr


@attr.s(auto_attribs=True, frozen=True)
class CommandState:
    selected_database: str
