"""Проверка валидности блокчейна"""
from wallet import Wallet

import hashlib


class Verification:
    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        if check_funds:
            return get_balance(transaction.sender) >= transaction.amount and Wallet.verify_transaction(transaction)
        else:
            return Wallet.verify_transaction(transaction)

    @classmethod
    def verify_chain(cls, blockchain, get_hash):
        for (index, el) in enumerate(blockchain):
            if index == 0:
                continue
            if el.previous_hash != get_hash(blockchain[index - 1]):
                return False
            if not cls.valid_proof(el.transactions[:-1], el.previous_hash, el.proof_number):
                print("Proof of work is invalid")
                return False
        return True

    @staticmethod
    def valid_proof(transactions, previous_hash, proof_number):
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(previous_hash) + str(proof_number)).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[0:2] == '00'

