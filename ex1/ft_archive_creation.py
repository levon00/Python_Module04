#!/usr/bin/env python3
import sys
import typing


class UsageError(Exception):
    def __init__(self, massage: str = "Usage Error"):
        super().__init__(massage)


def archive() -> None:
    flag = 0
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
            print(f"File '{file_name}' closed.\n")
            print("Transform data:\n---\n")
            trasform_text = file_content.replace("\n", "#\n") + "#"
            print(trasform_text)
            print("\n---")
            file_name = input("Enter new file name (or empty): ")
            if file_name == "":
                print("Not saving data.")
            else:
                print(f"Saving data to '{file_name}'")
                flag = 1
                file = open(file_name, "w")
                file.write(trasform_text)
                flag = 0
                print(f"Data saved in file '{file_name}'.")
        except FileNotFoundError as e:
            print(f"Error opening file '{file_name}': {e}")
        except PermissionError as e:
            print(f"Error opening file '/{file_name}': {e}")
        except UnicodeDecodeError as e:
            print(f"Error opening file '{file_name}': {e}")
    except UsageError as e:
        print(f"Usage: {e} <file>")
    if flag:
        print("Data not saved.")


if __name__ == "__main__":
    archive()
