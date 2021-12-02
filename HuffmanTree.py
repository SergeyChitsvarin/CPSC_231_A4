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
        self.char = char
        self.count = count
        self.left = left
        self.right = right
        self.bit = bit

    # PART2 (order)
    def __lt__(other, self):
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

    # PART3 (representation)

    # PART5 (equality)

    # PART1 (make_trees)
    @staticmethod
    def make_trees(dictionary):
        # references: static method
        # https://stackoverflow.com/questions/735975/static-methods-in-python
        # https://www.programiz.com/python-programming/methods/built-in/classmethod
        list_of_trees = []
        for char in dictionary:
            # (char, count, left, right, bit):
            huffman_tree = HuffmanTree(char, dictionary[char], None, None, None)
            list_of_trees.append(huffman_tree)

        return list_of_trees


dictionary = {"a": 1, "b": 2, "c": 0, "d": 6}

list_of_trees = (HuffmanTree.make_trees(dictionary))
list_of_trees.sort(reverse=True)
obj1 = (list_of_trees[0])
obj2 = (list_of_trees[1])
print(obj1.char)
print(obj2.count)

# PART4 (merge)

