#!/usr/bin/env python3
import bitcoin

class BitcoinKeyGenerator():
    
    def __init__(self):
        # GENERATE PRIVATE KEYS 
        self.private_key = bitcoin.random_key()
        self.decoded_private_key = bitcoin.decode_privkey(self.private_key, 'hex')
        self.wif_encoded_private_key = bitcoin.encode_privkey(self.decoded_private_key, 'wif')
        self.compressed_private_key = self.private_key + '01'
        # ALL PUBLIC KEYS
        self.public_key = bitcoin.fast_multiply(bitcoin.G, self.decoded_private_key)
        self.hex_encoded_public_key = bitcoin.encode_pubkey(self.public_key, 'hex')
        self.hex_compressed_public_key = self.generateHexCompressedPublicKey(self.public_key)
        self.bitcoinAddress = bitcoin.pubkey_to_address(self.public_key)
        self.compressedBitcoinAddress = bitcoin.pubkey_to_address(self.hex_compressed_public_key.encode('utf-8'))
        # self.compressed_address_base58check = bitcoin.pubkey_to_address(self.hex_compressed_public_key)
        
    def checkIfPrivateKeyIsValid(self):
        return 0 < self.decoded_private_key < bitcoin.N
    
    def generateHexCompressedPublicKey(self, public_key):
        (public_key_x, public_key_y) = public_key
        if public_key_y % 2 == 0:
          compressed_prefix = '02'
        else:
          compressed_prefix = '03'
        return compressed_prefix + bitcoin.encode(public_key_x, 16)