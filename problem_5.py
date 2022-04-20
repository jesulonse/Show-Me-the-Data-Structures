import hashlib, datetime

#Block acting as the Node class
class Block:

    def calc_hash(self):
      sha = hashlib.sha256()
      sha.update(self.data.encode('utf-8'))
      return sha.hexdigest()

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.next = None

    def __repr__(self) -> str:
        return str(self.timestamp) + str(' || ')  + str(self.data) + str(' || ') + str(self.previous_hash) + str(' || ') + str(self.hash)

         
#the LinkedList class
class BlockChain_LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data):
        if data is None or data == "":
            return
        if self.head is None:
            self.head = Block(datetime.datetime.utcnow(), data, 0)#datetime.datetime.utcnow() is used because the time is Greenwich Mean Time
            return       
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        node.next = Block(datetime.datetime.utcnow(), data, self.head.hash)
        return
    
    
    #creating the list of block chain
    def to_list(self):
        out_list = []
        block = self.head
        while block:
            out_list.append([block])
            block = block.next
        return out_list


#Edge cases:
#Case I: block chain with data
#The blocks are with the same timestamp being observed from output
print('Case I: block chain with data')
BlockChain_1 = BlockChain_LinkedList()
data_1 = "We are happy now"
data_2 = "We are a glorious people now"
data_3 = "We are going to heaven now"
data_4 = "Nothing can stop us now"

BlockChain_1.append(data_1)
BlockChain_1.append(data_2)
BlockChain_1.append(data_3)
BlockChain_1.append(data_4)

print(BlockChain_1.to_list())

#Block chain with data as "" or empty block
print('Case II: Block chain with data as "" or empty block')
BlockChain_2 = BlockChain_LinkedList()

BlockChain_2.append("")
BlockChain_2.append("")
BlockChain_2.append("")
BlockChain_2.append("")

print(BlockChain_2.to_list())

#Block chain with data as None
print('Case III: Block chain with data as None')
BlockChain_3 = BlockChain_LinkedList()


BlockChain_3.append(None)
BlockChain_3.append(None)
BlockChain_3.append(None)
BlockChain_3.append(None)
print(BlockChain_3.to_list())

#block chain with one of the blocks without data
print('Case IV: block chain with one of the blocks without data')
BlockChain_4 = BlockChain_LinkedList()
data_1 = "First data block"
data_2 = ""
data_3 = "Third data block"
data_4 = "Fourth data block"

BlockChain_4.append(data_1)
BlockChain_4.append(data_2)
BlockChain_4.append(data_3)
BlockChain_4.append(data_4)

print(BlockChain_4.to_list())