import hashlib
import time
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        timestamp = time.time()
        return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = create_new_block(previous_block, data)
        self.chain.append(new_block)

    def print_chain(self):
        print_blockchain(self.chain)
class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = f"{index}{previous_hash}{timestamp}{data}".encode()
    return hashlib.sha256(value).hexdigest()

def create_genesis_block():
    timestamp = time.time()
    return Block(0, "0", timestamp, "Genesis Block", calculate_hash(0, "0", timestamp, "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = time.time()
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

def print_blockchain(blockchain):
    for block in blockchain:
        print(f"Block {block.index}:")
        print(f"  Previous Hash: {block.previous_hash}")
        print(f"  Data: {block.data}")
        print(f"  Hash: {block.hash}")
        print(f"  Timestamp: {block.timestamp}")
        print("-" * 40)

# Create the blockchain
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# Add 6 more blocks
for i in range(1, 7):
    new_block = create_new_block(previous_block, f"Block {i} Data")
    blockchain.append(new_block)
    previous_block = new_block

# Print the blockchain
print_blockchain(blockchain)