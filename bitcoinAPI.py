
'''
How to make a Bitcoin transaction with Python:
https://dev.to/nownodes/how-to-make-a-bitcoin-transaction-with-python-54k4
'''

from bit import PrivateKeyTestnet, Key
import config

class BitcoinAPI():

    def __init__(self):
        self.CURRENCY = config.params["CURRENCY"]
        self.TX_AMOUNT = config.params["TX_AMOUNT"]
        self.DEAFULT_MESSAGE_SUFFIX = config.params["DEAFULT_MESSAGE_SUFFIX"]
    
    def load_wallet(self, wallet_wif, is_test=False):
        # get sending wallet/address info
        if is_test:
            key = PrivateKeyTestnet(wallet_wif) #create new: PrivateKeyTestnet()
        else:
            key = Key(wallet_wif)
        print("version: ", key.version)
        print("wif: ", key.to_wif())
        print("address: ", key.address)
        print("balance: ", key.get_balance(self.CURRENCY), self.CURRENCY)
        
        return key
    
    def execute(self, key, receiving_address, tweet_text):
        # execute a transaction and store tweet on bitcoin's blockchain
        blockchain_message = tweet_text + self.DEAFULT_MESSAGE_SUFFIX
        tx_hash = key.send([(receiving_address, self.TX_AMOUNT, self.CURRENCY)], message=blockchain_message)
        print("TxID: ", tx_hash)
        print("Verify that the message was stored in the OP_RETURN field using a Bitcoin blockchain explorer like: https://blockstream.info/testnet/ (test) or https://blockstream.info/ (prod)")


def main():
    #private key of sending wallet in WIF format
    SENDING_WALLET_WIF = config.params["TEST_SENDING_WALLET_WIF"]
    # receiving_address
    RECEIVING_ADDRESS = config.params["TEST_RECEIVING_ADDRESS"]
    # message to store with the transaction on the blockchain. Must not exceed 40 bytes. Encoded as UTF-8 (eg: 😀 is 4 bytes)
    TEST_MESSAGE = 'test message'
    
    # create/execute transaction and store message
    bit = BitcoinAPI()
    my_key = bit.load_wallet(SENDING_WALLET_WIF, is_test=True)
    bit.execute(my_key, RECEIVING_ADDRESS, TEST_MESSAGE)
    

if __name__ == "__main__":
    main()

