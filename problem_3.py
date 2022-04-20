# Huffman Coding in python
import sys

def char_freq(string):
    string = string.lower()#to ensure all characters are in the same case
    char_freq_dict = dict()
    for key in string:
        if char_freq_dict.get(key):
            char_freq_dict[key] += 1
        else:
            char_freq_dict[key] = 1 
    
    return [(key,value) for (key, value) in sorted(char_freq_dict.items(), key=lambda x: x[1])]
# Creating tree nodes
class Node:
    def __init__(self,frequency, char=None):
        self.char=char
        self.freq=frequency
        self.prev=None
        self.next=None
        self.left=None
        self.right=None
    
    def is_leaf(self):
        return (self.left is None and self.right is None)


# Main function implementing huffman coding which  is the Priority QUEUE
class Priority_Queue:
    def __init__(self):
        self.head=None
        self.tail=None
    def add_node(self, node):
        if self.head is None:
            self.head=node
            self.tail=node
            return
        head=self.head
        while(head is not None and head.freq<=node.freq):
            head=head.next
        #if we traverse through queue and need to insert node at head
        if head==self.head:
            node.next=self.head
            self.head.prev=node
            self.head=self.head.prev
            return
        #if we traverse through queue and need to insert node at tail
        if head==self.tail or head==None:
            self.tail.next=node
            node.prev=self.tail
            self.tail=self.tail.next
            return
        #node inserted in between the queue
        left=head.prev
        left.next=node
        head.prev=node
        node.prev=left
        node.next=head
        return
    
    def delete_node(self):
        node=self.head
        self.head=self.head.next
        node.next=None
        node.prev=None
        return node
    def print_que(self):
        head=self.head
        while head is not None:
            print(head.char, head.freq)
            head=head.next
    def is_empty(self):
        return self.head is None

# building the hoffman tree using the queue
def build_huffman(queue):
    while(not queue.is_empty() and queue.head.next):
        node1=queue.delete_node()
        node2=queue.delete_node()
        total_freq = node1.freq + node2.freq
        new_node = Node(total_freq)
        new_node.left = node1
        new_node.right = node2
        queue.add_node(new_node)
    return queue

def codes(head, string):
    arr=string
    if head.left:
        string+='0'
        codes(head.left, string)
    if head.right:
        string=arr
        string+='1'
        codes(head.right, string)
    if head.is_leaf():
        temp=string
        code_list[head.char]=temp
    return

def find_codes(tree):
    head=tree.head
    if head.is_leaf():
        return {tree.head.char:'0'}
    global code_list
    code_list=dict()
    codes(head, str())
    return code_list

def huffman_encoding(data):
    sorted_char_freq=char_freq(data)
    queue=Priority_Queue()
    for item in sorted_char_freq:
        char=item[0]
        freq=item[1]
        node=Node(freq, char)
        queue.add_node(node)
    tree=build_huffman(queue)
    get_code=find_codes(tree)
    encoded_data=''
    for x in data:
        encoded_data+=get_code[x]
    return encoded_data, tree

def huffman_decoding(data,tree):
    data=str(data)
    head=tree.head
    string=""
    if head.is_leaf():
        for x in data:
            string+=head.char
        return string
    for x in data:
        if head is not None:
            if x=="0":
                temp=head
                head=head.left
            elif x=="1":
                temp=head
                head=head.right
            if head.is_leaf():
                string+=head.char
                head=tree.head
                temp=tree.head
    return string

if __name__ == "__main__":
    

    a_great_sentence = "The bird is the word"
    #to take into account same char with different cases in the string (i.e. Upper and lower cases), 
    # we convert it all to lowercase
    a_great_sentence = a_great_sentence.lower()


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
#CASE II: Same words
    print('CASE II: Same words')
    a_great_sentence = "ZZZZZZZZZZZZZZZZ"
    a_great_sentence = a_great_sentence.lower()


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

#CASE III: Empty
    print('CASE II: Empty string')
    a_great_sentence = " "
    a_great_sentence = a_great_sentence.lower()


    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))

