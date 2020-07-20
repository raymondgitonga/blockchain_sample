import datetime
import hashlib
import _json
from flask import Flask

class Blockchain:
    def __init__(self):
        self.chain = []
        self.creat_block(proof = 1, previous_hash = '0')

