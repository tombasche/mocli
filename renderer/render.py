from typing import TypeVar

T = TypeVar("T")


def render(result: T) -> str:
    match result:
        case list():
            return "\n".join(result)
        case str():
            return result
        case _:
            raise NotImplementedError(f"Rendering for {result} not implemented")
