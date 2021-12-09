class HuffmanTree:
    """
    A class to represent an Huffman Tree
    Attributes
    ----------
    char : str
        The characters represented by this tree
    count : int
        The count of how many times char occurred in the text
    left : HuffmanTree/None
        The left HuffmanTree below this one
    right : HuffmanTree/None
        The right HuffmanTree below this one
    bit : bool
        The bit symbol used to reach this HuffmanTree (either True/False for 1/0)


    General Structure
                         HuffmanTree (char,count,bit)
                          /    \
                      left    right
                        /        \
                HuffmanTree      HuffmanTree

    Default Structure
                         HuffmanTree (char,count,None)
                          /    \
                      left    right
                        /        \
                     None         None
    """

    # PART1 (constructor)
    def __init__(self, char, count, left, right, bit):
        """
    :param char: individual character
    :param count: amount of times char appears
    :param left: left tree char
    :param right: right tree char
    :param bit:
    :return: constructor
    """
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit

    # PART2 (order)
    def __lt__(self, other):
        """
    __lt__ method
    :param other: other huffman Tree
    :return: less than operator with said conditions
    """
        # reference: using lt method in python https://www.pythonpool.com/python-__lt__/
        if self.count > other.count:
            return True
        if self.count < other.count:
            return False
        if self.char > other.char:
            return True
        else:
            return False

    # PART3 (string)
    def __str__(self):
        """
    __str__ method
    :return: returns string representation of values
    """
        # reference: string method in python https://www.educative.io/edpresso/what-is-the-str-method-in-python
        if self.bit is not None:
            bit = int(self.bit)
        else:
            bit = self.bit
        if self.left is None:
            left = None
        else:
            left = repr(self.left.char)
        if self.right is None:
            right = None
        else:
            right = repr(self.right.char)
        return f"({repr(self.char)},{self.count},{left},{right},{bit})"

    # PART3 (representation)
    def __repr__(self):
        """
    __repr__ method
    :return: string version of value and runs the value through the eval function with specific conditions.
    """
        if self.bit == 1:
            bit = True
        if self.bit == 0:
            bit = False
        if self.bit is None:
            bit = None
        return "HuffmanTree(" + repr(self.char) + "," + repr(self.count) + "," + repr(self.left) + "," + repr(
            self.right) + "," + repr(bit) + ")"

    # PART5 (equality)
    def __eq__(self, other):
        """
    __eq__ method
    :param other: other Huffman Tree
    :return: the equality operator that compares Huffman tree to other Huffman Tree with given conditions.
    """
        if other is None:
            return False
        if self.char == other.char and self.left == other.left and self.right == other.right:
            return True
        else:
            return False


# PART1 (make_trees)

def make_trees(dictionary):
    """
    function makes Huffman Trees
    :param dictionary:
    :return list_of_trees: a list of Huffman trees for each character
    """
    list_of_trees = []
    for char in dictionary:
        huffman_tree = HuffmanTree(char, dictionary[char], None, None, None)
        list_of_trees.append(huffman_tree)
    return list_of_trees


# PART4 (merge)

def merge(t1, t2):
    if t1 < t2:
        a = t2
        b = t1
    else:
        a = t1
        b = t2
    char = a.char + b.char
    count = a.count + b.count
    left = a
    right = b
    bit = None
    a.bit = 0
    b.bit = 1
    return HuffmanTree(char, count, left, right, bit)
