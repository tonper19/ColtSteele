"""
File I/O examples in Python.
The beginning.

AUTHOR
    Colt Steele
    and some chipotage and testing by Tony Perez
"""


def open_and_read():
    print("*** Read a file at once example")
    f = open("file_io.txt")
    whole_file = f.read()
    print(whole_file)
    f.close()


def line_by_line():
    print("*** Read a file one line at a time an move the cursor example")
    f = open("file_io.txt")
    line = f.readline()
    print(line)
    line = f.readline()
    print(line)
    print("--- Move the cursor to the beginning of the file")
    f.seek(0)  # move the cursor to the beginning
    line = f.readline()
    print(line)
    f.close()


def all_lines_in_a_list():
    print("*** Read all the lines of a files and store them in a list example")
    f = open("file_io.txt")
    lines = f.readlines()
    print(lines)
    f.close()


def with_open():
    print("*** With statement: popular and no need to close the file")
    with open("file_io.txt") as file:
        data = file.readlines()
    print(data)


if __name__ == "__main__":
    open_and_read()
    line_by_line()
    all_lines_in_a_list()
    with_open()
