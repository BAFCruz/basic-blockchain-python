#generates timestamps
import datetime

#lib required to calculate hash
import hashlib

class Block:

	def __init__(self, blockID, data, previousHash, timestamp):
		
		self.blockID = blockID
		self.data = data
		self.previousHash = previousHash
		self.timestamp = timestamp
		self.hash = self.hashBlock()

#creates the genesis block 
	def createGenesis():
		#Must match previous def __init__(self, ...) / constructor declared order, otherwise wont work as intended, also caution when printing
		return Block(0, None, 0x0, datetime.datetime.now()) #Constructor order: 'blockID', 'data', 'previousHash', 'timestamp'


#calculates a block hash
	def hashBlock(self):
		
		h = hashlib.sha256()
		h.update(str(self.blockID).encode() + str(self.data).encode() +
			str(self.previousHash).encode() + str(self.timestamp).encode())
        
		return h.hexdigest()


class Blockchain:

#starts blockchain with genesis block as 1st block
	blockchain = [Block.createGenesis()]
	previousBlock = blockchain[0]

#prints Genesis block info
	print("Genesis Block ID: {}".format(blockchain[0].blockID))
	print("Timestamp: {}".format(blockchain[0].timestamp))
	print("Genesis Hash: {}".format(blockchain[0].hash))
	print("\n")

#generates new blocks for the blockchain
	def nextBlock(previousBlock):
		
		next_blockID = previousBlock.blockID + 1
		next_timestamp = datetime.datetime.now()
		next_data = "Block successfully created"
		next_hash = previousBlock.hash

		return Block(next_blockID, next_data, next_hash, next_timestamp) #Must match the blockchain order
	

#generates the blockchain, given a number of blocks
	numberBlocks = 5

	for n in range (0, numberBlocks):
		
		addBlock = nextBlock(previousBlock)
		blockchain.append(addBlock)
		previousBlock = addBlock

		print("Block ID: {}".format(addBlock.blockID))
		print("Timestamp: {}".format(addBlock.timestamp))
		print("Data: {}".format(addBlock.data))
		print("Previous Block Hash: {}".format(addBlock.previousHash))
		print("Current Block Hash: {}".format(addBlock.hash))
		print("\n")
