from AarushCoin import *
from time import time
import pprint

prettyPrint = pprint.PrettyPrinter(indent=4)
blockchain = Blockchain()

key = blockchain.generateKeys()

blockchain.addTransaction("Person 1", "Person 2", 100, key, key)

blockchain.minePendingTransactions("Aarush")
blockchain.minePendingTransactions("Arjun")

prettyPrint.pprint(blockchain.packageChain())
print(f"Length: {len(blockchain.chain)}")