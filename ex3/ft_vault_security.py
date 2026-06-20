#!/usr/bin/env python3
class ParameterError(Exception):
    def __init__(self, message: str = "Wrong parameter was given"):
        super().__init__(message)


def secure_archive(file_name: str, action: str = "r",
                   writing_content: str = "") -> tuple[bool, str]:
    result_content: str = ""
    success: bool = False
    try:
        if action != "w" and action != "r":
            raise ParameterError(f"Your action is wrong {action}")
        try:
            with open(file_name, action) as file:
                if action == "r":
                    file_content = file.read()
                    success = True
                    result_content = file_content
                elif action == "w":
                    file.write(writing_content)
                    success = True
                    result_content = "Content successfully written to file"
        except FileNotFoundError as e:
            result_content = f"{e}"
        except PermissionError as e:
            result_content = f"{e}"
        except UnicodeDecodeError as e:
            result_content = f"{e}"
    except ParameterError as e:
        result_content = f"ParameterError: {e}: must be 'w' or 'r'"
    return (success, result_content)


def test_archive() -> None:
    print("=== Cyber Archives Security ===\n")
    print("Using 'secure_archive' to read from a nonexistent file:")
    save = secure_archive("nonexistent.txt")
    print(save)
    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    save = secure_archive("No_Permision_File")
    print(save)
    print("\nUsing 'secure_archive' to read from a regular file:")
    save = secure_archive("text.txt")
    print(save)
    print("\nUsing 'secure_archive' to write previous content to a new file:")
    save = secure_archive("new.txt", "w", save[1])
    print(save)


if __name__ == "__main__":
    test_archive()
