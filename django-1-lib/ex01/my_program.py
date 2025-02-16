#!/usr/bin/python3
from path import Path


def main():
    dir_path = Path("some_dir")
    file_path = "some_file"
    dir_path.mkdir_p()
    Path.touch(f"{dir_path}/{file_path}")
    file = Path(f"{dir_path}/{file_path}")
    file.write_lines(["42"])
    print(file.read_text(), end="")


if __name__ == '__main__':
    main()
