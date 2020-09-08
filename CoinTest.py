from AarushCoin import *
from time import time
import pprint

prettyPrint = pprint.PrettyPrinter(indent=4)

blockchain = Blockchain()

transaction = Transaction("Person1", "Person2", 10)
blockchain.pendingTransactions.append(transaction)

transaction = Transaction("Person1", "Person2", 10)
blockchain.pendingTransactions.append(transaction)

blockchain.minePendingTransactions("Aarush")
blockchain.minePendingTransactions("Arjun")

prettyPrint.pprint(blockchain.packageChain())
print(f"Length: {len(blockchain.chain)}")
"""
from AarushCoin import *
from time import time
import pprint

prettyPrint = pprint.PrettyPrinter(indent=4)

blockchain = Blockchain()
transactions = []

block = Block(transactions, time(), 0)
blockchain.addBlock(block)

block = Block(transactions, time(), 1)
blockchain.addBlock(block)

block = Block(transactions, time(), 2)
blockchain.addBlock(block)

prettyPrint.pprint(blockchain.packageChain())
print(f"Length: {len(blockchain.chain)}")
"""