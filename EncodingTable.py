import sys


class EncodingTable:
    """
    A class to represent an Encoding Table made from a Huffman Tree
    Attributes
    ----------
    encode : str
        The dictionary storing for each symbol "char" as binary bit string code "code"
    """

    def __init__(self, tree):
        """
        Constructs an EncodingTable using a HuffmanTree
        :param tree: The HuffmanTree to use to build the EncodingTable dictionary encode
        """
        # Create empty dictionary
        self.encode = {}
        # Launch recursive function to store values into self.encode dictionary
        self.recurse(tree, "")

    # PART 7 (recurse)
    def recurse(self, tree, code):
        # recursive call
        if tree.bit is not None:
            if tree.bit:
                code = code + "1"
            else:
                code = code + "0"
        # Base case
        if (tree.left and tree.right) is None:
            self.encode[tree.char] = code
        # If not base case
        else:
            self.recurse(tree.left, code)
            self.recurse(tree.right, code)

    # PART 6 (string)

    def encode_text(self, text):
        """
        Encodes the provided text using the internal encoding dictionary (turns each character symbol into a bit string)
        :param text: The string text to encode
        :return: A bit string "000100" based on the internal encode dictionary
        """
        output_text = ""
        # Loop through characters
        for char in text:
            # If one matches then encode into bitstring
            if char in self.encode:
                output_text += self.encode[char]
            else:
                sys.exit(f"Can't encode symbol {char} as it isn't in the encoding table:\n{self}")
        return output_text

    def __str__(self):
        my_dictionary = self.encode
        for key in my_dictionary:
            return print(f"{repr(key)}:" + my_dictionary[key])

