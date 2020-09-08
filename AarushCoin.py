from time import time
from datetime import datetime
import json
import hashlib
import random

class Blockchain(object):
	def __init__(self):
		self.chain = [self.addGenesisBlock()]
		self.pendingTransactions = []
		self.difficulty = 3
		self.minerRewards = 50
		self.blockSize = 10

	def generateKeys(self):
		pass
	
	def minePendingTransactions(self, miner):
		for i in range(0, len(self.pendingTransactions), self.blockSize):
			end = i + self.blockSize
			if i >= len(self.pendingTransactions):
				end = len(self.pendingTransactions)
			transactionSlice = self.pendingTransactions[i:end]
			newBlock = Block(transactionSlice, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), len(self.chain))
			hashVal = self.getLastBlock().hash
			newBlock.previousBlockHash = hashVal
			newBlock.mineBlock(self.difficulty)
			self.chain.append(newBlock)
			print("Mining Transactions Success!")
			payMiner = Transaction("Miner Rewards", miner, self.minerRewards)
			self.pendingTransactions = [payMiner]
		return True

	def addBlock(self, block):
		if len(self.chain) > 0:
			block.previousBlockHash = self.getLastBlock().hash
		else:
			block.previousBlockHash = "None"
		self.chain.append(block)

	def getLastBlock(self):
		return self.chain[-1]

	def packageChain(self):
		output = []
		for block in self.chain:
			innerOutput = {}
			innerOutput["hash"] = block.hash
			innerOutput["index"] = block.index
			innerOutput["previousBlockHash"] = block.previousBlockHash
			innerOutput["time"] = block.time
			innerOutput["nonce"] = block.nonce
			output.append(innerOutput)
			transactionOutput = []
			transactionInnerOutput = {}
			for transaction in block.transactions:
				transactionInnerOutput["time"] = transaction.time
				transactionInnerOutput["sender"] = transaction.sender
				transactionInnerOutput["reciever"] = transaction.reciever
				transactionInnerOutput["amount"] = transaction.amount
				transactionInnerOutput["hash"] = transaction.hash
				transactionOutput.append(transactionInnerOutput)
			innerOutput["transactions"] = transactionOutput
		return output

	def addGenesisBlock(self):
		transactionArray = []
		transactionArray.append(Transaction("Arjun", "Aarush", 10))
		genesis = Block(transactionArray, datetime.now().strftime("%m/%d/%Y, %H:%M:%S"), 0)
		genesis.previousBlockHash = "None"
		return genesis

class Block(object):
	def __init__(self, transactions, time, index):
		self.index = index
		self.transactions = transactions
		self.time = time
		self.previousBlockHash = ""
		self.nonce = 0
		self.hash = self.calculateHash()

	def mineBlock(self, difficulty):
		array = []
		for i in range(0, difficulty):
			array.append(i)
		arrayString = map(str, array)
		hashPuzzle = "".join(arrayString)
		while self.hash[0:difficulty] != hashPuzzle:
			self.nonce += 1
			self.hash = self.calculateHash()
			print(f"Nonce: {self.nonce}")
			print(f"Hash Attempt {self.hash}")
		print(f"Hash We Want {hashPuzzle} ... \n")
		print(f"Block Mined! Nonce to Solve Proof of Work: {self.nonce}")
		return True

	def calculateHash(self):
		hashTransactions = ""
		for transaction in self.transactions:
			hashTransactions += transaction.hash
		hashString = str(self.index) + str(self.nonce) + str(self.time) + hashTransactions
		hashEncoded = json.dumps(hashString, sort_keys=True).encode()
		return hashlib.sha256(hashEncoded).hexdigest()

class Transaction(object):
	def __init__(self, sender, reciever, amount):
		self.sender = sender
		self.reciever = reciever
		self.amount = amount
		self.time = time()
		self.hash = self.calculateHash()

	def calculateHash(self):
		hashString = self.sender + self.reciever + str(self.amount) + str(self.time)
		hashEncoded = json.dumps(hashString).encode()
		return hashlib.sha256(hashEncoded).hexdigest()
