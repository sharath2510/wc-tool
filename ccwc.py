import argparse

def args_setup():
    parser = argparse.ArgumentParser(description="Count number of bytes/lines/words/characters in file")
    parser.add_argument("-c", type=str, nargs="?", help="Count number of bytes in file")
    return parser.parse_args()

def main(args):
    count_bytes()

def count_bytes():
    with open("test.txt", "rb") as file:
        for line in file:
            print(line)

if __name__ == "__main__":
    args = args_setup()
    main(args)