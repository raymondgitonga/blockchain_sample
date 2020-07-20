import datetime
import hashlib
import json
from flask import Flask


class Blockchain:
    def __init__(self):
        self.chain = []
        self.creat_block(proof=1, previous_hash='0')

    # genesis block
    def create_block(self, proof, previous_hash):
        block = {'index': len(self.chain) + 1,
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash}
        self.chain.append(block)
        return block
