import argparse

def args_setup():
    parser = argparse.ArgumentParser(description="Count number of bytes/lines/words/characters in file")
    parser.add_argument("-c", action="store_true", help="Count number of bytes in file")
    return parser.parse_args()

def main(args):
    if args.c:
        count_bytes()

def count_bytes():
    # Open file in binary mode "rb" to count number of bytes
    file_name = "test.txt"
    with open(file_name, "rb") as file:
        file_content = file.read()
        num_bytes = len(file_content)
        print(f"{num_bytes} {file_name}")

if __name__ == "__main__":
    args = args_setup()
    main(args)