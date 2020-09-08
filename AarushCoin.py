from time import time
import json
import hashlib
import random

class Blockchain(object):
	def __init__(self):
		self.chain = []

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
		return output

class Block(object):
	def __init__(self, transactions, time, index):
		self.index = index
		self.transactions = transactions
		self.time = time
		self.previousBlockHash = ""
		self.nonce = 0
		self.hash = self.calculateHash()

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
			hashEncoded = json.dumps(hashString, sortKeys=True).encode()
			return hashlib.sha256(hashEncoded).hexdigest()
