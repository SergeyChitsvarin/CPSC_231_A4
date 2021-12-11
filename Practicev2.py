import sys
ZERO = 0
ONE = 1
TWO = 2
THREE = 3


# my_dictionary = {"a": "0",
#                  "b": "10",
#                  "c": "11"}
# binary_string = "00001010111111"


def get_text_and_table_paths():
    """
    Function handles input
    :return filename: path to the tbl and/or txt file
    """
    if len(sys.argv) != THREE:
        # if no arguments were given the program will exit.
        print("not enough arguments given")
        sys.exit(1)

    # if any arguments are given they are written down as table_path and text_path depending on their ending.

    if not ((sys.argv[1].endswith(".txt") and sys.argv[2].endswith(".tbl")) or
            (sys.argv[2].endswith(".txt") and sys.argv[1].endswith(".tbl"))):
        print("One of files should have extension .txt and another file should have .tbl extension")
        sys.exit(1)

    if sys.argv[1].endswith(".txt"):
        text_file_path = sys.argv[1]
        table_file_path = sys.argv[2]
        return text_file_path, table_file_path

    text_file_path = sys.argv[2]
    table_file_path = sys.argv[1]
    return text_file_path, table_file_path


def decode(text_path, dictionary_from_tbl):
    """
    Function reads file and decodes.
    :param text_path: The filename to read
    :return: A string of contents
    """
    key_list = list(dictionary_from_tbl.keys())
    decoded_string = ""
    key = ""
    try:
        with open(text_path) as input_file:
            
            keep_looping = True
            while keep_looping:
                char = input_file.read(1)
                
                key = key + char
                if key in key_list:
                     decoded_char = dictionary_from_tbl[key]
                     print(decoded_char, end='')
                     key = ""
                if not char:
                    keep_looping = False
    except IOError as ioe:
        sys.exit(f"Error reading input file!\nIOError -> {ioe}")


def make_dictionary(table_path):
    dictionary_from_tbl = {}
    try:
        with open(table_path) as input_file:
            list_of_lines = input_file.readlines()
            # References:
            # read line by line https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
            for line in list_of_lines:
                split_line = line.split(":")
                if len(split_line) == THREE:
                    key = split_line[2]
                else:
                    key = split_line[1]
                # last char in string https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/#:~:text=The%20last%20character%20of%20a%20string%20has%20index%20position%20%2D1,in%20the%20square%20brackets%20i.e.&text=It%20returned%20a%20copy%20of%20the%20last%20character%20in%20the%20string.
                # remove char from string https://careerkarma.com/blog/python-remove-character-from-string/
                last_char = key[-1]
                if last_char == "\n":
                    key = key[:-1]
                # remove first element in string https://stackoverflow.com/questions/4945548/remove-the-first-character-of-a-string
                value = split_line[0]
                value = value[1:]
                value = value[:-1]
                if value == "\\n":
                    value = "\n"
                if len(split_line) == THREE:
                    value = ":"
                dictionary_from_tbl[key] = value
    except IOError as ioe:
        sys.exit(f"Error reading table file!\nIOError -> {ioe}")
    return dictionary_from_tbl


def separate_char(new_dictionary, binary_list):
    key_list = list(new_dictionary.keys())
    decoded_string = ""
    key = ""
    for char in binary_list:
        if char in key_list and key == "":
            # print(new_dictionary[char])
            decoded_string = decoded_string + new_dictionary[char]
            key = ""
        else:
            key = key + char
        if key in key_list:
            # print(new_dictionary[key])
            decoded_string = decoded_string + new_dictionary[key]
            key = ""

    return decoded_string


def main():
    text_path, table_path = get_text_and_table_paths()
    dictionary_from_tbl = make_dictionary(table_path)
    decode(text_path, dictionary_from_tbl)

main()
