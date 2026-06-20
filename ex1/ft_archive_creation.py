#!/usr/bin/env python3
import sys
import typing


class UsageError(Exception):
    def __init__(self, massage: str = "Usage Error"):
        super().__init__(massage)


def archive() -> None:
    try:
        if (len(sys.argv) != 2):
            raise UsageError(sys.argv[0])
        file_name = sys.argv[1]

        try:
            print("=== Cyber Archives Recovery & Preservation ===")
            print(f"Accessing file '{file_name}'")
            file: typing.IO[str] = open(file_name, "r")
            print("---\n")
            file_content = file.read()
            print(file_content)
            print("\n---")
            file.close()
            print(f"\nFile '{file_name}' closed.\n")
            print("Transform data:\n---\n")
            trasform_text = ""
            trasform_text = ''

        except FileNotFoundError as e:
            print(f"Error opening file '{file_name}': {e}")
        except PermissionError as e:
            print(f"Error opening file '/{file_name}': {e}")
        except UnicodeDecodeError as e:
            print(f"Error opening file '{file_name}': {e}")
    except UsageError as e:
        print(f"Usage: {e} <file>")


if __name__ == "__main__":
    archive()
