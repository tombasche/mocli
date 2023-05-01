from typing import Generic, TypeVar

import attr

from command.command import Command

T = TypeVar("T")


@attr.s(auto_attribs=True, frozen=True)
class Result(Generic[T]):
    input: Command
    output: T
