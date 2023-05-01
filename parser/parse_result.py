from typing import Generic, TypeVar

import attr

T = TypeVar("T")


@attr.s(auto_attribs=True, frozen=True)
class ParseResult(Generic[T]):
    error: Exception | None = None
    value: T | None = None

    def ok(self) -> bool:
        return self.error is None and self.value is not None
