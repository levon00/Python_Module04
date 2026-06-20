#!/usr/bin/env python3
import sys
import typing


class UsageError(Exception):
    def __init__(self, massage: str = "Usage Error"):
        super().__init__(massage)


def management() -> None:
    flag = 0
    try:
        if (len(sys.argv) != 2):
            raise UsageError(sys.argv[0])
        file_name = sys.argv[1]

        try:
            sys.stdout.write("=== Cyber Archives Recovery &" +
                             " Preservation ===\n" +
                             f"Accessing file '{file_name}'\n")
            sys.stdout.flush()
            file: typing.IO[str] = open(file_name, "r")
            sys.stdout.write("---\n\n")
            file_content = file.read()
            sys.stdout.write(file_content + "\n\n---\n")
            file.close()
            sys.stdout.write(f"File '{file_name}' closed.\n\n" +
                             "Transform data:\n---\n\n")
            trasform_text = file_content.replace("\n", "#\n")
            if trasform_text[-1] != "\n":
                trasform_text += "#"
            sys.stdout.write(trasform_text + "\n\n---\n")
            sys.stdout.write("Enter new file name (or empty): ")
            sys.stdout.flush()
            file_name = sys.stdin.readline()
            file_name = file_name[:-1]
            if file_name == "":
                sys.stdout.write("Not saving data.\n")
            else:
                sys.stdout.write(f"Saving data to '{file_name}'\n")
                sys.stdout.flush()
                flag = 1
                file = open(file_name, "w")
                file.write(trasform_text)
                flag = 0
                sys.stdout.write(f"Data saved in file '{file_name}'.\n")
        except FileNotFoundError as e:
            sys.stderr.write(" [STDERR] Error opening file " +
                             f"'{file_name}': {e}\n")
        except PermissionError as e:
            sys.stderr.write(" [STDERR] Error opening file " +
                             f"'{file_name}': {e}\n")
        except UnicodeDecodeError as e:
            sys.stderr.write(" [STDERR] Error opening file " +
                             f"'{file_name}': {e}\n")
    except UsageError as e:
        sys.stderr.write(f" [STDERR] Usage: {e} <file>\n")
    sys.stderr.flush()
    if flag:
        sys.stdout.write("Data not saved.")
    sys.stdout.flush()


if __name__ == "__main__":
    management()
