#!/usr/bin/env python3
import sys
import typing


class UsageError(Exception):
    def __init__(self, massage: str = "Usage Error"):
        super().__init__(massage)


def ancient() -> None:
    try:
        if (len(sys.argv) != 2):
            raise UsageError(sys.argv[0])
        file_name = sys.argv[1]

        try:
            print("=== Cyber Archives Recovery ===")
            print(f"Accessing file '{file_name}'")
            file: typing.IO[str] = open(file_name, "r")
            print("---\n")
            print(file.read())
            print("\n---")
            file.close()
            print(f"\nFile '{file_name}' closed.")

        except FileNotFoundError as e:
            print(f"Error opening file '{file_name}': {e}")
        except PermissionError as e:
            print(f"Error opening file '/{file_name}': {e}")
        except UnicodeDecodeError as e:
            print(f"Error opening file '{file_name}': {e}")
    except UsageError as e:
        print(f"Usage: {e} <file>")


if __name__ == "__main__":
    ancient()
