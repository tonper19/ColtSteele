def process_file(p):
    with open(p) as file:
        data = file.readlines()
    print(data)


def main():
    p = "/path/to/datefile.dat"

    try:
        process_file(p)
    except OSError as e:
        print(f"Could not process the file because {str(e)}")

if __name__ == "__main__":
    main()
