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
    def __lt__(self, other):
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
        # reference: string method in python https://www.educative.io/edpresso/what-is-the-str-method-in-python
        if self.bit != None:
            bit = int(self.bit)
        else:
            bit = self.bit
        return f'{self.char, self.count, self.left, self.right, bit}'

    # PART3 (representation)
    def __repr__(self):
        return 'Huffman Tree(' + repr(self.char) + ',' + repr(self.count) + ',' + repr(self.left) + ',' + repr(
            self.right) + ',' + repr(self.bit) + ')'

    # PART5 (equality)
    def __eq__(self, other):


# PART1 (make_trees)

def make_trees(dictionary):
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
    print(f'a = {a}')
    print(f'b = {b}')
    return HuffmanTree(char, count, left, right, bit)


dictionary = {"o": 10, "l": 15, "w": 5, "h": 5, "r": 5, "d": 5, "e": 5}

list_of_trees = (make_trees(dictionary))
obj1 = (list_of_trees[0])
obj2 = (list_of_trees[1])
obj3 = HuffmanTree('d', 5, 'hro', 'world', 0)
obj4 = HuffmanTree('    ', 5, 6, 7, True)
# print(obj1)
# print(obj2)
# print(obj1 < obj2)
merge(obj1, obj2)
