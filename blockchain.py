"""Program to create a small Blockchain having a user defined number of blocks"""

from datetime import datetime
import hashlib as hasher


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return 'Block #{}'.format(self.index)

    def hash_block(self):
        sha = hasher.sha256()
        seq = (str(x) for x in (
               self.index, self.timestamp, self.data, self.previous_hash))
        sha.update(''.join(seq).encode('utf-8'))
        return sha.hexdigest()


def i_am_the_first_block():
    """The first block!"""
    block = Block(index=0,
                  timestamp=datetime.now(),
                  data="This is the Genesis Block",
                  previous_hash="0")
    return block


def next_block(last_block, data=''):
    """function returns the next block in the blockchain."""
    idx = last_block.index + 1
    block = Block(index=idx,
                  timestamp=datetime.now(),
                  data='{}{}'.format(data, idx),
                  previous_hash=last_block.hash)
    return block


def create_blockchain():
    print('-------Welcome to our world of a Small Blockchain--------');
    noOfBLocks = int(input('Enter the number of blocks for our blockchain')) 
    msg = input('Input the message to be stored in the blockchain')  
    blockchain = [i_am_the_first_block()]
    prev_block = blockchain[0]
    for _ in range(0, noOfBLocks):
      block = next_block(prev_block, data=msg)
      blockchain.append(block)
      prev_block = block
      print('{} added to blockchain'.format(block))
      print('Hash: {}\n'.format(block.hash))


# run the test code
create_blockchain()