import sys
ZERO = 0
ONE = 1
TWO = 2
THREE = 3


def get_text_and_table_paths():
    """
    Function handles input and returns a tbl and txt file paths.
    :return filename: path to the tbl and/or txt file
    """
    if len(sys.argv) != THREE:
        # if incorrect number of arguments given the program exits with error.
        print("not enough arguments given")
        sys.exit(1)
    # Checks extensions of txt and tbl file paths, exits if invalid.
    if not ((sys.argv[1].endswith(".txt") and sys.argv[2].endswith(".tbl")) or
            (sys.argv[2].endswith(".txt") and sys.argv[1].endswith(".tbl"))):
        print("One of files should have extension .txt and another file should have .tbl extension")
        sys.exit(1)
    # assign text and table file paths if first file is a text file.
    if sys.argv[1].endswith(".txt"):
        text_file_path = sys.argv[1]
        table_file_path = sys.argv[2]
        return text_file_path, table_file_path
    # assign text and table file paths if first file is a table file.
    text_file_path = sys.argv[2]
    table_file_path = sys.argv[1]
    return text_file_path, table_file_path


def decode(text_path, dictionary_from_tbl):
    """
    Function reads file and decodes using text_path and dictionary_from_tbl
    :param text_path: The filename to read
    :param dictionary_from_tbl: a dictionary of char: binary pairs.
    """
    # get list of keys from the dictionary
    key_list = list(dictionary_from_tbl.keys())
    # initialize variables
    decoded_char = ""
    key = ""
    try:
        # open file
        with open(text_path) as input_file:
            # loop until variable changes value to False
            keep_looping = True
            while keep_looping:
                # read char from a file
                char = input_file.read(1)
                # update key value
                key = key + char
                # if key found in the list, decode key and print it, clear the key value
                if key in key_list:
                    decoded_char = dictionary_from_tbl[key]
                    print(decoded_char, end='')
                    key = ""
                # if reaches the end of the file, then stop looping
                if not char:
                    keep_looping = False
    except IOError as ioe:
        sys.exit(f"Error reading text file!\nIOError -> {ioe}")


def make_dictionary(table_path):
    """
    Creates dictionary based on table file
    :param table_path: file path that has a table
    :return dictionary from table that will be used in decoding
    """
    # initialize dictionary
    dictionary_from_tbl = {}
    try:
        # open file for reading
        with open(table_path) as input_file:
            # References:
            # read line by line https://www.geeksforgeeks.org/read-a-file-line-by-line-in-python/
            # find all lines in input file
            list_of_lines = input_file.readlines()
            # loop through list of lines
            for line in list_of_lines:
                # split line using delimeter :
                split_line = line.split(":")

                # check if line has a character ':', based on length
                if len(split_line) == THREE:
                    # this line has a character ':', key can be found at index 2
                    key = split_line[2]
                else:
                     # this line does not have a character ':', key can be found at index 1
                    key = split_line[1]

                # last char in string https://thispointer.com/python-how-to-get-last-n-characters-in-a-string/#:~:text=The%20last%20character%20of%20a%20string%20has%20index%20position%20%2D1,in%20the%20square%20brackets%20i.e.&text=It%20returned%20a%20copy%20of%20the%20last%20character%20in%20the%20string.
                # remove char from string https://careerkarma.com/blog/python-remove-character-from-string/
                # get last char
                last_char = key[-1]
                # check if last char is a new line, remove it if found
                if last_char == "\n":
                    key = key[:-1]
                # remove first element in string https://stackoverflow.com/questions/4945548/remove-the-first-character-of-a-string
                # remove " in the end and beginning of string
                value = split_line[0]
                value = value[1:]
                value = value[:-1]
                # assign correct value for new line char
                if value == "\\n":
                    value = "\n"
                # check if line has a char ":"
                if len(split_line) == THREE:
                    # assign correct value for char ":"
                    value = ":"
                # populate dictionary with key, value pairs
                dictionary_from_tbl[key] = value
    except IOError as ioe:
        # exit with if there is an error reading table file
        sys.exit(f"Error reading table file!\nIOError -> {ioe}")
    return dictionary_from_tbl


def main():
    """
    Main function gets file paths from user input and decodes txt file using table.
    """
    # find files paths
    text_path, table_path = get_text_and_table_paths()
    # create dictionary from file
    dictionary_from_tbl = make_dictionary(table_path)
    # decode text file using dictionary
    decode(text_path, dictionary_from_tbl)


main()
