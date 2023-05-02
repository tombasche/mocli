import signal
from sys import stdout

from command.execute import make_execute
from db_driver.mongo_client import MongoClient
from parser.parse import parse
from renderer.render import render


def write(text: str) -> None:
    stdout.write(text)
    stdout.write("\n")


def exit_cli(_signal, _frame):
    print("\nGoodbye!", flush=True)
    exit(0)


signal.signal(signal.SIGINT, exit_cli)


def main():
    execute = make_execute(MongoClient("mongodb://localhost:27017"))
    state = None
    while True:
        raw_input = input("> ")
        command = parse(raw_input)
        if not command.ok():
            write(f"{command.error}\n")
            continue
        unwrapped_command = command.value
        state = unwrapped_command.next_state or state
        output = execute(unwrapped_command, state).output
        if output is None:
            exit(0)
        write(render(output))


if __name__ == "__main__":
    main()
