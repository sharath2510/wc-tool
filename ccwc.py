import argparse
import chardet #pip install chardet
import locale

def args_setup():
    parser = argparse.ArgumentParser(description="Count number of bytes/lines/words/characters in file")
    parser.add_argument("file_name", type=str, help="Name of the file to process")
    parser.add_argument("-c", action="store_true", help="Count number of bytes in file")
    parser.add_argument("-l", action="store_true", help="Count number of lines in file")
    parser.add_argument("-w", action="store_true", help="Count number of words in file")
    parser.add_argument("-m", action="store_true", help="Count number of characters in file")
    args = parser.parse_args()

    # If none of the count options are provided, display the -c, -l & -w options
    if not any([args.c, args.l, args.w, args.m]):
        args.c = args.l = args.w = True

    return args

def detect_file_encoding(file_name):
    with open(file_name, 'rb') as file:
        file_content = file.read()
        result = chardet.detect(file_content)
        encoding = result['encoding']
        return encoding

def is_multibyte_supported():
    current_locale = locale.getlocale()
    if current_locale:
        encoding = current_locale[1]
        if encoding:
            return "UTF-8" in encoding or "utf-8" in encoding
    return False

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

def count_characters(file_name, encoding):
    if is_multibyte_supported():
        with open(file_name, "r", encoding=encoding) as file:
            content = file.read()
            character_count = len(content)
        print(character_count, end=' ')
    else:
        count_bytes(file_name)

def main(args):
    file_name = args.file_name
    encoding = detect_file_encoding(file_name)
    if args.c:
        count_bytes(file_name)
    if args.l:
        count_lines(file_name, encoding)
    if args.w:
        count_words(file_name, encoding)
    if args.m:
        count_characters(file_name, encoding)
    print(args.file_name)

if __name__ == "__main__":
    args = args_setup()
    main(args)