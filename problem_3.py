# Huffman Coding in python
import sys

# Creating tree nodes
class NodeTree(object):

    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

    def children(self):
        return (self.left, self.right)

    def nodes(self):
        return (self.left, self.right)

    def __str__(self):
        return '%s_%s' % (self.left, self.right)


# Main function implementing huffman coding
def huffman_code_tree(node, left=True, binString=''):
    if type(node) is str:
        return {node: binString}
    (left, right) = node.children()
    huff_dict = dict()
    huff_dict.update(huffman_code_tree(left, True, binString + '0'))
    huff_dict.update(huffman_code_tree(right, False, binString + '1'))
    return huff_dict


# Calculating frequency
a_great_sentence_initial = "The bird is the word"

#making the sentence to be in lowercase so that both cases of capital or lowercase of each word can be of same format
a_great_sentence = a_great_sentence_initial.lower()

frequency_tab = {char : a_great_sentence.count(char) for char in set(a_great_sentence)} 
#reverse=True is used to set the dict from the end of it
frequency_dict = [(key,value) for (key, value) in sorted(frequency_tab.items(), key=lambda x: x[1], reverse=True)]

nodes = frequency_dict

while len(nodes) > 1:
    #last node based on the sort in the reverse order
    (key1, c1) = nodes[-1]
    #second to last node
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffmanCode = huffman_code_tree(nodes[0][0])

print(' Char | Huffman code | size ')
print('----------------------')
for (char, frequency) in frequency_dict:
    print(' %-4r| %-4r  |%12s |%-4r ' % (char, sys.getsizeof(char), huffmanCode[char], sys.getsizeof(int(huffmanCode[char], base=2))))
    




            

