from blockchain import Blockchain
from wallet import Wallet


class Node:
    def __init__(self):
        self.wallet = Wallet()
        self.wallet.create_keys()
        self.blockchain = Blockchain(self.wallet.public_key)


    def interface(self):

        go_on = True
        while go_on:

            print(self.blockchain.get_balance())
            print(self.blockchain.wallet)

            print("Please choose:")
            print("1: Add a new transaction value")
            print("2: Mine a new block")
            print("3: Output the blockchain")
            print("4: Create key")
            print("5: Load key")
            print("6: Save key")
            print("q: Quit")

            go_on = self.select()
            # print(f'{my_name} coins: {get_balance(my_name):.2f}')
            # if not exept_manipulations():
            #     print("THE BLOCKCHAIN WAS CHANGED")
            #     break

    def select(self):
        choose = input("Make choise: ")
        if choose == '1':
            print()
            self.input_new_transaction()
            return True
        elif choose == '2':
            print()
            if not self.blockchain.mine_block():
                print('You have no wallet')
            return True
        elif choose == '3':
            print()
            self.output_blockchain()
            return True
        elif choose == '4':
            print()
            self.wallet.create_keys()
            self.blockchain.wallet = self.wallet.public_key
            return True
        elif choose == '5':
            self.wallet.load_keys()
            self.blockchain = Blockchain(self.wallet.public_key)
            return True
        elif choose == '6':
            self.wallet.save_keys()
            self.blockchain = Blockchain(self.wallet.public_key)
            return True
        elif choose == 'q':
            return False
        else:
            print("Enter correct symbol!")
            return True

    # def print_participants(self):
    #     print(participants)

    def output_blockchain(self):
        for block in self.blockchain.get_chain():
            print(block)

    def input_new_transaction(self):
        recipient = input("Enter recipient: ")
        amount = float(input("Enter amount: "))
        signature = self.wallet.sign_transaction(self.wallet.public_key, recipient, amount)
        if not self.blockchain.add_new_transaction(recipient, signature, amount):
            print('No wallet')


node = Node()
node.interface()