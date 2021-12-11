# COURSE CPSC 231 FALL 2021
# INSTRUCTOR: Jonathan Hudson
# Tutorial: 02
# ID: 30154758
# Date: 2021/12/10
# description: creates huffman trees using char, count, left, right and bit. Also compares huffman trees
# and has string representation of huffman trees.
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
    constructs a huffman tree using char, count, left, right and bit.
    :param char: individual character
    :param count: amount of times char appears
    :param left: left tree char
    :param right: right tree char
    :param bit: tree bit
    """
        # assign instance variables
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
    :return: result of less than comparison
    """
        # reference: using lt method in python https://www.pythonpool.com/python-__lt__/
        # compare count values of both trees, if self count is greater, then return True
        if self.count > other.count:
            return True
        # if self.count is less than the other tree count, then return False
        if self.count < other.count:
            return False
        # next compare chars of both trees, if self char is greater than other tree char,
        # then return true, otherwise false
        if self.char > other.char:
            return True
        else:
            return False

    # PART3 (string)
    def __str__(self):
        """
    __str__ method
    :return: returns string representation of instance
    """
        # reference: string method in python https://www.educative.io/edpresso/what-is-the-str-method-in-python
        # convert bit to int if it is not None, otherwise keep it as None
        if self.bit is not None:
            bit = int(self.bit)
        else:
            bit = self.bit
        # check if left tree is None, keep it as None if it is
        # otherwise assign left to representation of the left child char
        if self.left is None:
            left = None
        else:
            left = repr(self.left.char)
        # check if right tree is None, keep it as None if it is
        # otherwise assign right to representation of the right child char
        if self.right is None:
            right = None
        else:
            right = repr(self.right.char)
        # return string representation of instance
        return f"({repr(self.char)},{self.count},{left},{right},{bit})"

    # PART3 (representation)
    def __repr__(self):
        """
    __repr__ method
    :return: string representation of Huffman Tree.
    """
        # if bit is 1, then display bit as True
        # if bit is 0, then display bit as False
        # otherwise show it as None
        if self.bit == 1:
            bit = True
        if self.bit == 0:
            bit = False
        if self.bit is None:
            bit = None
        # string representation of Huffman Tree.
        return "HuffmanTree(" + repr(self.char) + "," + repr(self.count) + "," + repr(self.left) + "," + repr(
            self.right) + "," + repr(bit) + ")"

    # PART5 (equality)
    def __eq__(self, other):
        """
    __eq__ method
    :param other: other Huffman Tree
    :return: returns true if huffman trees are the same or false otherwise
    """
        # compare Huffman trees and return true if trees are the same, otherwise false
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
    :param dictionary: a dictionary in which the key is char and the value is count.
    :return list_of_trees: a list of Huffman trees for each character
    """
    list_of_trees = []
    # check each char in dictionary
    for char in dictionary:
        # making a huffman tree for each character then adding the trees to list.
        huffman_tree = HuffmanTree(char, dictionary[char], None, None, None)
        list_of_trees.append(huffman_tree)
    return list_of_trees


# PART4 (merge)
def merge(t1, t2):
    """
    The function takes two Huffman trees and merges them.
    :param t1: one Huffman tree to be merged
    :param t2: other Huffman tree to be merged
    :return one Huffman tree merged from t1 and t2
    """
    # the program checks which tree is larger and assigns a to the bigger of the two.
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
