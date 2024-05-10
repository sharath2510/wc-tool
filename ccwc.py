import argparse
import chardet #pip install chardet

def args_setup():
    parser = argparse.ArgumentParser(description="Count number of bytes/lines/words/characters in file")
    parser.add_argument("-c", action="store_true", help="Count number of bytes in file")
    parser.add_argument("-l", action="store_true", help="Count number of lines in file")
    parser.add_argument("-w", action="store_true", help="Count number of words in file")
    args = parser.parse_args()

    # If none of the options are provided, default to True for all options
    if not any(vars(args).values()):
        args.c = args.l = args.w = True

    return args

def main(args):
    file_name = "test.txt"
    encoding = detect_file_encoding(file_name)
    if args.c:
        count_bytes(file_name)
    if args.l:
        count_lines(file_name, encoding)
    if args.w:
        count_words(file_name, encoding)

def detect_file_encoding(file_name):
    with open(file_name, 'rb') as file:
        file_content = file.read()
        result = chardet.detect(file_content)
        encoding = result['encoding']
        return encoding

def count_bytes(file_name):
    # Open file in binary mode "rb" to count number of bytes
    with open(file_name, "rb") as file:
        file_content = file.read()
        num_bytes = len(file_content)
        print(num_bytes, end=' ')

def count_lines(file_name, encoding):
    with open(file_name, "r", encoding=encoding) as file:
        line_count = 0
        for _ in file:
            line_count += 1
    print(line_count, end=' ')

def count_words(file_name, encoding):
    with open(file_name, "r", encoding=encoding) as file:
        word_count = 0
        for line in file:
            word_count += len(line.split())
    print(word_count, end=' ')

if __name__ == "__main__":
    args = args_setup()
    main(args)
    print("test.txt")